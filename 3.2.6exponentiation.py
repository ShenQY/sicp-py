#encoding:utf-8
"""two ways confirm exponentiation,(递归求幂,加个square乘法，可以优化很多计算次数)"""
def square(x):
	return x * x

count = 0
def fast_exp(b,n):
	global count 
	count = count + 1
	if n == 0:
		return 1
	elif n % 2 == 0:
		return square(fast_exp(b,n//2))
	else:
		return b*fast_exp(b,n-1)

scount = 0
def form_exp(b,n):
	global scount
	scount = scount + 1
	if n==0:
		return 1
	else:
		return b * form_exp(b,n-1)

print(fast_exp(2,100))

print(form_exp(2,100))

print(count,scount)


