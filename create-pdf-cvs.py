from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image

import csv


data_file = 'data.csv'

def import_data(data_file):
	attendee_data = csv.reader(open(data_file,"rb"))
	for row in attendee_data:
		last_name = row[0]
		first_name =  row[1]
		case_number = row[2]
		pdf_file_name = case_number + '_' + last_name + first_name + '.pdf'
		generate_certificate(first_name, last_name, case_number, pdf_file_name)

def generate_certificate(first_name, last_name, case_number, pdf_file_name):
	attendee_name = first_name + ' ' + last_name
	c = canvas.Canvas(pdf_file_name, pagesize=landscape(letter))

	#header text
	c.setFont('Helvetica', 30, leading=None)
	c.drawCentredString(415,500, "Doctor: "+first_name)
	c.setFont('Helvetica', 30, leading=None)
	c.drawCentredString(415,450,"Patient: "+last_name)
	infoLab = 'InfoLab.png'
	c.drawImage(infoLab, 350, 50, width=None, height=None)
	c.showPage()
	c.save()

import_data(data_file)