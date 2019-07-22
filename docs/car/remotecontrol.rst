Using gamepad to control Racecar
========================================

Turn on the robot
~~~~~~~~~~~~~~~~~~

    * Turn on the battery

    * Turn on the ESC（电调）

**Note: make sure your gamepad's control mode's light is off and the mode is in X**

Connect the TianRacer WiFi
~~~~~~~~~~~~~~~~~~~~~~~~~~

WiFi SSID: TianRacer

Password: www.tianbot.com

Confirm your Racecar's IP address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**192.168.50.10X** where X is your team number

**注意，这里X是你的队伍编号！**

Example:

If your team number is 9, your Racecar's IP address should be **192.168.50.109**

Using SSH
~~~~~~~~~~

Open a terminal

.. code:: bash

    ssh -X tianbot@192.168.50.10X

**where X is your team number**

For example, if your team number is 9, you should

.. code:: bash

    ssh -X tianbot@192.168.50.109

Type in the password: **ros**

**Note: you will not see the password on the screen, because the password typing is
hidden in linux terminal**

Open Racecar Bringup launch file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the following code **ONLY IF** you have logged into your Racecar

**Don't** run the code on your laptop

.. code:: bash

    roslaunch racecar_bringup racecar_bringup.launch

