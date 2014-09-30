django-pci-auth
===============

.. Warning::

    This application validates passwords via **un-encrypted AJAX** communication. Please **use with SSL only**!

Introduction
------------

Provides integration with existing PCI-related features and adds additional functionality to deliver a uniform application. Helps you build PCI-compliant websites with Django, but offers no guarantees of compliance.

Features
--------

- Stronger password hashing that allows for selection of hashing algorithm scrypt, bcrypt, PBKDF2, etc. via settings.py. [1]
- Checking for strong passwords with a default length setting overrideable in settings.py. [2]
- Integrate strong passwords into Django Admin.
- Lock out account for n minutes after x failed log-in attempts. [3]
- Set inactivity timeouts.
- Generate event/email when lock-out occurs. [4]
- Set flags disallowing certain accounts to be locked out.
- Log every log-on and explicit log-out (not necessary to log timed out log-ins).
- Track last four passwords and do not allow re-use. [5]
- Force password reset after X amount of time.
- Provide JavaScript to check for strong passwords inline.

Installation
------------

::

    $ virtualenv .
    $ bin/pip install django-pci-auth
    $ bin/django-admin.py syncdb --settings=django_pci_auth.settings
    $ bin/django-admin.py runserver --settings=django_pci_auth.settings

Open http://127.0.0.1:8000/

Settings
--------

Stronger password hashing
~~~~~~~~~~~~~~~~~~~~~~~~~

This is a built-in feature in Django 1.4+. Documented here for convenience::

    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
        'django.contrib.auth.hashers.BCryptPasswordHasher',
        'django.contrib.auth.hashers.SHA1PasswordHasher',
        'django.contrib.auth.hashers.MD5PasswordHasher',
        'django.contrib.auth.hashers.CryptPasswordHasher',
    )

Password Reuse
~~~~~~~~~~~~~~

How many old passwords will you store? This feature will prevent users from using the same passwords over and over again; it will keep the last ``OLD_PASSWORD_STORAGE_NUM`` number of passwords around and remove anything older. E.g.::

    OLD_PASSWORD_STORAGE_NUM = 4

Screenshots
-----------

Password length enforcement (with AJAX validation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://raw.github.com/aclark4life/django-pci-auth/master/docs/screenshot-ajax.png

Failed login attempts log
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://raw.github.com/aclark4life/django-pci-auth/master/docs/screenshot-axes.png

Recently used password log
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://raw.github.com/aclark4life/django-pci-auth/master/docs/screenshot-axes.png

.. [1] Included with Django 1.4+
.. [2] Provided by django-passwords
.. [3] Provided by django-axes
.. [4] https://github.com/django-security/django-pci-auth/blob/master/docs/MODELS.rst
.. [5] https://github.com/django-security/django-pci-auth/blob/master/django_pci_auth/validators.py#L9
