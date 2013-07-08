''' This module should provide a clean way to create the Database engine, add/Update/Delete records in the Model.py'''
import sqlalchemy
import Model

def version():
	'''For debugging info'''
	print "SQLAlchemy version: ", sqlalchemy.__version__