Get in touch with SLAM
========================

Start the turtlebot3 world
---------------------------

.. code:: bash

    roslaunch turtlebot3_gazebo turtlebot3_world.launch

Start the SLAM RViz
--------------------

If your system is **Ubuntu 16.04, run this code to install SLAM algorithm:**

.. code:: bash

    sudo apt install ros-kinetic-gmapping
    roslaunch turtlebot3_slam turtlebot3_slam.launch

If your system is **Ubuntu 18.04:**

.. code:: bash

    roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=karto

Open teleop keyboard control
-----------------------------

.. code:: bash

    rosrun turtlebot3_teleop turtlebot3_teleop_key 