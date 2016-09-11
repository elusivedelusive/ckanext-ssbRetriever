# ckanext-ssbRetriever

Installation
------------

To install, activate your CKAN virtualenv and then do:

    navigate to "/usr/lib/ckan/default/src/ckan/ckanext"
    git clone 'https://github.com/elusivedelusive/ssbRetriever.git'
    cd ssbRetriever
    python setup.py develop

Then add 'ssbRetriever = ckanext.ssbRetriever.plugin:ssbRetriever' under ckan.plugins in the setup.py file in you root ckan folder (/usr/lib/ckan/default/src/ckan)

Then add 'ssbRetriever' to the ckan.plugins line in your CKAN config file, for
example:

    ckan.plugins = resource_proxy stats datastore ssbRetriever

Lastly, restart your web server.
