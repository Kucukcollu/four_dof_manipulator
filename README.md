## four_dof_manipulator

![four_dof_manipulator](https://github.com/Kucukcollu/four_dof_manipulator/blob/master/adds/1.png)

#### Graduation Project 2020-2021: Simulation of Serial and Parallel Manipulators in ROS<br></br>


##### Project Members:
###### [Ali Aydın Küçükçöllü](mailto:kucukcollu@outlook.com)
###### [Batuhan Yalçınkaya](mailto:batuhanyalcinkayayk@gmail.com)
###### [Nurettin Uğur Alagaş](mailto:alaugurala@hotmail.com)<br></br>

##### ROS distro: Noetic <br></br>

##### How it Works?
###### `$cd catkin_ws/src`
###### `$git clone https://github.com/Kucukcollu/four_dof_manipulator.git`
###### `$cd catkin_ws/`
###### `$catkin_make`

###### Simulation on RViz
###### `$roslaunch four_dof_manipulator display.launch`<br></br>

![](https://github.com/Kucukcollu/four_dof_manipulator/blob/master/adds/rviz-Trim.gif)

###### Simulation on Gazebo
###### `$roslaunch four_dof_manipulator gazebo.launch`

###### demo with controller

###### `$rostopic pub /arm_controller/command trajectory_msgs/JointTrajectory '{joint_names: ["joint_1","joint_2","joint_3","joint_4"],points:[{positions: [0.98,0.83,-3.62,0.19],time_from_start:[1,0]}]}' -1`

###### `$rostopic pub /arm_controller/command trajectory_msgs/JointTrajectory '{joint_names: ["joint_1","joint_2","joint_3","joint_4"],points:[{positions: [-0.58,1.27,-3.85,-0.44],time_from_start:[1,0]}]}' -1`

###### `$rostopic pub /arm_controller/command trajectory_msgs/JointTrajectory '{joint_names: ["joint_1","joint_2","joint_3","joint_4"],points:[{positions: [-1.08,0.68,-3.46,0.70],time_from_start:[1,0]}]}' -1`

###### `$rostopic pub /arm_controller/command trajectory_msgs/JointTrajectory '{joint_names: ["joint_1","joint_2","joint_3","joint_4"],points:[{positions: [0.60,-0.63,-6.28,0.13],time_from_start:[1,0]}]}' -1`

###### `$rostopic pub /arm_controller/command trajectory_msgs/JointTrajectory '{joint_names: ["joint_1","joint_2","joint_3","joint_4"],points:[{positions: [-0.44,-0.47,-6.28,-0.86],time_from_start:[1,0]}]}' -1`
