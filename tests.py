# -*- coding: utf-8 -*-

import unittest
from BotDraw import *

class TestStringMethods(unittest.TestCase):
    def test_Bot__testConstruction(self):
			bot = Bot()
			self.assertTrue(bot.x == 0)
			self.assertTrue(bot.y == 0)
			self.assertTrue(bot.z == 0)
			self.assertTrue(bot.angle == 0)

    def test_Bot__drawBoxAt(self):
			bot = Bot()
			bot.drawBoxAt(3,3,3,1,2,3)
			elements = bot.getElements()
		
			self.assertTrue(elements[0]["type"] == "box")

    def test_Bot__drawBoxAt__failOnBadWidth(self):
			bot = Bot()
			with self.assertRaises(Exception) as context:
				bot.drawBoxAt("cat",3,3,1,2,3)

    def test_Bot__drawBoxAt__failOnBadHeight(self):
			bot = Bot()
			with self.assertRaises(Exception) as context:
				bot.drawBoxAt(3.12,"cat",3,1,2,3)

    def test_Bot__drawBoxAt__failOnBadDepth(self):
			bot = Bot()
			with self.assertRaises(Exception) as context:
				bot.drawBoxAt(3.12,3,"cat",1,2,3)
			

    def test_Bot__drawBoxAt__failOnBadX(self):
			bot = Bot()
			with self.assertRaises(Exception) as context:
				bot.drawBoxAt(3.12,3,3,"bad",2,3)

    def test_Bot__drawBoxAt__failOnBadYself(self):
			bot = Bot()
			with self.assertRaises(Exception) as context:
				bot.drawBoxAt(3.12,3,3,1,"bad",3)

    def test_Bot__drawBoxAt__failOnBadZ(self):
			bot = Bot()
			with self.assertRaises(Exception) as context:
				bot.drawBoxAt(3.12,3,3,1,2,"bad")


    def test_Bot__drawBox(self):
			bot = Bot()
			bot.drawBox(4,5,6)
			elements = bot.getElements()
			
			self.assertTrue(elements[0]["type"] == "box")
			self.assertTrue(elements[0]["width"] == 4)
			self.assertTrue(elements[0]["height"] == 5)
			self.assertTrue(elements[0]["depth"] == 6)

    def test_Bot__drawBox__FailOnBadWidth(self):
			bot = Bot()

			with self.assertRaises(Exception) as context:
				bot.drawBox("bad",5,6)

    def test_Bot__drawSphere(self):
			bot = Bot()
			bot.drawSphere(4)
			elements = bot.getElements()
			
			self.assertTrue(elements[0]["type"] == "sphere")
			self.assertTrue(elements[0]["radius"] == 4)
	
    def test_Bot__drawSphereAt(self):
			bot = Bot()
			bot.drawSphereAt(4,1,2,3)
			elements = bot.getElements()
			
			self.assertTrue(elements[0]["type"] == "sphere")
			self.assertTrue(elements[0]["radius"] == 4)
			self.assertTrue(elements[0]["x"] == 1)
			self.assertTrue(elements[0]["y"] == 2)
			self.assertTrue(elements[0]["z"] == 3)

    def test_Bot__drawObjFile(self):
			bot = Bot()
			scale = 0.25
			rotation = "0 0 0"
			model_name = "thing1"
			bot.drawObjFile(scale, rotation, model_name)
			
			elements = bot.getElements()
			
			self.assertTrue(elements[0]["type"] == "obj-model")
			self.assertTrue(elements[0]["scale"] == scale)
			self.assertTrue(elements[0]["rotation"] == rotation)
			self.assertTrue(elements[0]["model_name"] == model_name)


    def test_Bot__drawObjFile__FailWithBadRotation(self):
			bot = Bot()
			scale = 0.25
			rotation = "bad"
			model_name = "thing1"

			with self.assertRaises(Exception) as context:
				bot.drawObjFile(scale, rotation, model_name)

    def test_Bot__drawObjFile__FailWithBadRotation1(self):
			bot = Bot()
			scale = 0.25
			rotation = "bad 0 0"
			model_name = "thing1"

			with self.assertRaises(Exception) as context:
				bot.drawObjFile(scale, rotation, model_name)

    def test_Bot__drawObjFile__FailWithBadRotation2(self):
			bot = Bot()
			scale = 0.25
			rotation = "0 bad 0"
			model_name = "thing1"

			with self.assertRaises(Exception) as context:
				bot.drawObjFile(scale, rotation, model_name)

    def test_Bot__drawObjFile__FailWithBadRotation3(self):
			bot = Bot()
			scale = 0.25
			rotation = "0 0 bad"
			model_name = "thing1"

			with self.assertRaises(Exception) as context:
				bot.drawObjFile(scale, rotation, model_name)

    def test_Bot__drawObjFile__FailWithBadRotation4(self):
			bot = Bot()
			scale = 0.25
			rotation = 3.14
			model_name = "thing1"

			with self.assertRaises(Exception) as context:
				bot.drawObjFile(scale, rotation, model_name)




    def test_Bot__drawImageFile(self):
			bot = Bot()
			scale = 0.25
			rotation = "0 0 0"
			image_name = "mario"
			bot.drawImageFile(scale, rotation, image_name)
			
			elements = bot.getElements()
			
			self.assertTrue(elements[0]["type"] == "image")
			self.assertTrue(elements[0]["scale"] == scale)
			self.assertTrue(elements[0]["rotation"] == rotation)
			self.assertTrue(elements[0]["image_name"] == image_name)

		

    def test_Bot__moveUp(self):
			bot = Bot()		
			bot.moveUp(5)
			self.assertTrue(bot.y == 5)

	
    def test_Bot__moveLeft(self):
			bot = Bot()
			bot.moveLeft(5)
			self.assertTrue(bot.z == -5)

    def test_SceneMaker__Save(self):
			scene = SceneMaker()
			
			bot = Bot()
			bot.drawBox(1,1,1)
			bot.moveUp(2)
			bot.drawBox(1,1,1)
			bot.moveUp(2)
			bot.drawBox(1,1,1)
			bot.moveUp(2)
			elements = bot.getElements()

			scene.Save(elements,"index.html")

if __name__ == '__main__':
    unittest.main()
