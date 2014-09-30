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

Before you use this library in your applications you may wish to demo its functionality. To do so, follow these steps::

    $ virtualenv .
    $ bin/pip install django-pci-auth
    $ bin/django-admin.py syncdb --settings=django_pci_auth.settings
    $ bin/django-admin.py runserver --settings=django_pci_auth.settings

Open http://127.0.0.1:8000/

Libraries
---------

A list of libraries included:

- http://code.google.com/p/py-bcrypt/
- https://github.com/codekoala/django-axes
- https://github.com/dstufft/django-passwords

Articles
--------

- https://docs.djangoproject.com/en/1.4/topics/auth/
- https://docs.djangoproject.com/en/1.4/topics/auth/#using-bcrypt-with-django
- https://docs.djangoproject.com/en/1.4/topics/auth/#increasing-the-work-factor
- https://docs.djangoproject.com/en/1.4/topics/http/sessions/#session-cookie-age
- http://kencochrane.net/blog/2012/01/developers-guide-to-pci-compliant-web-applications/
- http://stackoverflow.com/questions/2693837/django-staff-decorator
- http://stackoverflow.com/questions/3566174/django-increase-inactivity-timeout
- http://stackoverflow.com/questions/5179635/django-account-lockout
- http://stackoverflow.com/questions/5226329/enforcing-password-strength-requirements-with-django-contrib-auth-views-password
- http://stackoverflow.com/questions/13055722/enforcing-password-strength-requirements-in-django
- http://www.egrappler.com/jquery-strong-password-plugin-power-pwchecker/
- http://www.insomnihack.com/?p=451
- http://www.elementps.com/merchants/pci-dss/compliance-level/

Settings
--------

Stronger password hashing
~~~~~~~~~~~~~~~~~~~~~~~~~

This is a built-in feature in Django 1.4+. Documented here for convenience::

    PASSWORD_HASHERS = (
        # From https://docs.djangoproject.com/en/1.4/topics/auth/:
        # "[redacted] This means that Django will use the first hash in the list
        # to store all passwords, but will support checking passwords stored with
        # the rest of the hashes in the list. If you remove a hash from the list
        # it will no longer be supported.
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

Feature overview (via index view)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://raw.github.com/aclark4life/django-pci-auth/master/docs/screenshot-index.png

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
