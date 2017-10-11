#encoding:utf-8
def inform_all_execpt(source,message,constraints):
	"""Inform all constraints of the message,except source."""
	for c in constraints:
		if c != source:
			c[message]()

def make_connector(name=None):
	"""A connector between constraints."""
	informant = None
	constraints = []
	def set_value(source,value):
		nonlocal informant
		val = connector['val']
		if val is None:
			informant,connector['val'] = source,value
			if name is not None:
				print(name , '=', value)
			inform_all_execpt(source,'new_val',constraints)
		else:
			if val != value:
				print('Contradiction detected:',val,'vs',value)
	def forget_value(source):
		nonlocal informant
		if informant == source:
			informant, connector['val'] = None,None
			if name is not None:
				print(name,'is forgotten')
			inform_all_execpt(source,'forget',constraints)
	connector = {'val':None,
				 'set_val':set_value,
				 'forget':forget_value,
				 'has_val':lambda:connector['val'] is not None,
				 'connect':lambda source:constraints.append(source)}
	return connector
def constant(connector,value):
	"""The constraint that connector = value"""
	constraint = {}
	connector['set_val'](constraint,value)
	return constraint
