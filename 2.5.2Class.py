#encoding:utf-8
#can run directly
class Account(object):
	"""docstring for Account"""
	interest = 0
	def __init__(self,holder):
		super(Account, self).__init__()
		self.balance = 0
		self.holder = holder
	def publicMethod(self):
		print ('public')

class BAccount(Account):
	"""docstring for BAccount"""
	def __init__(self, arg):
		super(BAccount, self).__init__()
		self.arg = arg
class DAccount(BAccount):
	"""docstring for DAccount"""
	def __init__(self, arg):
		super(DAccount, self).__init__()
		self.arg = arg
		
class CAccount(DAccount,BAccount):
	"""docstring for CAccount"""
	def __init__(self, arg):
		super(CAccount, self).__init__()
		self.arg = arg
		
a = Account('jim')
a.publicMethod()

b = Account('mali')
a.interest = 1
print (Account.interest,a.interest,b.interest)
Account.interest = 3
print (Account.interest,a.interest,b.interest)
print ([c.__name__ for c in CAccount.mro()])
