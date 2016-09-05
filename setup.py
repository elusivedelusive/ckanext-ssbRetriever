from setuptools import setup, find_packages

version = "0.1"

setup(
    name="ckanext-ssbRetriever",
    version="0.1",

    description="Grafisk brukergrensesnitt for aa kjore POST queries mot SSB utviklet for Stavanger Kommune",
    long_description='''Contributors:
    Jonatan Hoff <jonatan.hoff@gmail.com>''',
    author = "Jonatan Hoff",
    author_email = "jonatan.hoff@gmail.com",
    url="https://github.com/elusivedelusive/ckanext-ssbRetriever",
    license="",
    namespace_packages=['ckanext', 'ckanext.ssbRetriever'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[],
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords="CKAN",
    include_package_data = True,
    entry_points=\
    '''
    [ckan.plugins]
    ssbRetriever=ckanext.ssbRetriever.plugin:ssbRetriever
    ''',
    )
