from BotDraw import *

bot = Bot()

bot.saveLocation("start")





#======================================================================

bot.moveToLocation("start")
bot.color = "purple"
for x in range(0,10):
	bot.drawBox(1,0.1,1)
	bot.moveUp(0.1)
	bot.turn(5)

sceneMaker = SceneMaker()
sceneMaker.template_to_load = "template_ar.html"
sceneMaker.Save(bot.getElements(),"index.html")
print("Scene created.")

