#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup(
    author="st1vms",
    author_email='stefano.maria.salvatore@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description="Extends Selenium to give you the ability to inspect requests made by the browser.",
    license="MIT",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        'blinker>=1.7.0', # Fixes blnker import error
        'brotli>=1.0.9',
        'certifi>=2019.9.11',
        "h2>=4.0; python_version>='3.6.0'",
        "hyperframe>=6.0; python_version>='3.6.0'",
        'kaitaistruct>=0.7',
        'pyasn1>=0.3.1',
        'pyOpenSSL>=22.0.0',
        'pyparsing>=2.4.2',
        'pysocks>=1.7.1',
        'selenium>=4.0.0',
        'wsproto>=0.14',
        'zstandard>=0.14.1',
    ],
    extras_require={
        ':sys_platform == "win32"': [
            'pydivert>=2.0.3',
        ],
        ':python_version == "3.6"': [
            "dataclasses>=0.7",
        ],
        'dev': [
            'black',
            'bumpversion',
            'coverage',
            'flake8',
            'gunicorn',
            'httpbin',
            'isort',
            "mitmproxy>5.3.0; python_version>='3.8.0'",  # Needed for end2end tests
            'mypy',
            'pre-commit',
            'pytest',
            'pytest-cov',
            'tox',
            'twine',
            'werkzeug==2.0.3',
            'wheel',
        ],
    },
    keywords='selenium-wire',
    name='selenium-wire',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    setup_requires=[],
    test_suite='tests.seleniumwire',
    tests_require=['pytest'],
    url='https://github.com/st1vms/selenium-wire-fork',
    version='5.1.0',
    zip_safe=False,
)
