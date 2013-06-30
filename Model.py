import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

#TODO: SET RELATIONS BETWEEN TABLES

# Boom Boom

'''Creating the Base class, tables will allways inhirit this base class'''
Base = declarative_base()

'''Datatypes used in this model'''
from sqlalchemy import Column, Integer, String, Text, Date, Boolean


'''Defining our Tables/Classes'''
class Continent(Base):
	'''This class defines the continents of earth, it was made to make it possible
	for users to search universities by continent'''
	__tablename__ = "continents"

	id = Column( Integer, primary_key=True )
	name = Column(String(20))

	def __init__(self, id, name):
		self.id = id
		self.name = name

	def __repr__(self):
		return "<Continent({0})>".format(self.name)

class Country(Base):
	''' A class that defines countries accross the world
	It takes the following code, name, market, living_costs_per_month'''

	__tablename__ = 'country'
	
	id = Column(Integer, primary_key= True)
	code = Column(String(2)) #Country code like us, uk, fr ...
	name = Column(String(50))
	market = Column(Integer(2)) #Give the market there a number between 1 and 10
	living_costs_per_month = Column(Integer(5)) #Probably won't be accurate but it would be useful

	def __init__(self, code, name, market, living_costs_per_month):
		self. code = code
		self.name = name
		self.market = market
		self.living_costs_per_month = living_costs_per_month
	def __repr__(self):
		return "<Counrty({0} {1} {2} {3})>".format(self.code, self.name,self.market,self.living_costs_per_month)


class University(Base):
	'''A class defines universities.
	It takes the following: '''
	__tablename__ = 'university'

	id = Column(Integer, primary_key=True)
	global_rank = Column(Integer(5))
	local_rank = Column(Integer(4))
	city = Column(String(50)) #University City of location
	address = Column(String(80))
	student_support = Column(Text)
	housing = Column(Boolean) #Does the university provide housing or not
	adminstration_contact = Column(String(512))
	website = Column(String(512))

	def __init__(self, global_rank, local_rank, city, address, student_support,housing,
		adminstration_contact, website):
		self.global_rank= global_rank
		self.local_rank= local_rank
		self.city = city
		self.student_support = student_support
		self.housing = housing
		self.adminstration_contact = adminstration_contact
		self.website = website

	def __repr__(self):
		return "<University({0} {1} {2} {3} {4} {5} {6})>".format(self.global_rank, self.local_rank, self.city,
			self.student_support,self.housing,self.adminstration_contact, self.website)

class Faculty(Base):
	'''Faculties accross the universities'''
	__tablename__ = 'faculty'
	id = Column(Integer, primary_key=True)
	name = Column(String(30))
	school = Column(String(30))
	requirements = Column(Text)
	website = Column(String(512))

	def __init__(self, name, school,requirements, website):
		self.name = name
		self.school = school
		self.requirements = requirements
		self.website = website

	def __repr__(self):
		return "<Faculty({0} {1} {2} {3})>".format(self.name, self.school,
			self.requirementsself.website)

class Sections(Base):
	'''Sections in every faculty, Majors?'''

	__tablename__ = 'sections'

	id = Column(Integer, primary_key=True)
	name = Column(String(50))
	requirements = Column(Text)
	test_scores = Column(String(512)) #Some sections reqire specifi test scores you already got

	def __init__(self, name, requirements, test_scores):
		self.name = name
		self.requirements = requirements
		self.test_scores = test_scores

	def __repr__(self):
		return "<Section({0} {1} {2})>".format(self.name, self.requirements,
			self.test_scores)

class Programs(Base):
	'''Degree programs offered by University-> Faculty -> Section'''

	__tablename__ = 'programs'

	id = Column(Integer, primary_key=True)
	name = Column(String(50)) #Degree name
	language = Column(String(50)) #Degree program offered in what language
	level = Column(String(50)) #Degree level
	duration = Column(Integer(2)) #Degree duration in years or semesters
	start_date = Column(Date) #Program start date
	application_start_date = Column(Date) #When to apply
	application_deadline = Column(Date) #Application deadline!

	def __init__(self, name, language, level, duration, start_date,
		application_start_date, application_deadline):

		self.name = name
		self.language = language
		self.level = level
		self.duration = duration
		self.start_date = start_date
		self. application_start_date = application_start_date
		self.application_deadline = application_deadline

	def __repr__(self):
		return "<Program({0} {1} {2} {3} {4} {5} {6}".format(self.name, self.language,
			self.level,self.duration, self.start_date, self.application_start_date,
			self.application_deadline)

class Professors(Base):
	''' Professors in every program < faculty'''

	__tablename__= 'professors'

	id = Column(Integer, primary_key=True)
	name = Column(String(512))
	field_of_interest = Column(String(512))
	research_field = Column(String(1024))

	def __init__(self, name, field_of_interest, research_field):
		self.name = name
		self.field_of_interest = field_of_interest
		self.research_field = research_field

	def __repr__(self):
		return "<Professors({0} {1} {2})>".format(self.name,
			self.field_of_interest,self.research_field)

class Fees(Base):
	'''This class has a 1-Fees-To-Many-Programs relation. only'''
	__tablename__ = 'fees'

	id = Column(Integer, primary_key=True)

	currency = Column(String(3)) #Currency sign USD/EUR...
	amount = Column(Integer)

	def __init__(self, currency, amount):
		self.currency = currency
		self.amount = amount
	def __repr__(self):
		return "<Fees({0} {1})>".format(self.currency, self.amount)

class Contact(Base):
	'''Contact information for every professor'''
	__tablename__ = 'contact'

	id = Column(Integer, primary_key=True)

	email = Column(String(50))
	telephone = Column(Integer)
	mail = Column(String(512))

	def __init__(self, email, telephone, mail):
		self.email = email
		self.telephone = telephone
		self.mail = mail

	def __repr__(self):
		return "<Contact( {0} {1} {2} )".format(self.email,self.telephone,self.mail)		