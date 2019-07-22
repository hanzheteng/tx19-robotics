Writing a Simple Publisher and Subscriber 
==========================================

Writing the Publisher Node
--------------------------

Change directory into the techx2019 package

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

Copy the following Python Code into talker.py:

.. code:: python

    #!/usr/bin/env python

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

**Open Another Terminal** to run TurtleSim

**打开另一个终端（命令行）来运行TurtleSim**

.. code:: bash

    rosrun turtlesim turtlesim_node

**Open Another Terminal** to run the code

**再打开一个终端（命令行）来运行代码**

Run the code

.. code:: bash

    cd ~/catkin_ws/src/techx2019/scripts/
    python talker.py

**You should keep every programs running and move on!! Open a Terminal**

**到这里，一定不要暂停任何代码，之后会用到！！打开一个新的命令行**

Writing the Subscriber Node
---------------------------

The Code
~~~~~~~~

.. code:: bash

    roscd techx2019/scripts/
    touch listener.py
    chmod +x listener.py
    
Open the editor

.. code:: bash

    gedit listener.py

Copy the following Python Code into listener.py.

.. code:: python

    #!/usr/bin/env python

    import rospy
    from turtlesim.msg import Pose

    def printMessage(msg):

        print msg.x
        print msg.y
        print msg.theta

    def listener():

        rospy.init_node('listener')

        rospy.Subscriber('turtle1/pose', Pose, printMessage)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()

    if __name__ == '__main__':
        listener()

Building your nodes
~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    cd ~/catkin_ws
    catkin_make

Save and run the code:

.. code:: bash

    roscd techx2019/scripts
    python listener.py
