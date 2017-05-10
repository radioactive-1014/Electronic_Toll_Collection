#!/usr/bin/env python
import roslib
roslib.load_manifest('detection')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError



def callback(data):
	cv_image = bridge.imgmsg_to_cv2(data, desired_encoding="passthrough")
	
	gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
	cv2.imshow("Image window", gray_image)
	cv2.waitKey(3)
	print "do nothing"


bridge = CvBridge()
rospy.init_node('image_converter', anonymous=True)
image_sub = rospy.Subscriber("/usb_cam/image_raw",Image,callback)

rospy.spin()
 
cv2.destroyAllWindows()
