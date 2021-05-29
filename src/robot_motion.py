#!/usr/bin/env python

import rospy
import time
from trajectory_msgs.msg import JointTrajectory,JointTrajectoryPoint
from sensor_msgs.msg import JointState

def go_to_goal():

    jt=JointTrajectory()

    jt.header.stamp = rospy.Time.now()

    jt.joint_names.append("Joint_1")
    jt.joint_names.append("Joint_2")
    jt.joint_names.append("Joint_3")
    jt.joint_names.append("Joint_4")

    p=JointTrajectoryPoint()

    p.positions.append(0.60)
    p.positions.append(-0.63)
    p.positions.append(-6.28)
    p.positions.append(0.13)

    jt.points.append(p)

    for i in range(4):
        jt.points[i].time_from_start = rospy.Duration.from_sec(0.01)

    trajectory_publisher.publish(jt)


if __name__ == '__main__':
    try:
        
        rospy.init_node('manipulator_task_motion', anonymous=True)
        
        joint_command='/joint_states'
        trajectory_publisher = rospy.Publisher(joint_command, JointTrajectory, queue_size=1)

        position_command = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(position_command, JointState, poseCallback)

        time.sleep(2)

        go_to_goal()
    
    except rospy.ROSInterruptException:
        rospy.loginfo("Node Terminated.")
