#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'six', 'requests', 'arrow'
]

test_requirements = [
   'pytest',
   'requests_staticmock'
]

setup(
    name='pysaba',
    version='1.1.0',
    description="Sabat client library for API management",
    long_description=readme + '\n\n' + history,
    author="Anthony Shaw",
    author_email='anthonyshaw@apache.org',
    url='https://github.com/tonybaloney/pysaba',
    packages=[
        'saba'
    ],
    package_dir={'saba':
                 'saba'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache License (2.0)",
    zip_safe=False,
    keywords='sabat',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    tests_require=test_requirements,
    setup_requires=['pytest-runner']
)
