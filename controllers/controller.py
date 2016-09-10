import logging
from urllib import urlencode
import datetime
import mimetypes
import cgi

from pylons import config
from paste.deploy.converters import asbool
import paste.fileapp

import ckan.logic as logic
import ckan.lib.base as base
import ckan.lib.maintain as maintain
import ckan.lib.i18n as i18n
import ckan.lib.navl.dictization_functions as dict_fns
import ckan.lib.helpers as h
import ckan.model as model
import ckan.lib.datapreview as datapreview
import ckan.lib.plugins
import ckan.lib.uploader as uploader
import ckan.plugins as p
import ckan.lib.render
import requests,json

from ckan.common import OrderedDict, _, json, request, c, g, response
from ckan.controllers.package import PackageController
from ckanext.ssbRetriever.utils import execute_simple_post_query, multipart_post

log = logging.getLogger(__name__)

render = base.render
abort = base.abort
redirect = base.redirect

NotFound = logic.NotFound
NotAuthorized = logic.NotAuthorized
ValidationError = logic.ValidationError
check_access = logic.check_access
get_action = logic.get_action
tuplize_dict = logic.tuplize_dict
clean_dict = logic.clean_dict
parse_params = logic.parse_params
flatten_to_string_key = logic.flatten_to_string_key

lookup_package_plugin = ckan.lib.plugins.lookup_package_plugin

log = logging.getLogger(__name__)

class SSBController(PackageController):
    #these are actions
    def new_ssb_form(self):
	packageID = request.params.get('id')



	context = {'model': model, 'session': model.Session,
                       'user': c.user or c.author, 'auth_user_obj': c.userobj}

	pkg_dict = get_action('package_show')(context, {'id': packageID})
        data = clean_dict(dict_fns.unflatten(tuplize_dict(parse_params(request.POST))))
	errors = {}
	error_summary = {}
	template = 'package/new_resource_ssb.html'
	package_type = pkg_dict['type'] or 'dataset'

       	vars = {'data':data, 'errors': errors,
                'error_summary': error_summary, 'action': 'new',
                'resource_form_snippet': self._resource_form(package_type),
                'dataset_type': package_type}

	return render('package/new_resource_ssb.html', extra_vars=vars)

	#redirect(h.url_for(controller='SSBController', action='new_ssb_resource_form', id=packageID))

    def new_resource_ssb(self, data=None, errors=None, error_summary=None):
	#unpack variables from the request object
	packageID = request.params.get('id')
	queryUrl = request.params.get('query-url')
	queryText = request.params.get('query-text')
	name = request.params.get('name')
	description = request.params.get('description')

	#query ssb using the input query text and url
	ssbResponse = execute_simple_post_query(queryUrl, queryText)
	#set the upload parameter to be the responsetext. This uploads data from the memory as if it was a file
	filesRequests ={'upload': ('ssbData.csv', ssbResponse.text)}
	
	#the admin users authorization key
	headers = {"Authorization": "f65b83f5-c14a-4440-b07f-3be58acb686a"}
	
	#the url to the resource_create action api 
	ckanurl = "http://localhost/api/action/resource_create"

	#parameters NB url has to be an empty string to successfully post a file
	params= {'description': description,'package_id': packageID,'name': name, "url": " "}
	
	#use the multipart_post function to perform a post
	postResponse = multipart_post(ckanurl, filesRequests, headers, params)
	#, "id":"74bbb978-323c-4f82-9a27-77f1d2f1b663"

	log.warning("================CONTROLLER=====================")
	log.warmomg("PACKAGEID: " + packageID)
	log.warning("URL: " + queryUrl)
	log.warning("QUERY: " + queryText)
	log.warning("SSBRESPONSE: " + ssbResponse.text)
	log.warning("POSTRESPONSE: " + postResponse.text)
	log.warning("================CONTROLLER=====================")

	#redirect user to the dataset overview page
        redirect(h.url_for(controller='package', action='read', id=packageID))



