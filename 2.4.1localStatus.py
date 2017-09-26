#encoding:utf-8
def make_withdraw(balance):
	"""return a withdraw function draws down balance with each call."""
	def widthdraw(amount):
		nonlocal balance
		if amount > balance:
			return 'not enough'
		balance = balance - amount
		return balance
	return widthdraw

wd = make_withdraw(20)
print (wd(2),wd(2),wd(4))
