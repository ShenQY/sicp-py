#encoding:utf-8

def make_dict():
	"""return a fuctional implementation of a dictionary."""
	records = []
	def getitem(key):
		for k,v in records:
			if k == key:
				return v

	def setitem(key,value):
		for k,v in records:
			if k == key:
				v = value
				return
		records.append([key,value])

	def dispatch(message,key=None,value=None):
		if message == 'getitem':
			return getitem(key)
		elif message == 'setitem':
			setitem(key,value)
		elif message == 'keys':
			return tuple(k for k,_ in records)
		elif message == 'values':
			return tuple(v for _,v in records)
	return dispatch

dict = make_dict()
dict('setitem',3,9)
dict('setitem','num',11)
print dict('getitem',3)
print dict('getitem','num')
print dict('keys')
print dict('values')




