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

Now let's create a launch file called turtlemimic.launch and paste the following:

.. code:: xml

    <launch>

    <group ns="turtlesim1">
        <node pkg="turtlesim" name="sim" type="turtlesim_node"/>
    </group>

    <group ns="turtlesim2">
        <node pkg="turtlesim" name="sim" type="turtlesim_node"/>
    </group>

    </launch>

