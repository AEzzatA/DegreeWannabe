import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

#TODO change string format in __repr__ to proper ones other than %s or the new format function

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
	name = Coulmn(String(50))
	market = Column(Integer(2)) #Give the market there a number between 1 and 10
	living_costs_per_month = Column(Integer(5)) #Probably won't be accurate but it would be useful

	def __init__(self, code, name, market, living_costs_per_month):
		self. code = code
		self.name = name
		self.market = market
		self.living_costs_per_month = living_costs_per_month
	def __repr__(self):
		return "<Counrty({0} {1} {2} {3})>" % (self.code, self.name,self.market,self.living_costs_per_month)


class University(Base):
	'''A class defines universities.
	It takes the following: '''
	__tablename__ = 'university'

	id = Column(Integer, primary_key=True)
	global_rank = Column(Integer(5))
	local_rank = Column(Integer(4))
	city = Column(String(50)) #University City of location
	address = Column(String(80))
	student_support(Text)
	housing = Column(Boolean) #Does the university provide housing or not
	adminstration_contact = Column(String(512))
	website = Column(String(512))

	def __init__(self, global_rank=None, local_rank=None, city, address = "", student_support="",housing =False,
		adminstration_contact="", website):
		self.global_rank= global_rank
		self.local_rank= local_rank
		self.city = city
		self.student_support = student_support
		self.housing = housing
		self.adminstration_contact = adminstration_contact
		self.website = website

	def __repr__(self):
		return "<University({0} {1} {2} {3} {4} {5} {6})>" % (self.global_rank, self.local_rank, self.city,
			self.student_support,self.housing,self.adminstration_contact, self.website)
