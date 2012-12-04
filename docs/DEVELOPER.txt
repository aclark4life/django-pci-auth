Models
------

These models help provide the features listed above and are either included with django-pci-auth or one of its dependencies.

UserProfile
~~~~~~~~~~~

Profile model that stores two fields that are required (nolockout, and password_last_changed). If you already have a Profile model you will need to add these fields to it.

Fields:

- user (ForeignKey to User)
- nolockout (Boolean)
- password_last_changed (datetime)

AccessLog
~~~~~~~~~

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
~~~~~~~~~~~

Keeps track of the recently used passwords for a user, so that they aren't allowed to reuse the same ones over and over again.

Fields:

- user (ForeignKey to User)
- password (CharField 128 max)
- create_date (datetime)
