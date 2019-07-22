Edit Hosts file
===============

Check your Hosts file
----------------------

.. code:: bash

    cat /etc/hosts

The returned result should be **something like this**:

.. code:: bash

    127.0.0.1	localhost
    127.0.1.1	chris-Inspiron-7373

    # The following lines are desirable for IPv6 capable hosts
    ::1     ip6-localhost ip6-loopback
    fe00::0 ip6-localnet
    ff00::0 ip6-mcastprefix
    ff02::1 ip6-allnodes
    ff02::2 ip6-allrouters

Edit the file
--------------

open the file editor

.. code:: bash

    sudo gedit /etc/hosts

Copy and paste the following code to the end of the file:

.. code:: bash

    192.168.50.101   tianbot-01
    192.168.50.102   tianbot-02
    192.168.50.103   tianbot-03
    192.168.50.104   tianbot-04
    192.168.50.105   tianbot-05
    192.168.50.106   tianbot-06
    192.168.50.107   tianbot-07
    192.168.50.108   tianbot-08
    192.168.50.109   tianbot-09
    192.168.50.110   tianbot-10

make sure that your file is looking **something like this** right now:
**Note: Don't copy paste the following code.**

.. code:: bash

    127.0.0.1	localhost
    127.0.1.1	chris-Inspiron-7373

    # The following lines are desirable for IPv6 capable hosts
    ::1     ip6-localhost ip6-loopback
    fe00::0 ip6-localnet
    ff00::0 ip6-mcastprefix
    ff02::1 ip6-allnodes
    ff02::2 ip6-allrouters    

    192.168.50.101   tianbot-01
    192.168.50.102   tianbot-02
    192.168.50.103   tianbot-03
    192.168.50.104   tianbot-04
    192.168.50.105   tianbot-05
    192.168.50.106   tianbot-06
    192.168.50.107   tianbot-07
    192.168.50.108   tianbot-08
    192.168.50.109   tianbot-09
    192.168.50.110   tianbot-10

Save the file and close it