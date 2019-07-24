Use script to control Racecar
=======================

enter your techx2019 package's script folder

.. code:: bash

    roscd techx2019/scripts

create and edit square.py

.. code:: bash

    touch square.py
    chmod +x square.py
    gedit square.py

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

    def run_command(linear_x, angular_z, time):
        init_time = time.time()

        while(time.time() - init_time < time):
            msg.linear.x = linear_x
            msg.angular.z = angular_z
            pub.publish(msg)
            rate.sleep()

    def run(pub, rate, msg):

        run_command(1640, 66, 2)

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

