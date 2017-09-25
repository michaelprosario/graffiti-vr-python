from BotDraw import *

bot = Bot()

bot.saveLocation("start")


scale = 0.25
rotation = "-90 0 0"
model_name = "garden"
bot.drawObjFile(scale, rotation, model_name)



bot.moveUp(30)
bot.drawImageFile(20,"0 90 0", "mario")



#======================================================================

sceneMaker = SceneMaker()
sceneMaker.Save(bot.getElements(),"index.html")
print("Scene created.")

