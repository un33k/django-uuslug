import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='django-uuslug',
    version='0.8',
    description = "A Django slugify application that guarantees uniqueness and handles unicode",
    long_description = read('README'),
    author='Val Neekman',
    author_email='val@neekware.com',
    url='http://github.com/un33k/django-uuslug',
    packages=['uuslug'],
    install_requires = ['Unidecode>=0.04.5'],
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Utilities'],
    )
