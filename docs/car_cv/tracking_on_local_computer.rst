Setup Opencv and run tracking algorithm on local computer
=========================================================

In this section we install opencv on Ubuntu and implement multi-object tracking using built-in algorithm. 

Setup
~~~~~

First we need to setup opencv environment in ubuntu. 

**If you are running ubuntu 18.04, then do the following**

First we install pip3:

.. code:: bash

    sudo apt-get install python3-pip

then install libopencv-dev:

.. code:: bash

    sudo apt-get install libopencv-dev

then install opencv-python as follows:

.. code:: bash

    sudo pip3 install opencv-python

If you have reached this point, you can verify your installation in terminal and check the version as follows:

.. code:: bash

    $ python
    Python 2.7.15+ (default, Nov 27 2018, 23:36:35) 
    [GCC 7.3.0] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import cv2
    >>> cv2.__version__
    >>> '4.1.0'

Multi-object tracking algorithm in opencv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's make a new directory under techx19 for cv-related code(you may need to change the path to go into the directory you want):

.. code:: bash

    cd ~/catkin_ws/src/techx2019/script
    mkdir cv_local
    cd cv_local
    touch cv_multi_test.py
    gedit cv_multi_test.py

Then copy the following code and save it.

.. code:: python

	from __future__ import print_function
	import sys
	import cv2
	from random import randint
	 
	trackerTypes = ['BOOSTING', 'MIL', 'KCF','TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
	 
	def createTrackerByName(trackerType):
	  # Create a tracker based on tracker name
	  if trackerType == trackerTypes[0]:
	    tracker = cv2.TrackerBoosting_create()
	  elif trackerType == trackerTypes[1]: 
	    tracker = cv2.TrackerMIL_create()
	  elif trackerType == trackerTypes[2]:
	    tracker = cv2.TrackerKCF_create()
	  elif trackerType == trackerTypes[3]:
	    tracker = cv2.TrackerTLD_create()
	  elif trackerType == trackerTypes[4]:
	    tracker = cv2.TrackerMedianFlow_create()
	  elif trackerType == trackerTypes[5]:
	    tracker = cv2.TrackerGOTURN_create()
	  elif trackerType == trackerTypes[6]:
	    tracker = cv2.TrackerMOSSE_create()
	  elif trackerType == trackerTypes[7]:
	    tracker = cv2.TrackerCSRT_create()
	  else:
	    tracker = None
	    print('Incorrect tracker name')
	    print('Available trackers are:')
	    for t in trackerTypes:
	      print(t)
	     
	  return tracker

	# Create a video capture object to read videos
	cap = cv2.VideoCapture(0)
	 
	# Read first frame
	success, frame = cap.read()
	# quit if unable to read the video file
	if not success:
	  print('Failed to read video')
	  sys.exit(1)

	## Select boxes
	bboxes = []
	colors = [] 
	 
	# OpenCV's selectROI function doesn't work for selecting multiple objects in Python
	# So we will call this function in a loop till we are done selecting all objects
	while True:
	  # draw bounding boxes over objects
	  # selectROI's default behaviour is to draw box starting from the center
	  # when fromCenter is set to false, you can draw box starting from top left corner
	  bbox = cv2.selectROI('MultiTracker', frame)
	  bboxes.append(bbox)
	  colors.append((randint(0, 255), randint(0, 255), randint(0, 255)))
	  print("Press q to quit selecting boxes and start tracking")
	  print("Press any other key to select next object")
	  k = cv2.waitKey(0) & 0xFF
	  if (k == 113):  # q is pressed
	    break
	 
	print('Selected bounding boxes {}'.format(bboxes))

	# Specify the tracker type
	trackerType = "CSRT"

	# Create MultiTracker object
	multiTracker = cv2.MultiTracker_create()

	# Initialize MultiTracker
	for bbox in bboxes:
	  multiTracker.add(createTrackerByName(trackerType), frame, bbox)

	# Process video and track objects
	while cap.isOpened():
	  success, frame = cap.read()
	  if not success:
	    break

	  # get updated location of objects in subsequent frames
	  success, boxes = multiTracker.update(frame)

	  # draw tracked objects
	  for i, newbox in enumerate(boxes):
	    p1 = (int(newbox[0]), int(newbox[1]))
	    p2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))
	    cv2.rectangle(frame, p1, p2, colors[i], 2, 1)

	  # show frame
	  cv2.imshow('MultiTracker', frame)


	  # quit on ESC button
	  if cv2.waitKey(1) & 0xFF == 27:  # Esc pressed
	    break

Save the file, go back to terminal and excute the program:

.. code:: bash

	python cv_multi_test.py

follow the instruction in terminal, and you should be able to track multiple objects.

.. image:: video/multi_tracking.gif
   :width: 1200
