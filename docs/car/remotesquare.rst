Use script to control Racecar
=============================

enter your techx2019 package's script folder

.. code:: bash

    roscd techx2019/scripts

create and edit square.py

.. code:: bash

    touch square.py
    chmod +x square.py
    gedit square.py

Configure environment variables on your computer:
**Note:yourcarip is the IP address of your car. For example, 192.168.50.101**

.. code:: bash

    export ROS_MASTER_URI=http://yourcarip:11311

check your computer's ip address

.. code:: bash

    ifconfig

and then set the environment variable

.. code:: bash

    export ROS_IP=yourcomputerip

After configuring your computer, run the following code on the car

.. code:: bash

    export ROS_MASTER_URI=http://yourcarip:11311
    export ROS_IP=yourcarip

Copy and paste the following code:

.. code:: python

    #!/usr/bin/env python

    import rospy
    from geometry_msgs.msg import Twist
    import time

    def shut_down(pub, rate, msg):
        msg.linear.x = 1500
        msg.angular.z = 90
        pub.publish(msg)
        rate.sleep()

    def run_command(linear_x, angular_z, t, rate):
    #linear_x should be 1320-1680 where 1500 is stop
    #angular_z should be 66-114 where 90 is center
    #t is time
        init_time = time.time()

        while(time.time() - init_time < t):
            msg.linear.x = linear_x
            msg.angular.z = angular_z
            pub.publish(msg)
            rate.sleep()

    def run(pub, rate, msg):

        run_command(1640, 66, 2, rate)

        shut_down(pub, rate, msg)



    if __name__ == '__main__':

        pub = rospy.Publisher('/car/cmd_vel', Twist, queue_size=10)
        rospy.init_node('publisher')
        rate = rospy.Rate(10)
        msg = Twist()

        try:
            run(pub, rate, msg)
        except rospy.ROSInterruptException:
            shut_down(pub, rate, msg)
            pass

run the python code

.. code:: bash

    python square.py

