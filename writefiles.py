# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:00:47 2020

@author: sandra
"""
#!/usr/bin/python3

import datetime
import time
import subprocess
#i=0
#while i<3:
while True:   #comment this out for debug
	currentDT=datetime.datetime.now()
	starttime=time.time()
	datetime1=(currentDT.strftime("%Y-%m-%d-%H-%M-%S"))
	filename= 'logfile-'+datetime1+'.log'
	coughlog='cough.log'
	f=open(filename,'w+')
	time1=0
	maxloops=100  #change to 3 for debug
	while time1<maxloops:
		subprocess.call('./sopare.py >> cough.log',shell=True)
		cough=open('cough.log','r')
		lines=cough.readlines()
		cough.close()
		last_line=lines[len(lines)-1]
		currentDT1=datetime.datetime.now()
		datetime2=(currentDT1.strftime("%Y-%m-%d-%H-%M-%S"))
		to_write=datetime2+' '+last_line
		f.write(to_write)
		time1+=1
	f.close()
    #i+=1