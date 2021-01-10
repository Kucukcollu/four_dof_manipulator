## four_dof_manipulator

#### Graduation Project 2020-2021: Simulation of Serial and Parallel Manipulators in ROS<br></br>


##### Project Members:
###### [Ali Aydın Küçükçöllü](mailto:kucukcollu@outlook.com)
###### [Batuhan Yalçınkaya](mailto:batuhanyalcinkayayk@gmail.com)
###### [Nurettin Uğur Alagaş](mailto:alaugurala@hotmail.com)<br></br>

##### ROS distro: Noetic <br></br>

##### How it Wors?
###### `$cd catkin_ws/src`
###### `$git clone https://github.com/Kucukcollu/four_dof_manipulator.git`
###### `$cd catkin_ws/`
###### `$catkin_make`

###### Simulation on RViz
###### `$roslaunch four_dof_manipulator display.launch`<br></br>

###### Simulation on Gazebo
###### `$roslaunch four_dof_manipulator gazebo.launch`

###### demo with controller

###### `$rostopic pub /arm_controller/command trajectory_msgs/JointTrajectory '{joint_names: ["joint_1","joint_2","joint_3","joint_4"],points:[{positions: [-1.0,1.8,-5.8,-2.4],time_from_start:[1,0]}]}' -1`

###### `$rostopic pub /arm_controller/command trajectory_msgs/JointTrajectory '{joint_names: ["joint_1","joint_2","joint_3","joint_4"],points:[{positions: [-1.5,1.15,-1.8,0.60],time_from_start:[1,0]}]}' -1`
