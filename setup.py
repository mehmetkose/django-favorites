from distutils.core import setup

setup(
    name = 'favorites',
    version = '0.2',
    description = 'Generic favorites application for Django',
    author = 'Jakub Zalewski forked Andrew Gwozdziewycz',
    author_email = 'zalew7@gmail.com, git@apgwoz.com',
    packages = ['favorites'],
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)
