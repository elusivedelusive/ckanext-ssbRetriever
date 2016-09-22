#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import ckan.lib.base as base
import ckanext.ssbRetriever.config as plugin_settings
import ckan.lib.helpers as h
from ckan.common import request, response, _
from ckan.controllers.package import PackageController
from ckanext.ssbRetriever.utils import execute_simple_post_query, multipart_post, fixCSV

log = logging.getLogger(__name__)

render = base.render
abort = base.abort
redirect = base.redirect

class SSBController(PackageController):
    def new_ssb(self):
	return render('package/snippets/resource_form.html')
    def new_resource_ssb(self):

	#log.warning("================CONTROLLER=====================")
	#unpack variables from the request object
	packageID = request.params.get('id')
	queryUrl = request.params.get('query-url')
	queryText = request.params.get('query-text')
	resourceID = request.params.get('resourceid')
	name = request.params.get('name')
	description = request.params.get('description')
        inputFormat = request.params.get('inputFormat')
	#query ssb using the input query text and url
	try:
	    ssbResponse = execute_simple_post_query(queryUrl, queryText)
	except:
	    abort(404, _('Invalid query'))

	truncate = request.params.get('Truncate long columns')
	temp = ssbResponse.text

        if inputFormat == "csv":
            if truncate:
    		#set the upload parameter to be the responsetext. This uploads data from the memory as if it was a file
    		#log.warning( ssbResponse.text)
    		#needs encode
    	        temp = fixCSV(ssbResponse.text.encode('utf-8'))
    		#log.warning("================CONTROLLER=====================")
    		#log.warning(temp)
            filesRequests ={'upload': ('ssbData.csv',temp)}
        else:
            filesRequests ={'upload': ('ssbData.json',temp)}

	#retrieve admin user's authorization key from config file
	headers = {"Authorization": plugin_settings.Authorization}

	#retrieve url root from config file
	ckanurl = "http://" + plugin_settings.site_root_url + "/api/action/resource_create"

	#define parameters
	params= {'description': description,'package_id': packageID,'name': name, "url": " "}

	#if we are updating an already existing resource then use its ID as well
	if(resourceID):
		params['id']=resourceID;
	#parameters NB url has to be an empty string to successfully post a file


	#use the multipart_post function to perform a post
	postResponse = multipart_post(ckanurl, filesRequests, headers, params)

	#log.warning("PACKAGEID: " + packageID)
	#log.warning("URL: " + queryUrl)
	#log.warning("QUERY: " + queryText)
	#log.warning("SSBRESPONSE: " + ssbResponse.text)
	#log.warning("POSTRESPONSE: " + postResponse.text)
	#log.warning("================CONTROLLER=====================")

	if(resourceID):
		#redirect user to the resource overview page
        	redirect(h.url_for(controller='package', action='resource_read', id=packageID, resource_id=resourceID))
	else:
		#redirect user to the dataset overview page
        	redirect(h.url_for(controller='package', action='read', id=packageID))
