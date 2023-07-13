#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import Header
from nav_msgs.msg import Odometry

from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3


if __name__ == "__main__":
    rospy.init_node("odometry_publisher")
    pub = rospy.Publisher("odom", Odometry, queue_size=10)
    rate = rospy.Rate(10)  # Set the publishing rate

    while not rospy.is_shutdown():
        current_time = rospy.Time.now()
        # Fill in your odometry data here
        x = 0.0  # X position
        y = 0.0  # Y position
        theta = 0.0  # Orientation (yaw angle)
        vx = 0.0  # Linear velocity along X-axis
        vy = 0.0  # Linear velocity along Y-axis
        vtheta = 0.0  # Angular velocity

        # Create the odometry message
        odom = Odometry()
        odom.header = Header()
        odom.header.stamp = current_time
        odom.header.frame_id = "odom"
        odom.child_frame_id = "base_footprint"
        odom.pose.pose.position.x = x
        odom.pose.pose.position.y = y
        odom.pose.pose.position.z = 0.0
        odom.pose.pose.orientation.x = 0.0
        odom.pose.pose.orientation.y = 0.0
        odom.pose.pose.orientation.z = 0.0
        odom.pose.pose.orientation.w = 1.0
        odom.twist.twist.linear.x = vx
        odom.twist.twist.linear.y = vy
        odom.twist.twist.linear.z = 0.0
        odom.twist.twist.angular.x = 0.0
        odom.twist.twist.angular.y = 0.0
        odom.twist.twist.angular.z = vtheta

        # Publish the odometry message
        pub.publish(odom)
        rate.sleep()
