Laptop

Function :
1)  Displays the decision whether a door is OPEN or CLOSE in a bluemix webpage
2)  Creates a bluemix webapp using IoTF service provided by bluemix

Initial Steps (Bluemix)
1) Create a bluemix account at console.bluemix.net
2) Create a service (IoTF). Then you will get your organization id
3) Register the device (RaspberryPi) with the service. To register the device you will need the device id from Pi
4) Create a python based web app
5) The service and app can be found on the bluemix dashboard
6) Save the tokens and keys for future use

Laptop
1) Install CLI command line interface
2) Download the sample application for bluemix
3) Unzip the app and make the following changes
	(a) manifest.yml : change corresponding changes for organization id, memory required, service name
	(b) proc file : Here you have to specify the file that needs to be run by your app
	(c) requirements.txt : Here you have to specify all the libraries that need to be installed to run your app
4) Write the python code to create webapp

How to login? 
1) Open terminal/command window
2) Go to the folder that has your code
3) bx login
	Enter your email and password
4) bx target --cf
	This will show your bluemix organization and space

How to run?
1) bx cf push <Folder Name>
2) After it is completed, you may see your app logs using bx cf logs <folder> --recent

Creating training data set
1) Run the doorcaptureevents.py on RaspberryPi and save the data in a file train.csv
2) Save this train.csv in the folder of bluemix app code. This file will be used by the SVM classifier to train the model

How to launch webpage?
Pushing the code to bluemix creates a webpage at <orgid>.mybluemix.net

Note : you may have to change the options parameters based on your credentials