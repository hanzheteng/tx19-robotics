Navigation
===========

Get into the map folder

.. code:: bash

    roscd racecar_slam/maps/

Download the map data and save it into this folder

Get into the Navigation folder and change the linear velocity data

.. code:: bash

    roscd racecar_navigation/launch/includes/
    gedit tianbot_move_base.launch.xml  

find the line of baseSpeed and change it into

.. code:: xml

    <param name="baseSpeed" value="1600"/> <!-- pwm for motor constant speed, 1480: stop, 1440: ~0.5m/s, 1430: ~1.5m/s --> 

start the Navigation program

.. code:: bash

    roslaunch racecar_navigation racecar_amcl_nav.launch 

Open another terminal to run rViz

.. code:: bash

    rviz

Add the map data inside rviz