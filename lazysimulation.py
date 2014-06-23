#!/usr/bin/python
import sys
import numpy as np
import math
global duration
duration = int(sys.argv[1])
global slots
slots = int(sys.argv[2])
global B
B = int(sys.argv[3])
def minslope(i,energy):
	minx = i+1
	min = float(energy[i])/duration
	for x in range(i,slots):
		slope = float(sum(energy[j] for j in range(i,x+1)))/((x-i+1)*duration)
		if slope<min:
			min = slope
			minx = x+1
	return [min,minx]
def offline(energy):
	i=0
	throughput=0
	while(42):
		temp=i
		res = minslope(i,energy)
		p = res[0]
		i = res[1]
		throughput = throughput + (i-temp)*duration*math.log(p + 1)
		if(i == slots):
			break
	return throughput

def online(energy):
	throughput = 0
	spent = 0
	for i in range(0,slots):
		power = min(float(sum(energy[j] for j in range(0,i+1)) - spent), B)/((slots-i)*duration)
		throughput = throughput + duration*math.log(1+power)
		spent = spent + power*duration
	return throughput

off=0
on=0
for x in range (0,100):
	energy = np.random.uniform(0,B,slots)
	off+= offline(energy)
	on+= online(energy)
print float(off)/on