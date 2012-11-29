django-pci-auth
===============

**Django 1.4+ only**

This library integrates the current Django "best of" PCI auth libraries into a single application, then fills in the gaps. Filling gaps may involve making additional decisions for you, as suggested by Django Documentation e.g.:

- https://docs.djangoproject.com/en/1.4/topics/auth/#using-bcrypt-with-django
- https://docs.djangoproject.com/en/1.4/topics/auth/#increasing-the-work-factor
- https://docs.djangoproject.com/en/1.4/topics/http/sessions/#session-cookie-age

Or in some cases additional functionality may be provided by this library e.g.:

- Database models to persist event data e.g. lockouts

Features
--------

- Stronger password hashing that allows for selection of hashing algorithm scrypt, bcrypt, PBKDF2, etc. via settings.py. [1]
- Checking for strong passwords with a default length setting overrideable in settings.py. [2]
- Integrate strong passwords into Django Admin.
- Lock out account for n minutes after x failed log-in attempts. [3]
- Set inactivity timeouts.
- Generate event/email when lock-out occurs.
- Set flags disallowing certain accounts to be locked out.
- Log every log-on and explicit log-out (not necessary to log timed out log-ins).
- Track last four passwords and do not allow re-use.
- Force password reset after X amount of time.

**XXX Below not done**

- Provide JavaScript to check for strong passwords inline.

  - Javascript code should check the Django settings via AJAX re: password length min/max, etc.

Installation
------------

Before you use this library in your applications you may wish to demo its functionality. To do so, follow these steps::

    $ virtualenv .
    $ bin/pip install django-pci-auth
    $ bin/django-admin.py syncdb --settings=django_pci_auth.settings
    $ bin/django-admin.py runserver --settings=django_pci_auth.settings

Open http://127.0.0.1:8000/

Libraries
~~~~~~~~~

A list of libraries included:

- https://github.com/codekoala/django-axes
- https://github.com/dstufft/django-passwords

**XXX Not included yet but may be**

- http://code.google.com/p/django-brutebuster
- https://github.com/alexkuhl/django-failedloginblocker
- https://github.com/brianjaystanley/django-lockout

Articles
~~~~~~~~

A list of relevant articles:

- http://stackoverflow.com/questions/3566174/django-increase-inactivity-timeout
- http://stackoverflow.com/questions/5226329/enforcing-password-strength-requirements-with-django-contrib-auth-views-password
- http://stackoverflow.com/questions/13055722/enforcing-password-strength-requirements-in-django
- http://www.egrappler.com/jquery-strong-password-plugin-power-pwchecker/
- http://www.insomnihack.com/?p=451
- http://stackoverflow.com/questions/5179635/django-account-lockout
- http://kencochrane.net/blog/2012/01/developers-guide-to-pci-compliant-web-applications/
- http://stackoverflow.com/questions/2693837/django-staff-decorator
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

How many old passwords will you store? This will prevent users from using the same password over again. It will keep the newest ones around. As they change their password, the older ones will be removed.

    OLD_PASSWORD_STORAGE_NUM = 4

Screenshots
-----------

Overview of features
~~~~~~~~~~~~~~~~~~~~

.. image:: https://raw.github.com/aclark4life/django-pci-auth/master/screenshot-index.png

Password length enforcement
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://raw.github.com/aclark4life/django-pci-auth/master/screenshot.png

Failed login attempts log
~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://raw.github.com/aclark4life/django-pci-auth/master/screenshot-axes.png

License
-------

This software is licensed under the same BSD license that Django is licensed under. See: `LICENSE`_.

.. _`LICENSE`: https://github.com/aclark4life/django-pci-auth/blob/master/LICENSE


Developer
---------

Models
~~~~~~

These models help provide the features listed above and are either included with django-pci-auth or one of its dependencies.

UserProfile
+++++++++++

Profile model that stores two fields that are required (nolockout, and password_last_changed). If you already have a Profile model you will need to add these fields to it.

Fields:
    - user (ForeignKey to User)
    - nolockout (Boolean)
    - password_last_changed (datetime)

AccessLog
+++++++++

A permeant log that tracks all of the access attempts.

Fields:
    - user_agent (CharField 255)
    - ip_address (IpAddress)
    - user (ForeignKey User)
    - trusted (Boolean)
    - http_accept (CharField 255 max)
    - path_info (CharField 255 max)
    - attempt_time (datetime)
    - logout_time (datetime)

PasswordLog
+++++++++++

Keeps track of the recently used passwords for a user, so that they aren't allowed to reuse the same ones over and over again.

Fields:
    - user (ForeignKey to User)
    - password (CharField 128 max)
    - create_date (datetime)

.. [1] This feature is included with Django 1.4+
.. [2] This feature is provided by django-passwords
.. [3] This feature is provided by django-axes
