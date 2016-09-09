import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class ssbRetriever(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
		implements(IRoutes, inherit=True)

 	def before_map(self, map):
		map.connect('/SSB/new',
        controller='ckanext.ckanext-ssbRetriever.controllers.controller:SSBController',
		action='new_resource')
		return map

	def after_map(self, map):
		return map
