# Graffiti VR for Python

Graffiti VR for Python, a playful way of learning python, enables you to build 3D VR experiences using the Python programming language.  

This project uses a JavaScript framework called AFrame to build 3D content in your browser or mobile phone browser. The display engine supports major VR platforms including Google Cardboard, Vive, and Oculus. (Thank you AFrame community!)

In Graffiti VR, you command a small bot who can travel in 3D space. The robot can place boxes, spheres, images, and other 3D shapes. This tool borrows ideas from popular code education tools like Logo, code.org, ScriptCraft by Walter Higgins.

You can review a sample scene here: https://dark-bat.glitch.me/

You can use the keys WASD to move around the scene.

Here's another sample scene:
https://noon-afterthought.glitch.me/sample1.html

Try to build python code to draw those structures.  If you want to see the solution, check out 'sample1.py' in this code repository. 

# Install instructions

1. Install Python 2.7
2. Install pip
3. Execute the following: pip install Jinja2
4. Download Graffiti VR Python from here:  https://github.com/michaelprosario/graffiti-vr-python/archive/master.zip
5. Extract the zip file.

# Drawing your first scene

* Open a terminal or command prompt.
* Navigate into the source folder. (cd graffiti-vr-python-master)
* Create a file called 'first_scene.py' using your favorite text editor.
* Enter the following code into first_scene.py:

from BotDraw import *

```python
# Create a bot
bot = Bot()

# Stores the bots current location and angle
bot.saveLocation("start")

# Bot draws boxes moving upward
for x in range(0,10):
	bot.drawBox(1,1,1)
	bot.moveUp(2)

# Move the bot back to start
bot.moveToLocation("start")

# Convert actions of bot to AFrame.io HTML file.  
sceneMaker = SceneMaker()
sceneMaker.Save(bot.getElements(),"index.html")
print("Scene created.")
```

* Execute the following: python first_scene.py
* The system should update index.html.
* Execute the following: python -m SimpleHTTPServer
* Python should start a small web server in your current directory.
* Open up FireFox or Google Chrome.
* Navigate to http://localhost:8000/

Sample output: https://noon-afterthought.glitch.me/

# Drawing a JPEG image

```python

# Scale the image by 20 times
scale_factor = 20

# Rotate the image about the y-axis 90 degrees
rotation = "0 90 0"

# Set the image to Mario
image = "mario" 
bot.drawImageFile(scale_factor,rotation, image)
```
# Drawing a 3D model file 

```python
scale = 0.25

#rotate the 3D model about the x-axis by -90
rotation = "-90 0 0"

# Note: All 3D model files should be in 'obj' format.   The 'obj' file and 'mtl' file should be located in the models folder.
model_name = "garden"
bot.drawObjFile(scale, rotation, model_name)
```
# Where can I learn more about AFrame HTML?

If you want to tweak the HTML in index.html, you are welcome to do so.   You can learn more about Aframe.io at https://aframe.io/docs/0.7.0/introduction/ .

# Bot Draw methods

In order to draw, you start by creating an instance of the bot. The bot object has additional methods for drawing, turning, or moving.

bot = Bot()

# Moving and turning:

* bot.moveUp(steps) – Move the bot upward a few steps
* bot.forward(steps) – Move bot forward a few steps
* bot.moveLeft(steps) – Move bot left
* bot.moveRight(steps) – Move bot right
* bot.setAngle(degrees) – Set angle of direction for the robot. Enter * direction in degrees
* bot.getAngle() – Get current angle for the robot.
* bot.turn(angle) – Turn the robot a few degrees.

# Drawing stuff:

* bot.drawBoxAt(width,height,depth,x,y,z) – Draw box at a particular location.
* bot.drawBox(width,height,depth) – Draw box at current robot location.
* bot.drawSphere(radius) – Draw sphere at current robot location.
* bot.drawSphereAt(radius,x,y,z) – Draw sphere at particular location

# Remember locations, Return to locations

* bot.saveLocation(locationName) – Store bot location and give it a name.
* bot.moveToLocation(locationName) – Return to location by name

# Change colors:

* bot.color = “red”






 
