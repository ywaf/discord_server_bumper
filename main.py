# Made By Leho | leho.dev | github.com/lehoooo
import time
import discum
from discum.utils.slash import SlashCommander

# MAKE SURE TO DM THE BOT ANYTHING BEFORE RUNNING FOR THE FIRST TIME

botid = "DISBOARD BOT ID HERE" # PUT DISBOARD BOT ID IN HERE
channelid = "CHANNEL ID HERE" #current channel id to send to
guildid = "GUILDID HERE" #current guild id to send to


bot = discum.Client(token="YOUR TOKEN HERE :)", log=False)

while True:
    print("Bumping...")
    slashCmds = bot.getSlashCommands(str(botid)).json()
    s = SlashCommander(slashCmds)
    a = s.get(["bump"])
    bot.triggerSlashCommand(str(botid), str(channelid), guildID=str(guildid), data=a)
    print("Bumped!")
    print("Waiting...")
    time.sleep(120 * 60)
