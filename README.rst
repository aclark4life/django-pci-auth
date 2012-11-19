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

**XXX Below not done**

- Provide JavaScript to check for strong passwords inline.

  - Javascript code should check the Django settings via AJAX re: password length min/max, etc.

- Generate event/email when lock-out occurs.
- Set flags disallowing certain accounts to be locked out.

  - Persist beyond restart

- Log every log-on and explicit log-out (not necessary to log timed out log-ins).

  - Persist beyond restart

- Track last four passwords and do not allow re-use.

  - Persist beyond restart

- Force password reset after X amount of time.

  - Persist beyond restart

Installation
------------

Before you use this library in your applications you may wish to demo its functionality. To do so, follow these steps::

    $ virtualenv .
    $ bin/pip install django-pci-auth
    $ bin/django-admin.py syncdb --settings=django_pci_auth.settings
    $ bin/django-admin.py runserver --settings=django_pci_auth.settings

Open http://127.0.0.1:8000/

Background
----------

PCI is complex. Here is a bit of background on the subject. Inasmuch as it's possible to summarize here.

Levels
~~~~~~

**XXX Do we need to worry about levels?**

- PCI Compliance Level 1 - Merchants processing over 6 million Visa transactions annually (all channels) or Global merchants identified as Level 1 by any Visa region
- PCI Compliance Level 2 - Merchants processing 1 million to 6 million Visa transactions annually (all channels)
- PCI Compliance Level 3 - Merchants processing 20,000 to 1 million Visa e-commerce transactions annually
- PCI Compliance Level 4 - Merchants processing less than 20,000 Visa e-commerce transactions annually and all other merchants processing up to 1 million Visa transactions annually

Via: http://www.elementps.com/merchants/pci-dss/compliance-level/

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

.. [1] This feature is included with Django 1.4+
.. [2] This feature is provided by django-passwords
.. [3] This feature is provided by django-axes


Development
-----------

Issues
~~~~~~

Django-axes has been included here as a git submodule. But due to a bug in setuptools, this only works during installation (i.e. not during "python setup.py develop". See: https://bitbucket.org/tarek/distribute/issue/177/setuppy-develop-doesnt-support-package_dir). To workaround the issue, try something like::

    from django.core import management

    import sys  # Hack-a-round setuptools 'python setup.py develop' bug
    sys.path.append('')

    if __name__ == "__main__":
        management.execute_from_command_line()




