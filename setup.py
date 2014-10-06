from setuptools import find_packages
from setuptools import setup
import os

VERSION = '0.0.7'

setup(
    author='Alex Clark',
    author_email='aclark@aclark.net',
    description='Integrates existing PCI-related applications and provides additional PCI-related features.',
    include_package_data=True,
    install_requires=[
        'Django>=1.4',
        'django-axes>=1.2.6',
        'django-admin-bootstrapped',
        'django-dajaxice',
        'django-passwords',
        'django-password-policies',
        'docutils',
        'py-bcrypt',
        'pytz',
    ],
    long_description=(
        open("README.rst").read() + '\n' +
        open("CHANGES.txt").read()),
    name='django-pci-auth',
    packages=find_packages(),
    url='https://github.com/django-security/django-pci-auth',
    version=VERSION,
)
