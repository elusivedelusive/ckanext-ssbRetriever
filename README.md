# ckanext-ssbRetriever

Installation
------------

To install, activate your CKAN virtualenv and then do:

    navigate to "/usr/lib/ckan/default/src/ckan/ckanext"
    git clone 'https://github.com/elusivedelusive/ssbRetriever.git'
    cd ssbRetriever
    open the config.py file and add your authorization key and the string of you root site ul
    python setup.py develop

Then
    navigate to your root ckan folder (/usr/lib/ckan/default/src/ckan)
    open setup.py and add 'ssbRetriever = ckanext.ssbRetriever.plugin:ssbRetriever' under ckan.plugins

Then add 'ssbRetriever' to the ckan.plugins line in your CKAN config file, for
example:

    ckan.plugins = resource_proxy stats datastore ssbRetriever

Lastly, restart your web server.
