from flask import Flask,redirect
from flask import render_template
from flask import request
import os,json
import ibmiotf.application
import pandas as pd
import numpy as np
from sklearn import svm
import csv
from bs4 import BeautifulSoup,Tag
import re
import urllib2
import time
import datetime


client=None
app=Flask(__name__)
port=os.getenv('VCAP_APP_PORT','1883')

train_dataframe = pd.read_csv('train.csv')
train_labels = train_dataframe.Class_Label
labels = list(set(train_labels))
train_labels = np.array([labels.index(x) for x in train_labels])
train_features = train_dataframe.iloc[:,1:]
train_features = np.array(train_features)

classifier = svm.SVC()
classifier.fit(train_features, train_labels)

count = 0;
flag=True
res=[]
results=[]
test_features=[]
test_results=[]
time_stamps=[]
def classify():
	print "INSIDE CLASSIFY\n"
	global flag
	global test_results
	global test_features
	if(flag):
		print "START CLASSIFY\n"
		for x in test_features:
			results = classifier.predict(x)
	flag=False


def myCommandCallback(cmd):
	global code
	global writer
	global count
	global flag
	global test_features
	global time_stamps
	if cmd.event == "door":
		p=json.loads(cmd.payload)
		x_val=p['xAcc']
		if(count<=30):
			 test_features.append(x_val)
			 count=count+1
		else:
			 if(flag):
				classify()




@app.route('/')
def hello():
	global test_features
	global test_results
	global time_stamps
	code=''
	code_r=''
	final_dec=''
	ts=''
	print "code here"
	if(len(test_features)>0):
		for x in test_features:
			code=code+'  '+str(x)
			if(x==0):
				code_r=code_r+'  '+'OPEN'
			else:
				code_r=code_r+'  '+'CLOSE'
		st = time.time()
		ts=datetime.datetime.fromtimestamp(st).strftime('%Y-%m-%d %H:%M:%S')
	else:
		code=code+'NONE'
		code_r=code_r+'NONE'
		final_dec='NONE'
		
	return '<!doctype html>\n<html><head><title>HW4</title></head><body><h5>GROUP 7 HW 4 CSC 591</h5><br /><br /><h3>X_ACC_VAL : '+code+'</h3><br /><h3>CLASS LABELS : '+code_r+'</h3><br /><br /><br />Time STamps : '+ts+'</body></html>'

	

if __name__=="__main__":
	try:

		options = {"org":"vwcasz",
			   "type":"standalone",
			   "id":"1",
			   "auth-method":"use-token-auth",
			   "auth-token":"f4Q-03@Ti9*gysZdqa",
			   "auth-key":"a-vwcasz-7ag752fyzc"}
			   
		client=ibmiotf.application.Client(options)
		client.connect()
		client.deviceEventCallback=myCommandCallback
		client.subscribeToDeviceEvents(deviceType="RaspberryPi")
	
	except ibmiotf.ConnectionException as e:
		print e
	time.sleep(10)
	app.run(host='0.0.0.0',port=int(port))