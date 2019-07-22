Debugging Tools
================

rqt
---

rqt is a software framework of ROS that implements the various GUI tools in the form of plugins. 
One can run all the existing GUI tools as dockable windows within rqt! 
The tools can still run in a traditional standalone method, but rqt makes it easier to manage all the various windows on the screen at one moment.

.. code:: bash

    rqt


rqt_graph
----------

rqt_graph provides a GUI plugin for visualizing the ROS computation graph.
Its components are made generic so that other packages where you want to achieve graph representation can depend upon this pkg

.. code:: bash

    rqt_graph

rqt_tf_tree
------------

rqt_tf_tree provides a GUI plugin for visualizing the ROS TF frame tree.

.. code:: bash

    rqt_tf_tree

rostopic echo
--------------

rostopic echo topicname returns the messages being sent from the ROS master about a specific topic, topicname. To stop returning messages, press Ctrl+C. rostopic info topicname returns the message type, publishers, and subscribers for a specific topic, topicname. rostopic type topicname returns the message type for a specific topic.

.. code:: bash

    rostopic echo <topic name>

nmap
----

.. code:: bash

    nmap -sP 192.168.50.1/24