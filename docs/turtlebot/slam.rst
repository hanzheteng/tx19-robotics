Get in touch with SLAM
========================

Start the turtlebot3 world
---------------------------

.. code:: bash

    roslaunch turtlebot3_gazebo turtlebot3_world.launch

Start the SLAM RViz
--------------------

.. code:: bash

    roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=karto

Open teleop keyboard control
-----------------------------

.. code:: bash

    rosrun turtlebot3_teleop turtlebot3_teleop_key 