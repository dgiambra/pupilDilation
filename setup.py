#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pupilDilation',
    version='0.1.0',
    description="Code written for Hackats pupil state using facial recognition.",
    long_description=readme + '\n\n' + history,
    author="Dominic James Giambra",
    author_email='dgiambra@u.rochester.edu',
    url='https://github.com/dgiambra/pupilDilation',
    packages=[
        'pupilDilation',
    ],
    package_dir={'pupilDilation':
                 'pupilDilation'},
    entry_points={
        'console_scripts': [
            'pupilDilation=pupilDilation.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='pupilDilation',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
