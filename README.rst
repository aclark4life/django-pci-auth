
django-pci-auth
===============

This application integrates the current Django "best of" PCI auth libraries into a single application, then fills in the gaps.

Requirements
------------

- stronger password hashing that allows run time selection of hashing algoritm scrypt, bcrypt, PBKDF2, etc. via settings.py
- checking for 'strong' passwords. again with a default and overrideable in settings.py
- provide JavaScript as well as Django-side checking for 'strong' passwords.
- integrate strong passwords into Admin.
- log every log-on and explicit log-out (not necessary timed out log-ins).
- set inactivity timeouts.
- track last four passwords and do not allow re-use.
- lock out account for n minutes after x failed log-in attempts.
- set flags disallowing certain accounts to be locked out.
- generate event/email when lock-out occurs.
- force password reset after X amount of time.

Libraries
---------

**XXX** Fill in list of current "best of" libraries in existence e.g. http://www.djangopackages.com/grids/g/authorization/

License
-------

This software is licensed under the same BSD license that Django is licensed under. See: `LICENSE`_.

.. _`LICENSE`: https://github.com/aclark4life/django-pci-auth/blob/master/LICENSE
