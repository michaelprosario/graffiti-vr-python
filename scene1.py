from BotDraw import *

bot = Bot()

bot.saveLocation("start")




#======================================================================

bot.moveToLocation("start")
for x in range(0,10):
	bot.drawBox(1,1,1)
	bot.moveUp(2)

#======================================================================

bot.moveToLocation("start")
bot.moveRight(10)
for x in range(0,50):
	bot.drawBox(5,0.25,5)
	bot.moveUp(0.25)
	bot.turn(5)

#======================================================================

bot.moveToLocation("start")
bot.moveRight(20)
for y in range(0,12):
	if y % 2 == 0:
		bot.color="red"
	else:
		bot.color="green"

	bot.drawSphere(1)
	bot.moveUp(1)

#======================================================================

bot.moveToLocation("start")
bot.moveRight(30)

for x in range(0,20):	
	bot.drawBox(1,x,1)
	bot.moveRight(2)



bot.moveRight(100)
scale = 0.25
rotation = "-90 0 0"
model_name = "thing1"
bot.drawObjFile(scale, rotation, model_name)


#======================================================================

sceneMaker = SceneMaker()
sceneMaker.Save(bot.getElements(),"index.html")
print("Scene created.")

