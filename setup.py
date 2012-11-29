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
        'django-axes==1.2.5',  # XXX Never do this. Only Doing it here because 
                                # pkg_resources thinks 1.2.5-rc1 is newer than
                                 # 1.2.5
        'django-admin-bootstrapped',
        'django-passwords',
        'docutils',
        'py-bcrypt',
    ],
    long_description=open("README.rst").read(),
    name='django-pci-auth',
    packages=find_packages(),
    url='https://github.com/aclark4life/django-pci-auth',
    version=VERSION,
)
