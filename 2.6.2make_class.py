#encoding:utf-8
#can run directly

def make_instance(cls):
	"""Return a new object instance,which is a dispatch dictionary"""
	def get_value(name):
		if name in attributes:
			return attributes[name]
		else:
			value = cls['get'](name)
			return bind_method(value,instance)
	def set_value(name,value):
		attributes[name] = value
	attributes = {}
	instance = {'get':get_value,'set':set_value}
	return instance

def bind_method(value,instance):
	"""Return a bound method if value is callable,or other value"""
	if callable(value):
		def method(*args):
			return value(instance,*args)
		return method
	else:
		return value


def make_class(attributes,base_class = None):
	"""Return a new class ,which is a dispatch dictionary"""
	def get_value(name):
		if name in attributes:
			return attributes[name]
		elif base_class is not None:
			return base_class['get'](name)
	def set_value(name,value):
		attributes[name] = value
	def new(*args):
		return init_instace(cls,*args)
	cls = {'get':get_value,'set_value':set_value,'new':new}
	return cls

def init_instace(cls,*args):
	"""Return a new obje                    ct with type cls,initialized with args"""
	instace = make_instance(cls)
	init = cls['get']('__init__')
	if init:
		init(instace,*args)
	return instace



def make_account_class():
	"""Return the Account class,which has deposit and withdraw method."""
	def __init__(self,account_holder,accB):
		self['set']('holder',account_holder)
		self['set']('balance',0)
	def deposit(self,amount):
		"""Increase the account balance by amount and withdraw methods."""
		new_balance = self['get']('balance') + amount
		self['set']('balance',new_balance)
		return self['get']('balance')
	def withdraw(self,amount):
		balance = self['get']('balance')
		if amount > balance:
			return 'not enough'
		self['set']('balance',balance - amount)
		return self['get']('balance')
	return make_class({'__init__':__init__,
					   'deposit':deposit,
					   'withdraw':withdraw,
					   'interest':0.02})
Account = make_account_class()
# print (Account)
jim_acct = Account['new']('2','3')
print (jim_acct['get']('holder'))
print (jim_acct['get']('interest'))
print (jim_acct['get']('deposit')(20))
print (jim_acct['get']('withdraw')(5))
jim_acct['set']('interest',0.04)
print (jim_acct['get']('interest'))

print (jim_acct['get']('deposit'))
	# print(type(*args))


