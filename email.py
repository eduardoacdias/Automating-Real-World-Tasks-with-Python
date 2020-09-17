#! /usr/bin/env python3

import datetime
import os

from run import catalog_data
from reports import generate_report
from emails import generate_email, send_email


def pdf_body(input_for,desc_dir):
	"""Generating a summary with two lines, which gives the output name and weight"""
	res = []
	wt = []
	for item in os.listdir(desc_dir):
	  filename=os.path.join(desc_dir,item)
	  with open(filename) as f:
	  	line=f.readlines()
	  	weight=line[1].strip('\n')
	  	name=line[0].strip('\n')
	  	print(name,weight)
	  	res.append('name: ' +name)
	  	wt.append('weight: ' +weight)
	  	print(res)
	  	print(wt)
	new_obj = ""  # initializing the object
	# Calling values from two lists one by one.
	for i in range(len(res)):
		if res[i] and input_for == 'pdf':
			new_obj += res[i] + '<br />' + wt[i] + '<br />' + '<br />'
	return new_obj

if __name__ == "__main__":
	user = os.getenv('USER')
	description_directory = '/home/{}/supplier-data/descriptions/'.format(user)  # The dir...
	current_date = datetime.date.today().strftime("%B %d, %Y")  # Creating data in format...
	title = 'Processed Update on ' + str(current_date)  # Title for the PDF file with the...
	generate_report('/tmp/processed.pdf', title, pdf_body('pdf',description_directory))
	email_subject = 'Upload Completed - Online Fruit Store'  # subject line give in assig...
	email_body = 'All fruits are uploaded to our website successfully. A detailed list is...'
	msg = generate_email("automation@example.com", "<username>@example.com".format(user),...)
						 email_subject, email_body, "/tmp/processed.pdf")  # structuring...
	send_email(msg)
