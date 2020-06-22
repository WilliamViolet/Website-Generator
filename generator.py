# Overview Description: This code will take an existing HTML template and have a user interface that
#                       Allows the user to enter his/her own information to generate their website
#                       From the template
# 
# Functions: This program as it stands has limited functionality
#            Can only edit existing templates
#	         Strict formatting based on predifined CSS
#
# Start: No gui to start. Get backend working first then create
#        The user interface for the program
# 
#
import sys
from PyQt5.QtWidgets import *

def start():
	file_object = open("templates/resume.html","r")
	file_data = file_object.read()
	return file_data

def get_info():
	title = ""
	name = ""
	aboutMeInformation = ""
	interestingClasses = ""
	skill_names = ""
	work_experience_names = ""
	project_names = ""
	contact_types = ""

	print("Any list of things we ask for, please comma separate the string input")
	title = input("Enter the title of your webpage(Ex. Name's Resume Site): ")
	# name = input("Enter your name: ")
	# aboutMeInformation = input("Enter a short paragraph about you: ")
	# interestingClasses = input("input class names relevant to your major(comma separated): ")
	# skill_names = input("Enter a list of skills you have (comma separated)")
	# work_experience_names = input("Enter any internships you may have had (Title of Job - year started, year completed) comma separated:")
	# project_names = input("Enter any projects that you might be working on: ")
	# contact_types = input("Enter a list of types to be contacted at(LinkedIn, Phone, Email):")
	return title, name, aboutMeInformation, interestingClasses, skill_names, work_experience_names, project_names, contact_types

def format_skill():
	pass

def format_classes():
	pass

def format_work():
	pass

def format_proj():
	pass

def format_contact():
	pass

def add_data(template_data, title, name, aboutMeInformation, interestingClasses, skill_names, work_experience_names, project_names, contact_types):
	template_data = template_data.replace("WRITE TITLE HERE", title)
	create_html(template_data)

def create_html(template_data):
	file_object = open("products/resume_product.html","w+")
	file_object.write(template_data)


file_data = start()
title, name, aboutMeInformation, interestingClasses, skill_names, work_experience_names, project_names, contact_types = get_info()

add_data(file_data, title, name, aboutMeInformation, interestingClasses, skill_names, work_experience_names, project_names, contact_types)

