
django-pci-auth
===============

This project integrates the current "best of" PCI auth libraries in to a single application, then fills in the gaps.

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

XXX Fill in libs
