Create a workspace
==================

Let's create and build a catkin workspace:

.. code:: bash

    mkdir -p ~/catkin_ws/src
    cd ~/catkin_ws/
    catkin_make
    echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc