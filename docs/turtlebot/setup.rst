Setting up Turtlebot3
======================

Turtlebot3 is only available in **ROS Kinetic** and **ROS Melodic**

The installation methods for ROS Kinetic and ROS Melodic are **different**:

Download & Install Turtlebot3 Package
---------------------------------------

Please choose only one from the following installation method according to your environment
只从下列两种安装中，根据你的系统环境选择一种

* **ROS Kinetic (Ubuntu 16.04)**

.. code:: bash

    sudo apt install ros-kinetic-turtlebot3-*
    cd ~/catkin_ws
    catkin_make
    source ~/catkin_ws/devel/setup.bash
    rospack profile

* **ROS Melodic (Ubuntu 18.04)**

.. code:: bash

    cd ~/catkin_ws/src
    git clone https://github.com/ROBOTIS-GIT/turtlebot3.git
    git clone https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
    git clone https://github.com/ROBOTIS-GIT/turtlebot3_simulation.git
    git clone https://github.com/ROBOTIS-GIT/turtlebot3_autorace.git
    cd ..
    rosdep install --from-paths src -i -y
    catkin_make
    source ~/catkin_ws/devel/setup.bash
    rospack profile

Turtlebot3 Model Config
-------------------------

There are two kinds of model for Turtlebot3. If you don't choose one of them, the program **will not** run.
For general purpose, we choose to use "burger" model.

.. code:: bash

    echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
    source ~/.bashrc

Test Launch
------------

If everything is set up correctly, you should get a opened simulator with a small robot inside it.

.. code:: bash

    roslaunch turtlebot3_gazebo turtlebot3_world.Launch

You can use **Ctrl+C** to exit the program