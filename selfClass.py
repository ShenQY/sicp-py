#encoding:utf-8
def make_class(attributes,base_class = None):
	
	def get_value(name):
		if name in attributes:
			return attributes[name]
		elif base_class is not None:
			return base_class['get'](name)
	def set_value(name,value):
		attributes[name] = value
	def new(*args):
		instace = init_instace(cls,*args)
		return instace
	cls = {'get':get_value,'set':set_value,'new':new}
	return cls

def init_instace(cls,*args):
	instace = make_instance(cls)
	init = cls['get']('__init__')
	if init:
		init(instace,*args)
	return instace

def make_instance(cls):
	def get_value(name):
		if name in attrs:
			return attrs[name]
		else:
			value = cls['get'](name)
			return bind_method(instance,value)
	def set_value(name,value):
		attrs[name] = value
	attrs = {}
	instance = {'get':get_value,'set':set_value}
	return instance

def bind_method(instance,value):
	if callable(value):
		def method(*args):
				return value(instance,*args)
		return method
	else:
		return value

def make_cat_class():
	def init(self,hands):
		self['set']('hands',hands)
		print('aaaaa')
	def addHand(self,count):
		sums = self['get']('hands')
		print('sum','++++',sums,count)
		sums = sums + count
		self['set']('hands',sums)
		return self['get']('hands')
	return make_class({'__init__':init,
						'addHand':addHand,
						'orginC':100
						})
	

CAT = make_cat_class()
print(CAT)
cat = CAT['new'](2)

print(cat)
print(cat['get']('hands'))
print(cat['get']('addHand'))
print(cat['get']('addHand')(4))

print(cat['get']('hands'))
print(cat['get']('orginC'))
cat['set']('orginC',20)
print(cat['get']('orginC'))













