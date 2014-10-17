#!/usr/bin/env python  
import roslib
roslib.load_manifest('me495_hw1_turtle')
import rospy
import math
import tf
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute

def talker():
     # set initial state to (x,y,theta) = (0,0,0)
     #rospy.wait_for_service('turtle1/teleport_absolute')
     #turtle1_teleport = rospy.ServiceProxy('turtle1/teleport_absolute', TeleportAbsolute)
     #turtle1_teleport(0,0,0)

     __rate_T = 10 # this should be a private parameter
     pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
     rospy.init_node('turtle_tf_broadcaster')
     r = rospy.Rate(__rate_T)
     test = Twist()
     test.linear.x = 0.0
     test.linear.y = 0.0
     test.linear.z = 0.0
     test.angular.x = 0.0
     test.angular.y = 0.0
     test.angular.z = 0.0
     while not rospy.is_shutdown():
          now = rospy.get_time()
          cur_angle = math.atan2(3*math.sin((4*math.pi*now)/__rate_T),3*math.sin((2*math.pi*now)/__rate_T))
          test.linear.x = 3*math.sin((4*math.pi*now)/__rate_T) * math.cos(cur_angle)
          #test.linear.y = 3*math.sin((2*math.pi*now)/rate_T)
          test.angular.z = math.atan2(3*math.sin((4*math.pi*now)/__rate_T),3*math.sin((2*math.pi*now)/__rate_T))
          pub.publish(test)
          r.sleep()

if __name__ == '__main__':
     try:
          talker()
     except rospy.ROSInterruptException: pass


