django-user-unique-email
========================

Reusable User model with required unique email field and mid-project support.

It defines custom User model reusing of the original table (auth_user) if exists.
If needed (when added to existing project),
it recreates history of applied migrations in the correct order.


Adding to existing project
--------------------------

* **Backup the database**
* **Ensure that any reference to User model (in your project and all third-party apps) uses 'AUTH_USER_MODEL' setting or 'get_user_model'.**
* **Ensure that there are no duplicit or empty emails in table 'auth_user'.**
* **Test it on a clone of your project, before you try to deploy it to production server.**


Installation
------------

.. code:: shell

    pip install django-user-unique-email


Configuration
-------------

Add 'user_unique_email' to INSTALLED_APPS and set AUTH_USER_MODEL in settings:

.. code:: python

    # Add user_unique_email to INSTALLED_APPS
    INSTALLED_APPS.append('user_unique_email')

    # Custom User model
    AUTH_USER_MODEL = 'user_unique_email.User'
