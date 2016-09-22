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

#Takes a csv string and calls truncateAndNumerateColumnHeaders to truncate and numerate long headers
def fixCSV(csvIn):
	rownum = 0
	headers = ""
	newHeaders = []
	newRow = []


	csvfile = io.BytesIO(csvIn)

	r = csv.reader(csvfile)

	out = io.BytesIO()
	writer = csv.writer(out)

	for row in r:
		if(rownum==0):
			newHeaders = truncateAndNumerateColumnHeaders(row)
			#this is where the magic happens
			newHeaders = [nh.encode('utf-8') for nh in newHeaders]
			#print 'NH', newHeaders
			writer.writerow(newHeaders)
		else:
			newRow.append(row)
		rownum += 1


	writer.writerows(newRow)
	#print "THIS IS UTILS =        " + out.getvalue()

	return out.getvalue()

#truncates column headers over 55 characters and numerates them with a counter in the beginning of the name
def truncateAndNumerateColumnHeaders (headers):
	newHeaders = []
	headernum = 0;
	for header in headers:
		if(len(header) > 55):
			header = header[0:55]
		#magic
		nh = header.decode('utf-8')
		temp = u'{} {}'.format(headernum, nh)
		newHeaders.append(temp)
		headernum += 1
	return newHeaders

test = '''"region","Har innfÃ¸rt eiendomsskatt, Ja=1 Nei=0 2001","Har innfÃ¸rt eiendomsskatt, Ja=1 Nei=0 2002","Har innfÃ¸rt eiendomsskatt, Ja=1 Nei=0 2003","Har eiendomsskatt i hele kommunen, Ja=1 Nei=0 2001","Har eiendomsskatt i hele kommunen, Ja=1 Nei=0 2002","Har eiendomsskatt i hele kommunen, Ja=1 Nei=0 2003","Har eindomsskatt i hele kommunen, unntatt verker og bruk og annen nÃ¦ringseiendom, Ja=1 Nei=0 2001","Har eindomsskatt i hele kommunen, unntatt verker og bruk og annen nÃ¦ringseiendom, Ja=1 Nei=0 2002","Har eindomsskatt i hele kommunen, unntatt verker og bruk og annen nÃ¦ringseiendom, Ja=1 Nei=0 2003"
"EAK Landet",.,..,..,.,..,..,.,..,..
"EAKUO Landet uten Oslo",.,..,..,.,..,..,.,..,..
"0101 Halden",..,..,..,..,..,..,..,..,..'''
#print(fixCSV(test))
