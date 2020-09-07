#!/usr/bin/env python

from __future__ import division
import rospy, time
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
import RPi.GPIO as GPIO
from std_msgs.msg import Int32
import Adafruit_PCA9685

# Initialise the PCA9685 using the default address (0x40).
pwm0 = Adafruit_PCA9685.PCA9685(address=0x40)

# Alternatively specify a different address and/or bus:
pwm1 = Adafruit_PCA9685.PCA9685(address=0x41)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(pwmno,channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    if pwmno == 0:
        pwm0.set_pwm(channel, 0, pulse)
    elif pwmno == 1:
        pwm1.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm0.set_pwm_freq(60)
pwm1.set_pwm_freq(60)

def joystick_callback(data):
  # rospy.loginfo("Dato 1: %s", data.axes[0])
  # rospy.loginfo("Dato 2: %s", data.buttons[0])

  pub=rospy.Publisher('joystick_cmd_vel', Twist, queue_size=1)
  twist=Twist()
  twist.linear.x=data.axes[0]
  twist.angular.z=data.axes[1]
  # rospy.loginfo("twist.linear: %f ; angular %f", twist.linear.x, twist.angular.z)
  pub.publish(twist)

  if data.buttons[0]==1:    # Cuadrado
    rospy.loginfo("Arriba")
    # All servos to 90
    pwm0.set_pwm(0, 0, 375)
    pwm0.set_pwm(1, 0, 375)
    pwm0.set_pwm(2, 0, 375)
    time.sleep(2)
    pwm0.set_pwm(3, 0, 375)
    pwm0.set_pwm(4, 0, 375)
    pwm0.set_pwm(5, 0, 375)
    time.sleep(2)
    pwm0.set_pwm(6, 0, 375)
    pwm0.set_pwm(7, 0, 375)
    pwm0.set_pwm(8, 0, 375)
    time.sleep(2)
    pwm0.set_pwm(9, 0, 375)
    pwm0.set_pwm(10, 0, 375)
    pwm0.set_pwm(11, 0, 375)
    time.sleep(2)
    pwm0.set_pwm(12, 0, 375)
    pwm0.set_pwm(13, 0, 375)
    pwm0.set_pwm(14, 0, 375)
    time.sleep(2)
    pwm0.set_pwm(15, 0, 375)
    pwm1.set_pwm(0, 0, 375)
    pwm1.set_pwm(1, 0, 375)
    print('servos ok')

  if data.buttons[1]==1:    # Equis
    rospy.loginfo("Hola")
    pwm0.set_pwm(10, 0, 580)
    pwm0.set_pwm(11, 0, 490)
    pwm0.set_pwm(9, 0, 450)
    time.sleep(1)
    pwm0.set_pwm(9, 0, 300)
    time.sleep(1)
    pwm0.set_pwm(9, 0, 375)
    pwm0.set_pwm(11, 0, 375)
    pwm0.set_pwm(10, 0, 375)    

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
