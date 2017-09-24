from BotDraw import *

bot = Bot()

bot.saveLocation("start")






scale = 0.25
rotation = "-90 0 0"
model_name = "pokemon2"
bot.drawObjFile(scale, rotation, model_name)

bot.moveLeft(-40)

scale = 0.25
rotation = "-90 -180 0"
model_name = "pokemon3"
bot.drawObjFile(scale, rotation, model_name)


#======================================================================

sceneMaker = SceneMaker()
sceneMaker.Save(bot.getElements(),"index.html")
print("Scene created.")

