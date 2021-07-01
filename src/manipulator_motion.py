#!/usr/bin/env python

from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
import roslib;roslib.load_manifest('four_dof_manipulator')
from trajectory_msgs.msg import JointTrajectoryPoint
from std_msgs.msg import Float64
import actionlib
import rospy
import time

class Manipulator:
    def __init__(self, robot_group):
        self.robot_group = robot_group
        self.jta = actionlib.SimpleActionClient('/'+self.robot_group+'_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
        rospy.loginfo('Waiting for joint trajectory action...')
        self.jta.wait_for_server()
        rospy.loginfo('Found joint trajectory action!!!')


    def move_joint(self, angles):
        goal = FollowJointTrajectoryGoal()
        # manipulator joint names
        goal.trajectory.joint_names = ['joint_1', 'joint_2','joint_3','joint_4']
        point = JointTrajectoryPoint()
        point.positions = angles
        point.time_from_start = rospy.Duration(3)
        goal.trajectory.points.append(point)
        self.jta.send_goal_and_wait(goal)

class Gripper(Manipulator):

    def move_joint(self, angles):
        goal = FollowJointTrajectoryGoal()
        # gripper joint names
        goal.trajectory.joint_names = ['finger1', 'finger2']
        point = JointTrajectoryPoint()
        point.positions = angles
        point.time_from_start = rospy.Duration(3)
        goal.trajectory.points.append(point)
        self.jta.send_goal_and_wait(goal)
 
def main():
    rospy.loginfo('Task started !!!')
    
    arm = Manipulator('arm') # define arm object to control manipulator
    hand = Gripper('hand') # define hand object to control gripper

    time.sleep(1)
    arm.move_joint([0,0,0,0])
    hand.move_joint([-0.25,0.25])
    time.sleep(1)
    arm.move_joint([-1,-0.36,-2.86,-0.33])
    hand.move_joint([0.2,-0.2])
    time.sleep(1)
    arm.move_joint([0.66,0.71,-2.89,-1.15])
    hand.move_joint([-0.25,0.25])
    time.sleep(1)
    arm.move_joint([-0.81,-0.42,-5.64,-0.57])
    hand.move_joint([-0.25,0.25])
    time.sleep(1)

    rospy.loginfo('Task finished!!!')

if __name__ == '__main__':
      rospy.init_node('four_dof_manipulator_move')
      main()
