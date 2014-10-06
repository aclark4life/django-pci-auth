django-pci-auth
===============

.. Warning::

    This application validates passwords via **un-encrypted AJAX** communication. Please **use with SSL only**!

Introduction
------------

Integrates existing PCI-related applications and provides additional PCI-related features.

Features
--------

Installation
------------

::

    $ virtualenv .
    $ bin/pip install django-pci-auth

Demo
~~~~

::

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
