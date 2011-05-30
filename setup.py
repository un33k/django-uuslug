import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-uslug",
    version = "0.1",
    url = 'http://github.com/un33k/django-uslug',
    license = 'BSD',
    description = "A Unicode slug that is also guaranteed to be unique",
    long_description = read('README'),
    author = 'Val L33',
    author_email = 'val@neekware.com',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools', 'Unidecode>=0.04.5'],

    classifiers = [
        'Development Status :: 1 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)