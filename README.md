# Motion-Detection-Security-App

Utilizing OpenCV, Pandas, Bokeh, etc

Status - Complete

# ABOUT
This app detects moving objects within a camera's frame, and boxes them all within a green rectangle while constantly tracking their movements. Moreover, all movements along with their intervals (how long the object was moving for) are recorded and filtered into a dataFrame. Finally, such data is then plotted onto a UI for users to monitor (in graph form). When hovering over areas of movements on the graph, the exact start and end times pop up. I currently have this program connected to a Raspberry Pi and running at my house.

# INSTALLING

1- git clone (https/ssh) depending on your permissions
2- cd to directory
3- pip install bokeh
4- pip install opencv-python
5- python plot.py
