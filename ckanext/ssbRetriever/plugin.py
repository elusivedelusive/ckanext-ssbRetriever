import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class ssbRetriever:
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config_):
                toolkit.add_template_directory(config_, 'templates')
