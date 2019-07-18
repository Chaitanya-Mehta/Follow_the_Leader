#!/usr/bin/env python
import rospy
from std_msgs.msg import String

#follower robot subscribes to leader's pose, 
# its own pose and publishes its future speed to its own turtle
# location of the leader is its goal position, but it achiieves it while avoiding obstacles

# It may not be necessary that the follower should see the leader.
# As a sheep, It would go where bulk of the sheep goes, following the first one. 
def chatter_callback(message):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", message.data)
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, chatter_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1)
    i = 0
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % i
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
        i=i+2
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass