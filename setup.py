from setuptools import find_packages
from setuptools import setup
import os

VERSION = '0.0.1'

setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    description='PCI-compliant authentication application for Django 1.4+. '
        'Uses "best of" existing libraries then fills in the gaps.',
    include_package_data=True,
    install_requires=[
        'docutils',
#        'django-axes',  # 1.2.5rc1 has bad setup.py
        'django-passwords',
        'py-bcrypt',
    ],
    long_description=open("README.rst").read(),
    name='django-pci-auth',
    packages=[
        'axes',
    ],
    package_dir={
        '': 'django-axes',
    },
    version=VERSION,
)
