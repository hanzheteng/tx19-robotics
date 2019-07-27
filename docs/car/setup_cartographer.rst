Setup Cartographer
==================

In this section we setup environment for cartographer on your own computer. (If you are running ros2go from USB, you can skip this section).

First install some required package:

.. code:: bash 

	sudo apt-get update 
	sudo apt-get install -y python-wstool python-rosdep ninja-build 

Then Create a new workspace 'carto_ws'. 

.. code:: bash 

	mkdir carto_ws 
	cd carto_ws 
	wstool init src 

Merge the cartographer_ros.rosinstall file and fetch code for dependencies. 

.. code:: bash 

	wstool merge -t src https://raw.githubusercontent.com/tianbot/tianbot_racecar/master/cartographer_ros.rosinstall 
	wstool update -t src 

Then install proto3. 

.. code:: bash 

	src/cartographer/scripts/install_proto3.sh 

Then install deb dependencies. note that the command 'sudo rosdep init' will print an error if you have already executed it since installing ROS. This error can be ignored. 

.. code:: bash 

	sudo rosdep init 
	rosdep update 
	rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y 

Lastly we build and install. 

.. code:: bash

	catkin_make_isolated --install --use-ninja 
	echo "source ~/carto_ws/install_isolated/setup.bash" >> ~/.bashrc

Now you can restart all terminal and move to next section.








