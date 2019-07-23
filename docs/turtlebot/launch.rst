Using roslaunch to simplify the program
========================================

We have learned how to use roslaunch. NOw we can use it on our turtlebot waypoint nevigation program.

First, get into the package launch directory

.. code:: bash

    roscd turtlebot3_gazebo/launch/

Create a new blank launch file called **turtlebot3_waypoint.launch** and edit it

.. code:: bash

    touch turtlebot3_waypoint.launch
    gedit turtlebot3_waypoint.launch

Copy and paste the following launch file code:

.. code:: xml

    <launch>
    <arg name="model" default="$(env TURTLEBOT3_MODEL)" doc="model type [burger, waffle, waffle_pi]"/>
    <arg name="x_pos" default="-2.0"/>
    <arg name="y_pos" default="-0.5"/>
    <arg name="z_pos" default="0.0"/>

    <include file="$(find gazebo_ros)/launch/empty_world.launch">
        <arg name="world_name" value="$(find turtlebot3_gazebo)/worlds/turtlebot3_world.world"/>
        <arg name="paused" value="false"/>
        <arg name="use_sim_time" value="true"/>
        <arg name="gui" value="true"/>
        <arg name="headless" value="false"/>
        <arg name="debug" value="false"/>
    </include>

    <param name="robot_description" command="$(find xacro)/xacro --inorder $(find turtlebot3_description)/urdf/turtlebot3_$(arg model).urdf.xacro" />

    <node pkg="gazebo_ros" type="spawn_model" name="spawn_urdf"  args="-urdf -model turtlebot3_$(arg model) -x $(arg x_pos) -y $(arg y_pos) -z $(arg z_pos) -param robot_description" />
    <node pkg="turtlebot3_gazebo" name="waypoint" type="waypoint.py" output="screen"/>
    </launch>

Save and close the file

Run the launch file

.. code:: bash

    roslaunch turtlebot3_gazebo turtlebot3_waypoint.launch