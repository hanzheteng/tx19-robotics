Installing ROS 
==============

**Your configuration must be either one from the following:**

* System: Ubuntu 16.04
* or
* System: Ubuntu 18.04

**If you are using Ubuntu 16.04, you must install ROS Kinetic**  

**如果你的系统版本是Ubuntu 16.04, 一定要安装ROS Kinetic**

**If you are using Ubuntu 18.04, you must install ROS Melodic**

**如果你的系统版本是Ubuntu 18.04, 一定要安装ROS Melodic**

**In this document, we are using Ubuntu 18.04 + ROS Melodic, but if you are using Ubuntu 16.04, please change
all the Melodic into Kinetic**

**在这个文档中，我们使用的是Ubuntu 18.04 + ROS Melodic的配置,如果你使用的是Ubuntu 16.04也没有关系,
只需要将代码中的Melodic名称改为Kinetic即可使用**

Setup sources.list
---------------------

以下两端代码只需要运行 **其中一段** ，推荐运行第一段

The Tsinghua University Mirror Source (**Recommended**):

.. code:: bash 

    sudo sh -c '. /etc/lsb-release && echo "deb http://mirrors.tuna.tsinghua.edu.cn/ros/ubuntu/ $DISTRIB_CODENAME main" > /etc/apt/sources.list.d/ros-latest.list'

or you can use the default source:

.. code:: bash 

    sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

Setup your keys
------------------

Run the following code:

.. code:: bash

    sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

可能运行时间过长，可以耐心等待

如果报错，可以等一段时间再运行

Update Package Index
--------------------

.. code:: bash

    sudo apt-get update

**It may takes some time**

Install ROS
-----------

请在下面两端代码中，根据你的操作系统，**仅选择一段运行**

* **Ubuntu 18.04:**
    .. code:: bash

        sudo apt-get install ros-melodic-desktop-full

* **Ubuntu 16.04:**
    .. code:: bash

        sudo apt-get install ros-kinetic-desktop-full

Initialize Rosdep
-----------------

Before you can use ROS, you will need to initialize rosdep.

.. code:: bash

    sudo rosdep init
    rosdep update

Environment Setup
-----------------

* **Ubuntu 18.04:**
    .. code:: bash

        echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
        source ~/.bashrc

* **Ubuntu 16.04:**
    .. code:: bash

        echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
        source ~/.bashrc

Install More Dependencies
-------------------------

.. code:: bash

    sudo apt install python-rosinstall python-rosinstall-generator python-wstool build-essential

