django-pci-auth
===============

**Django 1.4+ only**

This application integrates the current Django "best of" PCI auth libraries into a single application, then fills in the gaps. Filling gaps may involve making additional decisions for you, as suggested by Django Documentation e.g.:

- https://docs.djangoproject.com/en/1.4/topics/auth/#using-bcrypt-with-django
- https://docs.djangoproject.com/en/1.4/topics/auth/#increasing-the-work-factor

Or in some cases, additional functionality may be provided by this package e.g.:

- XXX Add example

Features
--------

**XXX Done**

- Stronger password hashing that allows for selection of hashing algorithm scrypt, bcrypt, PBKDF2, etc. via settings.py. [1]
- Checking for strong passwords with a default length setting overrideable in settings.py. [2]
- Integrate strong passwords into Django Admin.

**XXX Not done**

- provide JavaScript as well as Django-side checking for 'strong' passwords.
- log every log-on and explicit log-out (not necessary timed out log-ins).
- set inactivity timeouts.
- track last four passwords and do not allow re-use.
- lock out account for n minutes after x failed log-in attempts.
- set flags disallowing certain accounts to be locked out.
- generate event/email when lock-out occurs.
- force password reset after X amount of time.

Background
----------

PCI is complex. Here is a bit of background on the subject. Inasmuch as it's possible to summarize here.

Levels
~~~~~~

- PCI Compliance Level 1 - Merchants processing over 6 million Visa transactions annually (all channels) or Global merchants identified as Level 1 by any Visa region
- PCI Compliance Level 2 - Merchants processing 1 million to 6 million Visa transactions annually (all channels)
- PCI Compliance Level 3 - Merchants processing 20,000 to 1 million Visa e-commerce transactions annually
- PCI Compliance Level 4 - Merchants processing less than 20,000 Visa e-commerce transactions annually and all other merchants processing up to 1 million Visa transactions annually

Via: http://www.elementps.com/merchants/pci-dss/compliance-level/

Libraries
~~~~~~~~~

A list of libraries included:

**XXX** In flux

- http://www.djangopackages.com/grids/g/authorization/
- http://code.google.com/p/django-axes/
- http://ianlewis.bitbucket.org/django-newauth/
- https://github.com/dstufft/django-passwords/

Articles
~~~~~~~~

A list of relevant articles:

- http://www.insomnihack.com/?p=451
- http://stackoverflow.com/questions/11257607/customising-the-django-admin-change-password-page
- http://stackoverflow.com/questions/5226329/enforcing-password-strength-requirements-with-django-contrib-auth-views-password
- http://stackoverflow.com/questions/13055722/enforcing-password-strength-requirements-in-django

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

Screenshots
-----------

Password length enforcement
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: https://raw.github.com/aclark4life/django-pci-auth/master/screenshot.png

License
-------

This software is licensed under the same BSD license that Django is licensed under. See: `LICENSE`_.

.. _`LICENSE`: https://github.com/aclark4life/django-pci-auth/blob/master/LICENSE

.. [1] This feature is included with Django 1.4+
.. [2] This feature is provided by django-passwords

