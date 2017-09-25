#encoding:utf-8
from doctest import run_docstring_examples
def fib(n):
	"""Reture the sum of the first

    >>> fib(2)
    1
    >>> fib(3)
    1
    >>> fib(44)
    433494437
	"""
	pred,curr = 0,1
	k = 2
	while k < n:
		pred,curr = curr,pred + curr
		k = k + 1
	return curr
assert fib(8) == 13#直接的断言方式
#方法的单元测试
def fib_test():
	assert fib(8) == 13
	assert fib(2) == 1
	assert fib(3) == 1
	assert fib(50) == 7778742049
fib_test()#调用单元测试
run_docstring_examples(fib,globals())#运行fib()方法中的“”“”“”中的断言
