import random
import math
import os
#import matplotlib.pyplot as plt
#import numpy as np

def activationSigmoid(x):
   return 1 / (1 + math.exp(-x))

def activationLinear(x):
    if x > 0.1:
        return 1
    else:
        return 0

def abs(num):
	if num > 0:
		return num
	else:
		return -num

def error(idealOutput,current):
   return abs(idealOutput - current)

i = 1
k = 0
l = []
w = []
learningRate = 0.05
Out = 0
b1 = 1

n = input("enter count neuor: ")
idealOutput = input("enter ideal output: ")

for i in range(n):
	val = 0
	val = input("enter value of element " + str(i + 1) + ": ")
	l.append(val)

print("inputs: ")

for i in range(n):
	print(str(i + 1) + " = " + str(l[i]))

for i in range(n):
	val = 0
	val = random.random()
	w.append(val)

print("weights: ")

for i in range(n):
	print(str(i + 1) + " = " + str(w[i]))

os.system("pause -n")

while True:
	k = k + 1
	for i in range(n):
		Out = Out + l[i] * w[i]
	Out = Out + b1
	activatedOut = activationLinear(Out)
	delta = error(idealOutput,activatedOut)
	print("iterations: " + str(k))

	if activatedOut != idealOutput and activatedOut == 0:
		for i in range(n):
			if l[i] == 1:
				w[i] = w[i] + learningRate * delta

	if activatedOut != idealOutput and activatedOut == 1:
		for i in range(n):
			if l[i] == 1:
				w[i] = w[i] - learningRate * delta

	if activatedOut == idealOutput:
		print("weights finnaly: ")

		for i in range(n):
			print(str(i + 1) + " = " + str(w[i]))
		break


	#print("out = " + str(activatedOut))
