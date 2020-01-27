from django.core.management.commands.migrate import Command as _Command
from django.db import connections
from django.db.migrations.recorder import MigrationRecorder


def _has_table(recorder):
    try:
        return recorder.has_table()
    except AttributeError:
        # Django < 2
        recorder.ensure_schema()
        return True


class Command(_Command):
    def handle(self, *args, **options):
        # Get the database we're operating from
        db = options['database']
        connection = connections[db]

        # Hook for backends needing any database preparation
        connection.prepare_database()

        # Detect mid-project installation
        recorder = MigrationRecorder(connection)
        if (
            _has_table(recorder)
            and recorder.migration_qs.filter(app='auth').exists()
            and not recorder.migration_qs.filter(app='user_unique_email').exists()
        ):
            # Auto fake initial migration
            migrations = [recorder.Migration(app='user_unique_email', name='0001_initial')] + [
                recorder.Migration(app=m.app, name=m.name)
                for m in recorder.migration_qs.iterator()
            ]
            recorder.flush()
            recorder.migration_qs.bulk_create(migrations)

        # Go on with normal migrate command
        return super().handle(*args, **options)
