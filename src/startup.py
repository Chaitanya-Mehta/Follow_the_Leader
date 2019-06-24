#!/usr/bin/env python

import sys
import rospy
from turtlesim.srv import Spawn
from turtlesim.srv import SpawnRequest
from turtlesim.srv import SpawnResponse

def add_two_ints_client(x, y):
    rospy.wait_for_service('turtlesim/Spawn')
    try:
        add_two_ints = rospy.ServiceProxy('turtlesim_spawn', Spawn)
        resp1 = (x, y)
        return setup_done:
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        print usage()
        sys.exit(1)
    print "Spawning %s turtles for startup"%(n)
    setup_done = setup_turtlesim(n)
    if setup_done:
        print "Setup Complete"
    else:
        print "Setup Failed"
    