#encoding:utf-8
#高阶函数,将函数作为参数值传递
def summation(n,term,next):
	total,k = 0,1
	while k <= n:
		total , k = total + term(k) , next(k)
	return total

def identify(k):
	return k
#返回n的3次方
def cube(n):
	return pow(n,3)

def successor(k):
	return k + 1

#求自然数的和:1,2,3,4,5
def sum_naturals(n):
	return summation(n,identify,successor)
#求立方的和:1 + 2^3 + 3^3 + 4^3......
def sum_cubes(n):
	return summation(n,cube,successor)

print sum_naturals(3)
print sum_cubes(3)

for x in xrange(1,10):
	pass