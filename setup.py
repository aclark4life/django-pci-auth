from setuptools import find_packages
from setuptools import setup
import os

VERSION = '0.0.2'

setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    description='PCI-compliant authentication application for Django 1.4+. '
        'Uses "best of" existing libraries then fills in the gaps.',
    include_package_data=True,
    install_requires=[
        'docutils',
#        'django-axes',  # 1.2.5-rc1 has bad setup.py
        'django-passwords',
        'py-bcrypt',
    ],
    long_description=open("README.rst").read(),
    name='django-pci-auth',
    packages=[
        'axes',
        'django_pci_auth',
    ],
    package_dir={
        'axes': 'django-axes',  # Hack-a-round
        'django_pci_auth': 'django_pci_auth',
    },
    url='https://github.com/aclark4life/django-pci-auth',
    version=VERSION,
)
