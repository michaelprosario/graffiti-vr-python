# -*- coding: utf-8 -*-

import math
import numbers
import decimal

from jinja2 import *

class SceneMaker:
	def __init__(self):
		self.template_to_load = 'template1.html'

	def Save(self, objElements, strFilename):
		env = Environment(
		    loader=PackageLoader('tests', 'templates')
		)

		template = env.get_template(self.template_to_load)
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

	def isString(self, k):
		return isinstance(k, basestring)

	def isFloat(self,value):
		try:
			float(value)
			return True
		except:
			return False

	
	def checkWidthHeightDepth(self, width, height, depth):
		if not isinstance(width, numbers.Number):		
			raise Exception("Width is not a number.")
		if not isinstance(height, numbers.Number):		
			raise Exception("Height is not a number.")
		if not isinstance(depth, numbers.Number):		
			raise Exception("Depth is not a number.")

	def checkXYZ(self, x, y, z):
		if not isinstance(x, numbers.Number):		
			raise Exception("x is not a number.")
		if not isinstance(y, numbers.Number):		
			raise Exception("y is not a number.")
		if not isinstance(z, numbers.Number):		
			raise Exception("z is not a number.")

	def drawBoxAt(self,width,height,depth,x,y,z):
		self.checkWidthHeightDepth( width, height, depth)
		self.checkXYZ(x,y,z)

		element = {"width": width, "height": height, "depth": depth, 
				"x": x, "y":y, "z": z,
				"rotationx": 0, "rotationy":0, "rotationz": 0,
				"type": "box", "color": self.color	 
				}
		self.elements.append(element)

	def drawBox(self,width,height,depth):
		self.checkWidthHeightDepth( width, height, depth)

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
		if not isinstance(radius, numbers.Number):		
			raise Exception("Radius is not a number.")

		botX = self.x
		botY = self.y
		botZ = self.z
		element = {"radius": radius,
				"x": botX, "y": botY, "z": botZ,
				"type": "sphere", "color": self.color	 
				}
		self.elements.append(element)

	def raiseRotationError(self):
		raise Exception("Rotation should be a string of 3 numbers separated by spaces.  Example: '0 90 -90'")

	def checkRotation(self, rotation):
		if not self.isString(rotation):
			self.raiseRotationError()

		parts = rotation.split(" ")
		if len(parts) != 3:
			self.raiseRotationError()
		
		if not self.isFloat(parts[0]):
			self.raiseRotationError()
		
		if not self.isFloat(parts[1]):
			self.raiseRotationError()

		if not self.isFloat(parts[2]):
			self.raiseRotationError()
		



	def drawObjFile(self, scale, rotation, model_name):
		if not isinstance(scale, numbers.Number):		
			raise Exception("Scale is not a number.")

		self.checkRotation(rotation)
		


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
		if not isinstance(scale, numbers.Number):		
			raise Exception("Scale is not a number.")

		self.checkRotation(rotation)


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
		if not isinstance(radius, numbers.Number):		
			raise Exception("radius is not a number.")

		self.checkXYZ(x,y,z)

		element = {"radius": radius,
				"x": x, "y": y, "z": z,
				"type": "sphere", "color": self.color	 
				}
		self.elements.append(element)

	def moveUp(self,steps):
		if not isinstance(steps, numbers.Number):		
			raise Exception("steps is not a number.")


		self.y += steps
		
	def moveLeft(self,steps):
		if not isinstance(steps, numbers.Number):		
			raise Exception("steps is not a number.")

		deltaX = steps * math.cos(self.angle - (math.pi/2));
		deltaZ = steps * math.sin(self.angle- (math.pi/2));

		self.x += deltaX
		self.z += deltaZ

	def moveRight(self,steps):
		if not isinstance(steps, numbers.Number):		
			raise Exception("steps is not a number.")

		self.moveLeft(-1*steps)


	def getPosition(self):
		position = { "x" : self.x, "y": self.y, "z": self.z }
		return position
		
	def getElements(self):
		return self.elements;

	def getAngle(self):
		return 180.0 * self.angle/math.pi

	def setAngle(self, degrees):
		if not isinstance(degrees, numbers.Number):		
			raise Exception("degrees is not a number.")


		self.angle = degrees*math.pi/180.0

	def turn(self,angle):
		if not isinstance(angle, numbers.Number):		
			raise Exception("angle is not a number.")


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
		if not isinstance(steps, numbers.Number):		
			raise Exception("steps is not a number.")
		
		deltaX = steps * math.cos(self.angle)
		deltaZ = steps * math.sin(self.angle)
		self.x += deltaX
		self.z += deltaZ
		







