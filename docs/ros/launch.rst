Roslaunch
===============

Using roslaunch command
-----------------------

Usage:

.. code:: bash

    roslaunch [package] [filename.launch]

First go to the techx2019 package we created and built earlier:

.. code:: bash

    roscd techx2019

Create a launch directory:

.. code:: bash

    mkdir launch
    cd launch

The Launch File
---------------

Now let's create a launch file called turtlemimic.launch

.. code:: bash

    touch turtlemimic.launch
    gedit turtlemimic.launch

Paste the following:

.. code:: xml

    <launch>

    <group ns="turtlesim">

        <node pkg="turtlesim" name="turtle1" type="turtlesim_node"/>
        <node pkg="turtlesim" name="turtle2" type="turtlesim_node"/>
        <node pkg="techx2019" name="talker" type="talker.py" output="screen"/>

    </group>

    </launch>

Run the launch file:

.. code:: bash

    roslaunch techx2019 turtlemimic.launch