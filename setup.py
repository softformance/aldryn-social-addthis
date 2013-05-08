# -*- coding: utf-8 -*-
from setuptools import setup
from aldryn_social_sharing import __version__

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
    name='aldryn-social-sharing',
    version=__version__,
    description='Allows sharing CMS content via social media',
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/aldryn/aldryn-social-sharing',
    packages=['aldryn_social_sharing'],
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=REQUIREMENTS,
    include_package_data=True,
    zip_safe=False
)
