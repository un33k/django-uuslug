from distutils.core import setup

setup(name='django-uuslug',
    version='0.2',
    description = "A Unicode slug that is also guaranteed to be unique",
    author='Val L33',
    author_email='val@neekware.com',
    url='http://bitbucket.org/un33k/django-uuslug',
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
