"""
Logistic sequences

Usage: python logistic.py
Def: Computes first n terms of logistic difference equation p_{n+1} = k*p_n*(1 - p_n), starting with initial population p_0, where 0 < p_0 < 1
Params: p_n measures the size of the population of the nth generation; k; 

"""
import numpy as np
import matplotlib.pyplot as plt

def main():
	print "This program illustrates the logistic difference equation"
	p = input("Enter a number between 0 and 1: ")
	k = input("Enter a number between 1 and 3: ")
	t = 40 # number of years
	num = np.zeros(t+1)
	num[0] = 1
	for i in range (t):
		p = k * p * (1 - p)
		num[i+1] = p
	plt.plot(range(t+1),num, 'b')
	plt.xlabel('Year')
	plt.ylabel('Number')
	plt.title('Population size: ish') 


	plt.show()

if __name__ == '__main__':
	main()