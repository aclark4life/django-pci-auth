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
        'Django>=1.4',
        'docutils',
        'django-passwords',
        'py-bcrypt',
    ],
    long_description=open("README.rst").read(),
    name='django-pci-auth',
    packages=[
        'django_pci_auth',
        'axes',
    ],
    package_dir={
        'django_pci_auth': 'django_pci_auth',
        '': 'django-axes',
    },
    url='https://github.com/aclark4life/django-pci-auth',
    version=VERSION,
)
