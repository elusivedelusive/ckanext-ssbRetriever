import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import requests

def query_form():
    return "the end is coming"

class ssbRetriever(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(p.ITemplateHelpers)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')

    def get_helpers(self):
        return {'ssbRetriever_query_form': query_form}

    def package_form(self):
        return 'package/new_package_form.html'

    def new_template(self):
        return 'package/new.html'

    def comments_template(self):
        return 'package/comments.html'

    def search_template(self):
        return 'package/search.html'

    def read_template(self):
        return 'package/read.html'

    def history_template(self):
        return 'package/history.html'

    def package_types(self):
        return ['dataset']

    def is_fallback(self):
        return True

    def setup_template_variables(self, context, data_dict=None, package_type=None):
        from ckan.lib.base import c
        from ckan import model
        c.licences = model.Package.get_license_options()
