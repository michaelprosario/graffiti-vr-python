# Graffiti VR for Python

Graffiti VR for Python, a playful way of learning python, enables you to build 3D VR experiences using the Python programming language.  

This project uses a JavaScript framework called AFrame to build 3D content in your browser or mobile phone browser. The display engine supports major VR platforms including Google Cardboard, Vive, and Oculus. (Thank you AFrame community!)

In Graffiti VR, you command a small bot who can travel in 3D space. The robot can place boxes, spheres, images, and other 3D shapes. This tool borrows ideas from popular code education tools like Logo, code.org, ScriptCraft by Walter Higgins.

You can review a sample scene here: [https://dark-bat.glitch.me/]

You can use the keys WASD to move around the scene.

# Bot Draw methods

In order to draw, you start by creating an instance of the bot. The bot object has additional methods for drawing, turning, or moving.

# Moving and turning:

* moveUp(steps) – Move the bot upward a few steps
* forward(steps) – Move bot forward a few steps
* moveLeft(steps) – Move bot left
* moveRight(steps) – Move bot right
* setAngle(degrees) – Set angle of direction for the robot. Enter * direction in degrees
* getAngle() – Get current angle for the robot.
* turn(angle) – Turn the robot a few degrees.

# Drawing stuff:

* drawBoxAt(width,height,depth,x,y,z) – Draw box at a particular location.
* drawBox(width,height,depth) – Draw box at current robot location.
* drawSphere(radius) – Draw sphere at current robot location.
* drawSphereAt(radius,x,y,z) – Draw sphere at particular location
* drawCone(radius,height)
* drawCylinder(radius,height)
* drawImageAt(strPath,width, height, x,y,z) – Draw image at particular location. The path should be a fully qualified path to a valid web image.
* drawImage(strPath,width,height) – Draw image at bot location. The path should be a fully qualified path to a valid web image.

# Remember locations, Return to locations

* saveLocation(locationName) – Store bot location and give it a name.
* moveToLocation(locationName) – Return to location by name

# Change colors:

* bot.drawColor = “red”


# Install instructions

1. Install Python 2.7
2. Install pip
3. Execute the following:

pip install Jinja2

4. Download Graffiti VR Python from here:[https://github.com/michaelprosario/graffiti-vr-python/archive/master.zip]

5. Extract the zip file.


 
