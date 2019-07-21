Writing a Simple Publisher and Subscriber 
==========================================

Writing the Publisher Node
--------------------------

Change directory into the beginner_tutorials package

.. code:: bash

    roscd techx2019

The Code
~~~~~~~~

.. code:: bash

    mkdir scripts
    cd scripts
    touch talker.py
    chmod +x talker.py

Open the editor

.. code:: bash

    gedit talker.py

Copy the following Python Code into talker.py.

.. code:: python

    import rospy
    from geometry_msgs.msg import Twist

    def talker():
        pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
        rospy.init_node('publisher')
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            msg = Twist()
        msg.linear.x = 1.0
        msg.angular.z = 1.0
            pub.publish(msg)
            rate.sleep()

    if __name__ == '__main__':
        try:
            talker()
        except rospy.ROSInterruptException:
            pass

Build the code

.. code:: python

    cd ~/catkin_ws
    catkin_make

Test Using TurtleSim
~~~~~~~~~~~~~~~~~~~~

Open roscore

.. code:: bash

    roscore

Open TurtleSim

.. code:: bash

    rosrun turtlesim turtlesim_node

Run the code

.. code:: bash

    cd ~/catkin_ws/src/techx2019/scripts/
    python talker.py

Writing the Subscriber Node
---------------------------

The Code
~~~~~~~~

.. code:: bash

    roscd techx2019/scripts/
    wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/listener.py
    chmod +x listener.py
    
Building your nodes
-------------------

.. code:: bash

    cd ~/catkin_ws
    catkin_make

Play with Turtle
