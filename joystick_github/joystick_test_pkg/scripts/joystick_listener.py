#!/usr/bin/env python

import rospy, time
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

def joystick_callback(data):
  rospy.loginfo("Dato 1: %s", data.axes[0])
  rospy.loginfo("Dato 2: %s", data.buttons[0])

  pub=rospy.Publisher('joystick_cmd_vel', Twist, queue_size=1)
  twist=Twist()
  twist.linear.x=data.axes[0]
  twist.angular.z=data.axes[1]
  rospy.loginfo("twist.linear: %f ; angular %f", twist.linear.x, twist.angular.z)
  pub.publish(twist)

  if data.buttons[0]==1:
    rospy.loginfo("Hola")


def joystick_listener():
  rospy.init_node('joystick_listener', anonymous=True)
  rospy.loginfo("Conectado")
  rospy.Subscriber('joy', Joy, joystick_callback)

  
  



  rospy.spin()

if __name__=='__main__':
  try:
    joystick_listener()
  except rospy.RosInterruptException:
    pass
