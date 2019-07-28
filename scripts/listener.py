#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose

def printMessage(msg):

    print msg.x
    print msg.y
    print msg.theta

def listener():

    rospy.init_node('listener')

    rospy.Subscriber('turtle1/pose', Pose, printMessage)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()