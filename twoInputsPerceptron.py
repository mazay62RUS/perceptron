import random
import matplotlib.pyplot as plt
import numpy as np

def activationSigmoid(x):
    return 1 / (1 + np.exp(-x))

def activationLinear(x):
    if x > 0.5:
        return 1
    else:
        return 0

def error(idealOutput,current):
    return np.abs(idealOutput - current)

l1 = input("enter l1: ")
l2 = input("enter l2: ")
b1 = 1
i = 1
w1 = random.random()
w2 = random.random()
x1 = []
y1 = []
x2 = []
y2 = []

idealOutput = input("enter idealOutput: ")
learningRate = 0.000005

while True:
    Out = l1 * w1 + l2 * w2 + b1
    x1.append(i)
    y1.append(w1)
    x2.append(i)
    y2.append(w2)
    activatedOut = activationLinear(Out)
    delta = error(idealOutput,activatedOut)
    print("ideal: " , idealOutput , ". current: " , activatedOut)
    print("w1 = ",w1," w2 = ", w2)
    print(i)
    i = i + 1
    if activatedOut != idealOutput and activatedOut == 0:
        if l1 == 1:
            w1 = w1 + learningRate * delta
        if l2 == 1:
            w2 = w2 + learningRate * delta
    if activatedOut != idealOutput and activatedOut == 1:
        if l1 == 1:
            w1 = w1 - learningRate * delta
        if l2 == 1:
            w2 = w2 - learningRate * delta
    if activatedOut == idealOutput:
        print("finnaly w1 = ",w1," w2 = ", w2)
        break

plt.plot(x1,y1,label="w1")
plt.plot(x2,y2,label="w2")
plt.xlabel("iterations")
plt.ylabel("weights")
plt.title("weights / iterations")
plt.legend()
plt.show()
