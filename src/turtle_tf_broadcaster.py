#!/usr/bin/env python  
import roslib
roslib.load_manifest('me495_hw1_turtle')
import rospy
import math
import tf
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute
from turtlesim.msg import Pose
import sys

def talker(rate_T):
     # set initial position
     rospy.wait_for_service('turtle1/teleport_absolute')
     turtle1_teleport = rospy.ServiceProxy('turtle1/teleport_absolute', TeleportAbsolute)
     turtle1_teleport(5.4444444, 5.4444444,(math.pi)/6.5)
     
     pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
     velocity = Twist()
     start_time = rospy.get_time()
     while not rospy.is_shutdown():
          now = rospy.get_time() - start_time

          x_in = (4*math.pi*now)/rate_T
          y_in = (2*math.pi*now)/rate_T

          x_t = 3*math.sin(x_in)
          x_t_1 = ((12*math.pi)/rate_T) * math.cos(x_in)
          x_t_2 = -((48*(math.pow(math.pi,2)))/(math.pow(rate_T,2)))*math.sin(x_in)

          y_t = 3*math.sin(y_in)
          y_t_1 = ((6*math.pi)/rate_T) * math.cos(y_in)
          y_t_2 = -((12*(math.pow(math.pi,2)))/(math.pow(rate_T,2)))*math.sin(y_in)

          cur_angle = math.atan2(y_t,x_t)

          v_t = math.sqrt(math.pow(x_t_1,2) + math.pow(y_t_1,2))
          w_t = ((x_t_1*y_t_2) - (y_t_1*x_t_2))/(math.pow(x_t_1,2) + math.pow(y_t_1,2))

          velocity.linear.x = v_t #* math.cos(cur_angle)
          velocity.angular.z = w_t#cur_angle

          pub.publish(velocity)

if __name__ == '__main__':
     args = rospy.myargv(argv=sys.argv)
     rate_T = int(args[1])
     try:
          rospy.init_node('turtle_tf_broadcaster')
          talker(rate_T) 
     except rospy.ROSInterruptException: pass