# Motion-Detection-Security-App

Utilizing OpenCV, Pandas, Bokeh, etc

Status - Complete

# ABOUT
This app detects moving objects within a camera's frame and boxes such objects in a green rectangle while tracking their movements. Moreover, all movements along with their intervals (how long the object was moving for) gets recorded and filtered into a dataFrame. Finally, such data is then plotted onto a UI for users to monitor in graph form. When, hovering over movement areas in the graph the exact start and end times pop up. Currently I have this program connected to a Raspberry Pi and running at my house.

# INSTALLING

1- git clone (https/ssh) depending on your permissions
2- cd to directory
3- pip install bokeh
4- pip install opencv-python
5- python plot.py
