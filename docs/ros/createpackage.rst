Create ROS Package
==================

Creating a catkin Package
-------------------------

.. code:: bash

    cd ~/catkin_ws/src

Now use the catkin_create_pkg script to create a new package called 'techx2019' which depends on std_msgs, roscpp, and rospy:

.. code:: bash

    catkin_create_pkg techx2019 std_msgs rospy

Building a catkin workspace and sourcing the setup file
-------------------------------------------------------

Now you need to build the packages in the catkin workspace:

**Note: We need to use catkin_make because we create a new package**

.. code:: bash

    cd ~/catkin_ws
    catkin_make
    rospack profile