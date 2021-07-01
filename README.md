## four_dof_manipulator
#### Simulation of 4 DoF Manipulator

![four_dof_manipulator](https://github.com/Kucukcollu/four_dof_manipulator/blob/master/adds/solidworks.png)

#### Project Information
##### OS: Ubuntu 18.04
##### ROS distro: Melodic
##### Additional Plugin: [gazebo_grasp_fix](https://github.com/JenniferBuehler/gazebo-pkgs/wiki/The-Gazebo-grasp-fix-plugin)<br></br>

#### How it works in your machine?
##### `$cd catkin_ws/src`
##### `$git clone https://github.com/Kucukcollu/four_dof_manipulator.git`
##### for MoveIt package
##### `https://github.com/Kucukcollu/manipulator_motion_planning`
##### `$cd catkin_ws/`
##### `$catkin_make`<br></br>


#### Simulation in RViz
##### `$roslaunch four_dof_manipulator display.launch`<br></br>

![](https://github.com/Kucukcollu/four_dof_manipulator/blob/master/adds/rviz.PNG)<br></br>

#### Simulation in Gazebo
##### `$roslaunch four_dof_manipulator gazebo.launch`

![](https://github.com/Kucukcollu/four_dof_manipulator/blob/master/adds/gazebo.PNG)<br></br>

#### Mainly there are three way to simulate manipulator
##### 1- Publish command from terminal

##### Controlling of arm:

##### `$rostopic pub /arm_controller/command trajectory_msgs/JointTrajectory '{joint_names: ["joint_1","joint_2","joint_3","joint_4"],points:[{positions: [0.98,0.83,-3.62,0.19],time_from_start:[1,0]}]}' -1`

##### Controlling of hand:

##### `$rostopic pub /hand_controller/command trajectory_msgs/JointTrajectory '{joint_names: ["finger1","finger2"],points:[{positions: [0.2,-0.2],time_from_start:[1,0]}]}' -1`

##### 2- Run MoveIt and Gazebo together
##### `$roslaunch four_dof_manipulator all.launch`

![](https://github.com/Kucukcollu/four_dof_manipulator/blob/master/adds/rvizANDgazebo.PNG)


##### 3- Run via Script
##### `$roslaunch four_dof_manipulator gazebo.launch`
##### or
##### `$roslaunch four_dof_manipulator all.launch`
##### then
##### `$rosrun four_dof_manipulator manipulator_motion.py`<br></br>

#### Final Simulation

![](https://github.com/Kucukcollu/four_dof_manipulator/blob/master/adds/simülasyon.gif)<br></br>

##### Project Members:
###### [Ali Aydın Küçükçöllü](mailto:kucukcollu@outlook.com)
###### [Batuhan Yalçınkaya](mailto:batuhanyalcinkayayk@gmail.com)
###### [Nurettin Uğur Alagaş](mailto:alaugurala@hotmail.com)<br></br>
