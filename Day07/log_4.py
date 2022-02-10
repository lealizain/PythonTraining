
import logging

logging.basicConfig(filename='test.log', level = logging.INFO)

def add(x, y):
	return x + y 


def sub (x, y):
	return x - y



print(add(2,2))