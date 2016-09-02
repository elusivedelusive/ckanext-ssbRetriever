from setuptools import setup, find_packages

version = "0.1"

setup(
    name="ckanext-ssbRetriever",
    version="0.1",

    description="Grafisk brukergrensesnitt for å kjore POST queries mot SSB utviklet for Stavanger Kommune",
    long_description='''Contributors:
    Jonatan Hoff <jonatan.hoff@gmail.com>''',
    url="https://github.com/elusivedelusive/ckanext-ssbRetriever",
    license="",
    keywords="CKAN",
    include_package_data = True,
    entry_points='''
        [ckan.plugins]
        ssbRetriever=ckanext.ssbRetriever.plugin:ssbRetriever
    ''',
    )
