Mapping
========

Open a terminal, connect with your car

First, bring up everything on your car

.. code:: bash

    roslaunch racecar_bringup racecar_bringup.launch

Then, Open another terminal and SSH into your car


**On your car**, config network variables

.. code:: bash

    export ROS_MASTER_URI=http://yourcarip:11311
    export ROS_IP=yourcarip

On your computer, find your computer's ip

.. code:: bash

    ifconfig

Open another terminal, config network variables **on your computer**

.. code:: bash

    export ROS_MASTER_URI=http://yourcarip:11311
    export ROS_IP=yourcomputerip

You can use the following code to check if your environment variables have been set correcly

.. code:: bash

    echo $ROS_MASTER_URI
    echo $ROS_IP

Get into your computer's SLAM package

.. code:: bash

    roscd racecar_slam

Update to the latest SLAM package

.. code:: bash

    git pull origin master

Make the package

.. code:: bash
    
    cd ~/catkin_ws
    catkin_make

Run the mapping launch file

.. code:: bash

    roslaunch racecar_slam racecar_laser_only_cartographer.launch