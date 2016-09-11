#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckan.controllers.package import PackageController


class ssbRetriever(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)

    #the files from these directories will overload their counterparts in the ckan folder
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_resource('templates/js', 'js')

    def before_map(self, map):
	#These are routes that link to actions in the controller
        map.connect('/dataset/new',controller='ckanext.ssbRetriever.controllers.controller:SSBController', action='new_resource_ssb')
        map.connect('/dataset/new', controller='ckanext.ssbRetriever.controllers.controller:SSBController', action='new_resource_ssb')
        return map

    def after_map(self, map):
        return map
