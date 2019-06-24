#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose

def chatter_callback(message):
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, chatter_callback)
    rospy.spin()
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, chatter_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

def velocity_commander():
    rate = rospy.Rate(1)
    i = 0
    while not rospy.is_shutdown():
        pose_pub.publish()
        rate.sleep()
if __name__ == '__main__':
    try:
        pose_pub = rospy.Publisher('leader_pose', String, queue_size=10)
        rospy.init_node('leader_pose_publisher', anonymous=True)
    except rospy.ROSInterruptException:
        pass