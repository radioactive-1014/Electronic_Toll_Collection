#!/usr/bin/env python
import roslib

import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import numpy as np




bridge = CvBridge()
pub = rospy.Publisher("image_topic_2",Image,queue_size=1000)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(10) # 10hz
cap = cv2.VideoCapture('test7.mp4')
while (True):


		ret, frame = cap.read()
		
		if ret:
    		
			pub.publish(bridge.cv2_to_imgmsg(frame, "bgr8"))
			rate.sleep()
		else: 
			print "failed"	


print "done"			