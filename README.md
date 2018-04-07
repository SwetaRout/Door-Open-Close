# Door-Open-Close-

In this assignment, you will develop an inertial measurement unit (IMU) and cloud based system that will identify door open and door close events. You will attach the IMU sensor to a door, and using values from the IMU, determine when it has been closed and when opened. 
An IMU usually comprises a 3-axis analog gyro and a 3-axis accelerometer.  Here is a link to one: http://www.amazon.com/gp/product/B008BOPN40. IMUs are primarily used to sense and measure motion. The phones use them, for example, to switch screen orientation when you rotate the phone. Search online and you will find several tutorials on what an accelerometer and a gyro is and how to use them programmatically. 
You will attach the IMU sensor to a door, and interface the IMU sensor with an IoT device (any IoT device of your choice, such as a Raspberry Pi, Beaglebone, Arduino etc), which will collect the values from the sensor and send to a cloud service (such as IBM Bluemix). You will run a classification algorithm in the cloud service, which will monitor the values it receives from the IoT device. Whenever the door is opened or closed, the cloud service should automatically identify whether the door has been opened or closed respectively. The cloud service will then send the decision to an application running on your personal device (can be a laptop or smart phone). This application will continuously show the current status of the door (i.e., whether it is closed or open). 
For the classification technique, use support vector machines. I will recommend that you use the libSVM implementation (https://www.csie.ntu.edu.tw/~cjlin/libsvm/). As IBM Bluemix has a python runtime, you will port the python version of libSVM to IBM Bluemix. All processing of the values reported by the IMU should happen in Bluemix. The IoT device should only be used to relay those values to IBM Bluemix. The communication protocol between the IoT device and the IBM Bluemix must be MQTT. IBM Bluemix supports MQTT. The decision on each door opening and closing must be sent to a laptop/smart phone. Both the IoT device and the laptop/smartphone will be MQTT clients. IoT device will be publisher; laptop/smartphone will be subscriber. The laptop/smart phone should show the current status whether the door is opened or closed. Every time a new door open/close event is detected by the cloud service and pushed to the laptop/smart phone, the laptop/smart phone should update the decision it is showing to the user and also show the time of latest decision. 
For the classification scheme to work, you will need training instances. To collect training instances, attach the IMU to a door. Height of the sensor does not matter but distance from the hinge does. I would suggest that you refrain from attaching the IMU at the opening edge of the door because if you collect all your training data from the edge of a door, your scheme may not work on another door with different size. To make a decision, you are free to require the door to be moved by a certain angular distance before making a decision. For example, your implementation may require that the door must be opened by at least 45 degrees before your implementation can detect and recognize it. Similarly, when closing the door, you can say that your implementation can detect and recognize a door close only when the door moves by at least 20 degrees etc. Your choice! But make sure that one motion of door opening is recorded as one door open event and not multiple. Same applies to door closing. For example, if you require the door to be closed by at least 20 degrees to detect a door close event, but if you move the door by 70 degrees in one go, then that should be detected as a single door close event, not 3 door close events. 