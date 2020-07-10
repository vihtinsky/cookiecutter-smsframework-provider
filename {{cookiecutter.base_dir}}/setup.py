#! /usr/bin/env python
""" SMS framework: {{ cookiecutter.provider}} provider """

from setuptools import setup, find_packages

setup(
    # http://pythonhosted.org/setuptools/setuptools.html
    name='smsframework-{{ cookiecutter.provider_slug}}',
    version='0.0.1-0',
    author='{{ cookiecutter.full_name}}',
    author_email='{{ cookiecutter.email}}',

    url='https://github.com/{{ cookiecutter.github_username}}/py-smsframework-{{ cookiecutter.provider_slug}}',
    license='BSD',
    description=__doc__,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=['sms', 'message', 'notification', 'receive', 'send', '{{ cookiecutter.provider_slug}}'],

    packages=find_packages(),
    scripts=[],
    entry_points={},

    install_requires=[
        'smsframework >= 0.0.9',
    ],
    extras_require={
        'receiver': ['flask >= 0.10'],  # sms receiving
    },
    test_suite='nose.collector',
    include_package_data=True,

    platforms='any',
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
)
