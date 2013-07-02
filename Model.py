import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

#TODO: SET RELATIONS BETWEEN TABLES

# Boom Boom

'''Creating the Base class, tables will allways inherit this base class'''
Base = declarative_base()

'''Datatypes used in this model'''
from sqlalchemy import Column, Integer, String, Text, Date, Boolean

''' Relationship primatives needed'''
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

'''Every class defines a table in SQL'''
class Continent(Base):
	'''Continent(Name)
	country is a FK'''
	__tablename__ = "continents"

	id = Column( Integer, primary_key=True )
	name = Column(String(20))
	country = relationship("Country") #Continent -> Country One-to-many relation
	'''note: A relationship function takes the Class name "The capital first letter one"
	unlike the foreignkey function which takes the __tablename__ value 
	"the small first letter one" '''

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return "<Continent( {0} )>".format(self.name)

class Country(Base):
	'''takes Country(Name)
	universities / country_metadata is a FK'''

	__tablename__ = 'country'
	
	id = Column(Integer, primary_key= True)
	name = Column(String(50)) #Country name
	continent_id = Column(Integer, ForeignKey('continents.id')) #Continent -> Country One-to-many relation
	universities = relationship("University")
	country_metadata = relationship('CountryMetadata')

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return "<Counrty( {0} )>".format(self.name)

class CountryMetadata(Base):
	'''CountryMetadata(Code, Market,LivinCostsPerMonth)
	country_id is a FK'''
	__tablename__ = 'countryMetadata'

	id = Column(Integer, primary_key=True)
	code = Column(String(2)) #Country Code like fr, uk, us..
	market = Column(Integer)
	living_costs_per_month = Column(Integer) #In USD
	country_id = Column(Integer, ForeignKey('country.id'))

	def __init__(self, code, market, living_costs_per_month):
		self.code = code
		self.market = market
		self.living_costs_per_month = living_costs_per_month
	def __repr__(self):
		return "<CountryMetadata( {0} {1} {2} )>".format(self.code,self.market,self.living_costs_per_month)


class University(Base):
	'''University(Name, City,Address,Website)
	faculties is a FK'''
	__tablename__ = 'university'

	id = Column(Integer, primary_key=True)
	name = Column(String(100))
	city = Column(String(50)) #University City of location
	address = Column(String(80))
	website = Column(String(512))
	country_id = Column(Integer, ForeignKey('country.id')) #The foreignkey of countries in University table
	faculties = relationship('Faculty')
	advgs = relationship('Advantages')


	def __init__(self, name, city, address, student_support, adminstration_contact, website):
		self.name = name
		self.city = city
		self.student_support = student_support
		self.adminstration_contact = adminstration_contact
		self.website = website

	def __repr__(self):
		return "<University( {0} {1} {2} {3} )>".format(self.name, self.city, self.address, self.website)

class Advantages(Base):
	'''Advantages(GlobalRank, LocalRank,Housing,StudentSupport)
	university_id is a FK'''

	__tablename__ = 'advantage'

	id = Column(Integer, primary_key=True)
	global_rank = Column(Integer)
	local_rank = Column(Integer)
	housing = Column(Boolean)
	student_support = Column(Text)
	university_id = Column(Integer, ForeignKey('university.id'))

	def __init__(self, global_rank, local_rank, housing, student_support):
		self.global_rank = global_rank
		self.local_rank = local_rank
		self.housing = housing
		self.student_support = student_support
	def __repr__(self):
		return "<Advantages( {0} {1} {2} )>".format(self.global_rank, self.local_rank, self.housing)

class Faculty(Base):
	'''Faculty(Name,School,Requirements,Website)
	sections is a FK '''
	__tablename__ = 'faculty'
	id = Column(Integer, primary_key=True)
	name = Column(String(30))
	school = Column(String(30))
	requirements = Column(Text)
	website = Column(String(512))
	university_id = Column(Integer, ForeignKey('university.id'))
	sections = relationship('Sections')

	def __init__(self, name, school,requirements, website):
		self.name = name
		self.school = school
		self.requirements = requirements
		self.website = website

	def __repr__(self):
		return "<Faculty( {0} {1} {2} {3} )>".format(self.name, self.school,
			self.requirementsself.website)

class Sections(Base):
	'''Sections(Name,Requirements,TestScores)
	programs is a FK'''

	__tablename__ = 'sections'

	id = Column(Integer, primary_key=True)
	name = Column(String(50))
	requirements = Column(Text)
	test_scores = Column(String(512)) #Some sections reqire specifi test scores you already got
	faculty_id = Column(Integer, ForeignKey('faculty.id'))
	programs = relationship('Programs')

	def __init__(self, name, requirements, test_scores):
		self.name = name
		self.requirements = requirements
		self.test_scores = test_scores

	def __repr__(self):
		return "<Section( {0} {1} {2} )>".format(self.name, self.requirements,
			self.test_scores)

class Programs(Base):
	'''Programs(Name,Language,Level, Duration, StartDate, ApplicationStartDate,ApplicationDeadline)
	fees / professors is a FK'''

	__tablename__ = 'programs'

	id = Column(Integer, primary_key=True)
	name = Column(String(50)) #Degree name
	language = Column(String(50)) #Degree program offered in what language
	level = Column(String(50)) #Degree level
	duration = Column(Integer(2)) #Degree duration in years or semesters
	start_date = Column(Date) #Program start date
	application_start_date = Column(Date) #When to apply
	application_deadline = Column(Date) #Application deadline!
	section_id = Column(Integer, ForeignKey('sections.id'))
	professors = relationship('Professors')
	fees = relationship('Fees', uselist=False, backref='programs') #One-To-one Relation with fees


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
		return "<Program( {0} {1} {2} {3} {4} {5} {6} )>".format(self.name, self.language,
			self.level,self.duration, self.start_date, self.application_start_date,
			self.application_deadline)

class Professors(Base):
	''' Professors(Name,ResearchField)
	contact is a FK'''

	__tablename__= 'professors'

	id = Column(Integer, primary_key=True)
	name = Column(String(512))
	research_field = Column(String(1024))
	section_id = Column(Integer, ForeignKey('programs.id'))
	contact = relationship('Contact')

	def __init__(self, name, field_of_interest, research_field):
		self.name = name
		self.research_field = research_field

	def __repr__(self):
		return "<Professors( {0} {1} {2} )>".format(self.name,
			self.field_of_interest,self.research_field)

class Fees(Base):
	'''Fees(Currency,Amount)
	program_id is a FK'''
	__tablename__ = 'fees'

	id = Column(Integer, primary_key=True)

	currency = Column(String(3)) #Currency sign USD/EUR...
	amount = Column(Integer)
	program_id = Column(Integer, ForeignKey('programs.id'))

	def __init__(self, currency, amount):
		self.currency = currency
		self.amount = amount
	def __repr__(self):
		return "<Fees( {0} {1} )>".format(self.currency, self.amount)

class Contact(Base):
	'''Contact(Email,Telephone, Mail)
	profes is a FK'''
	__tablename__ = 'contact'

	id = Column(Integer, primary_key=True)

	email = Column(String(50))
	telephone = Column(Integer)
	mail = Column(String(512))
	professor_id = Column(Integer, ForeignKey('professors.id'))

	def __init__(self, email, telephone, mail):
		self.email = email
		self.telephone = telephone
		self.mail = mail

	def __repr__(self):
		return "<Contact( {0} {1} {2} )>".format(self.email,self.telephone,self.mail)		