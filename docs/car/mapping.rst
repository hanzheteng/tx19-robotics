Mapping
========

**The following steps are running on ROS2GO platform**

Open a terminal, connect with your car.

First, bring up everything on your car

.. code:: bash

    roslaunch racecar_bringup racecar_bringup.launch

Then, Open another terminal and SSH into your car

**On your car**, config network variables by modifying your ~/.bashrc file:

.. code:: bash

    sudo gedit ~/.bashrc

in the poped up text editor, add these two lines to the bottom of the file.

.. code:: bash

    ROS_MASTER_URI=http://yourcarip:11311
    ROS_IP=yourcarip

where "yourcarip" is the IP address of your car (192.168.50.10*). 

Save the file and type in terminal:

.. code:: bash

    source ~/.bashrc

Open another terminal, then open a terminal and type:

.. code:: bash

    ifconfig

then find the IP address of your computer in the printed message. It should look like 192.168.50.***.

Then config network variables **on your computer**

.. code:: bash

    sudo gedit ~/.bashrc

Then add these two lines to the bottom of the file:

.. code:: bash

    export ROS_MASTER_URI=http://yourcarip:11311
    export ROS_IP=yourcomputerip

save the file and type in terminal:

.. code:: bash

    source ~/.bashrc

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

Run the mapping launch file to start mapping

.. code:: bash

    roslaunch racecar_slam racecar_laser_only_cartographer.launch

You may see something like this

.. image:: pics/slam.png
   :width: 1200

Tp save the map, open a new terminal and run

.. code:: bash

    rosrun map_server map_saver --occ 51 --free 49 -f test_carto_map