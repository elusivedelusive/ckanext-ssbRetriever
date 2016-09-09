# encoding: utf-8

import logging
from urllib import urlencode
import datetime
import mimetypes
import cgi

from ckan.common import config
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

from ckan.common import OrderedDict, _, json, request, c, g, response
from home import CACHE_PARAMETERS

log = logging.getLogger(__name__)
from ckan.controllers.package import PackageController

class SSBController(PackageController):

    def new_resource(self, id):
        # using default functionality
        template = self.read(id)

        #check if metadada info exists and add it otherwise
        context = {'model': model, 'session': model.Session, 'user': c.user or c.author}
        package_info = get_action('package_show')(context, {'id': c.pkg.id})


        c.resultformats = RESULT_FORMATS
        c.selectedformat = 'html'

        if 'runquery' in request.params:
            query_results, content_type, errors, error_message = execute_query(request.params['query'], request.params['resultformat'], self.packageendpoint, request.url.replace('/sparql', ''))
            c.query = request.params['query']
            c.selectedformat = request.params['resultformat']

            if errors:
                c.error_message = error_message
            else:
                if content_type:
                    response.headers['Content-type'] = content_type
                    return query_results
                else:
                    c.queryresults = query_results

        return render('package/resources.html')
