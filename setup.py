from setuptools import setup, find_packages
import os

DESCRIPTION = "A Django email backend for Mailgun"

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    pass

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Framework :: Django',
]

setup(
    name='django-mailgun',
    version='0.1',
    packages=['django_mailgun'],
    author='Bradley Whittington',
    author_email='radbrad182@gmail.com',
    url='http://github.com/bradwhittington/django-mailgun/',
    license='MIT',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    platforms=['any'],
    classifiers=CLASSIFIERS,
    install_requires=['mailgun.py'],
)
