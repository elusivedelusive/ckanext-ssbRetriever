#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '0.1'

setup(
    name='ckanext-ssbRetriever',
    version='0.1',

    description='''plugin for å hente data fra ssb med post requets for Stavanger Kommune''',
    long_description='''Contributors:
    Jonatan Hoff <jonatan.hoff@acando.no>
    ''',
    url='https://github.com/elusivedelusive/ssbRetriever',
    author='Jonatan Hoff',
    author_email='jonatan.hoff@gmail.com',
    license='',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='CKAN POST SSB',
    namespace_packages=['ckanext', 'ckanext.ssbRetriever'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[],
    include_package_data=True,
    entry_points='''
        [ckan.plugins]
        ssbRetriever=ckanext.ssbRetriever.plugin:ssbRetriever
    ''',
)
