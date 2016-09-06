import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

def test():
	return "hello world"

def show_query_form():
	value = True
	value = toolkit.asbool(value)
	return value

class ssbRetriever(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    def extract_template_name_from_request(self):
 	return self.request.path_info[9:]

    def post(self):
	template_name = self.extract_template_name_from_request()

	self.response.write(template.render(test="hello world"))

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')

    def get_helpers(self):
	return {'ssbRetriever_test':test,
	'ssbRetriever_show_query': show_query_form,
	}
