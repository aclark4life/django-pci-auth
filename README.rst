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

Overview
--------

PCI is complex. Here is a bit of background on the subject. Inasmuch as it's possible to summarize here.

Levels
~~~~~~

- PCI Compliance Level 1 - Merchants processing over 6 million Visa transactions annually (all channels) or Global merchants identified as Level 1 by any Visa region
- PCI Compliance Level 2 - Merchants processing 1 million to 6 million Visa transactions annually (all channels)
- PCI Compliance Level 3 - Merchants processing 20,000 to 1 million Visa e-commerce transactions annually
- PCI Compliance Level 4 - Merchants processing less than 20,000 Visa e-commerce transactions annually and all other merchants processing up to 1 million Visa transactions annually

Via: http://www.elementps.com/merchants/pci-dss/compliance-level/

Libraries
---------

A list of libraries included:

**XXX** In flux

- http://www.djangopackages.com/grids/g/authorization/
- http://code.google.com/p/django-axes/
- http://ianlewis.bitbucket.org/django-newauth/
- https://github.com/dstufft/django-passwords/

Articles
--------

A list of articles:

- http://www.insomnihack.com/?p=451

License
-------

This software is licensed under the same BSD license that Django is licensed under. See: `LICENSE`_.

.. _`LICENSE`: https://github.com/aclark4life/django-pci-auth/blob/master/LICENSE
