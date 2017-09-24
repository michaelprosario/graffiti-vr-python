# -*- coding: utf-8 -*-

import math
from jinja2 import *

class SceneMaker:
	def Save(self, objElements, strFilename):
		env = Environment(
		    loader=PackageLoader('tests', 'templates')
		)

		template = env.get_template('template1.html')
		template_output = template.render(elements = objElements )

		file = open(strFilename,"w")  
		file.write(template_output)
		file.close() 



class Bot:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.z = 0 
		self.angle = 0
		self.elements = []
		self.locations = {}
		self.color = "tomato"
		

	def drawBoxAt(self,width,height,depth,x,y,z):
		element = {"width": width, "height": height, "depth": depth, 
				"x": x, "y":y, "z": z,
				"rotationx": 0, "rotationy":0, "rotationz": 0,
				"type": "box", "color": self.color	 
				}
		self.elements.append(element)

	def drawBox(self,width,height,depth):

		posx = self.x - (width/2.0)
		posy = self.y
		posz = self.z + (depth/2.0)


		element = {"width": width, "height": height, "depth": depth, 
				"x": posx, "y": posy, "z": posz,
				"rotationx": 0, "rotationy":self.getAngle(), "rotationz": 0,
				"type": "box", "color": self.color	 
				}
		self.elements.append(element)

	def drawSphere(self,radius):
		botX = self.x
		botY = self.y
		botZ = self.z
		element = {"radius": radius,
				"x": botX, "y": botY, "z": botZ,
				"type": "sphere", "color": self.color	 
				}
		self.elements.append(element)

	def drawObjFile(self, scale, rotation, model_name):
		botX = self.x
		botY = self.y
		botZ = self.z
		element = {"model_name": model_name,
				"x": botX, 
				"y": botY, 
				"z": botZ,
				"type": "obj-model",
				"rotation" : rotation, 
				"scale" : scale
				}

		self.elements.append(element)
		
	def drawImageFile(self, scale, rotation, image_name):
		botX = self.x
		botY = self.y
		botZ = self.z
		element = {
			    "image_name": image_name,
				"x": botX, 
				"y": botY, 
				"z": botZ,
				"type": "image",
				"rotation" : rotation, 
				"scale" : scale
				}

		self.elements.append(element)

				


	def drawSphereAt(self,radius,x,y,z):
		element = {"radius": radius,
				"x": x, "y": y, "z": z,
				"type": "sphere", "color": self.color	 
				}
		self.elements.append(element)

	def moveUp(self,steps):
		self.y += steps
		
	def moveLeft(self,steps):
		deltaX = steps * math.cos(self.angle - (math.pi/2));
		deltaZ = steps * math.sin(self.angle- (math.pi/2));

		self.x += deltaX
		self.z += deltaZ

	def moveRight(self,steps):
		self.moveLeft(-1*steps)


	def getPosition(self):
		position = { "x" : self.x, "y": self.y, "z": self.z }
		return position
		
	def getElements(self):
		return self.elements;

	def getAngle(self):
		return 180.0 * self.angle/math.pi

	def setAngle(self, degrees):
		self.angle = degrees*math.pi/180.0

	def turn(self,angle):
		currentAngle = self.getAngle()
		self.setAngle(currentAngle + angle)
	
	def moveToLocation(self,locationName):
		point = self.locations[locationName]
		self.x = point["x"]
		self.y = point["y"]
		self.z = point["z"]
		self.angle = point["angle"]

	def saveLocation(self,locationName):
		point = {"x": self.x, "y": self.y, "z": self.z, "angle": self.angle }
		self.locations[locationName] = point
		
	def forward(self, steps):
		deltaX = steps * math.sin(self.angle)
		deltaZ = steps * math.cos(self.angle)
		self.x += deltaX
		self.z += deltaZ
		







