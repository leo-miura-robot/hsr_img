#!/usr/bin/env python
## coding: UTF-8

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge, CvBridgeError


def callback_rgb(msg):
    
    bridge_rgb = CvBridge()
    rgb_image = bridge_rgb.imgmsg_to_cv2(msg,"bgr8").copy()
    img_gray = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("gray", img_gray)
    cv2.imshow("rgb",rgb_image)
    cv2.waitKey(1)

    
def main():
    rospy.init_node("camera",anonymous=True)
    pub = rospy.Subscriber("/hsrb/head_rgbd_sensor/rgb/image_rect_color",Image,callback_rgb)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
