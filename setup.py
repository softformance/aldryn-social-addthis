# -*- coding: utf-8 -*-
from setuptools import setup
from aldryn_social_addthis import __version__

REQUIREMENTS = [
    'django-filer',
    'django-social-tags',
    'pillow',
]

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    name='aldryn-social-addthis',
    version=__version__,
    description='Allows sharing content via addthis integration',
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/aldryn/aldryn-social-addthis',
    packages=['aldryn_social_addthis'],
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=REQUIREMENTS,
    include_package_data=True,
    zip_safe=False
)
