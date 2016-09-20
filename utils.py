#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import csv
import io

#performs a simple post request using the python requests library
#url = url to an endpoint that accepts post requests
#data = request body. In the case of querying SSB it contains a json query
def execute_simple_post_query(url, query):
	return requests.post(url, data = query)

#performs a multipart/form request using the python requests library
#url = url to an endpoint that accepts post requests
#files = one or several files to be uploaded
#headers = requests headers
#data = various parameters that the endpoint may require
def multipart_post(url, files, headers, params):
	return requests.post(url, files = files, headers = headers, data = params)

#use
def fixCSV(csvIn):
	rownum = 0
	headers = ""
	newHeaders = []
	out = io.StringIO()
	writer = csv.writer(out)
	csvfile = StringIO(csvIn)

	dialect = csv.Sniffer().sniff(csvfile.read(1024))
	csvfile.seek(0)
	r = csv.reader(csvfile, dialect)
	for row in r:
		if(rownum==0):
			newHeaders = truncateAndNumerateLongColumnHeaders(row)
			writer.writerow(newHeaders)
		else:
			writer.writerow(row)
		rownum += 1
	return out.getvalue()

#
def truncateAndNumerateLongColumnHeaders (headers):
	newHeaders = []
	headernum = 0;
	for header in headers:
		if(len(header) > 60):
			header = header[0:60]
		temp = str(headernum)+ " " + header
		newHeaders.append(temp)
		headernum += 1
	return newHeaders

#print(fixCSV("StatBank.csv"))
