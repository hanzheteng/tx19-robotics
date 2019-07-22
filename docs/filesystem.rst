ROS Filesystem
==============

Using rospack
-------------

rospack allows you to get information about packages. 
In this tutorial, we are only going to cover the find option, which returns the path to package.

rospack命令可以用来查找包的路径

Usage:

.. code:: bash

    rospack find [package_name]

Example:

.. code:: bash

    rospack find techx2019

Using roscd
-----------

It allows you to change directory (cd) directly to a package or a stack.

roscd命令可以直接像cd一样进入目录，不同的是roscd可以直接定位到ros包

Usage:

.. code:: bash

    roscd [locationname[/subdir]]

Example:

.. code:: bash

    roscd techx2019

**Note: roscd will access the directory output by the rospack find command**

Using rosls
-----------

It allows you to ls directly in a package by name rather than by absolute path.

同roscd和cd的关系

Usage:

.. code:: bash

    rosls [locationname[/subdir]]

Example:

.. code:: bash

    rosls techx2019

**Tab Completion(Tab键自动补全)**
-------------------------------------------

Example:

.. code:: bash

    roscd tec

Press the Tab right now, you will automatically get the command

.. code:: bash

    roscd techx2019


