#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import re
import os
import sys


name = 'django-uuslug'
package = 'uuslug'
description = 'A Django slugify application that guarantees uniqueness and handles unicode.'
url = 'https://github.com/un33k/django-uuslug'
author = 'Val Neekman'
author_email = 'info@neekware.com'
license = 'BSD'
install_requires = ['python-slugify>=1.2.0']
classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Framework :: Django :: 1.11',
    'Framework :: Django :: 2.1',
    'Framework :: Django :: 2.2',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
]


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    args = {'version': get_version(package)}
    print("You probably want to also tag the version now:")
    print("  git tag -a %(version)s -m 'version %(version)s' && git push --tags" % args)
    sys.exit()


setup(
    name=name,
    version=get_version(package),
    url=url,
    license=license,
    description=description,
    author=author,
    author_email=author_email,
    packages=get_packages(package),
    package_data=get_package_data(package),
    install_requires=install_requires,
    classifiers=classifiers
)
