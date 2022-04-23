import os 

from dotenv import load_dotenv
from discord.ext import commands 

default_intents = discord.Intents.default()
default_intents.members = True 
client = discord.Client(intents=default_intents)


load_dotenv(dotenv_path="config")
bot = commands.Bot(command_prefix="!")

#connexion du Bot
class DocBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/")

    async def on_ready(self):
        print(f"{self.user.display_name} est connecté.")

    #reponse d'un bot
    async def on_message(self, message):
        if message.content.lower() == "salut":
            await message.channel.send("salut cava?") 
    
    #acceil d'un nouveau membre
    async def on_member_join(self, member):
    general_channel: discord.Textchannel = client.get_channel(958696044227612745)
    await general_channel.send(content=f"bienvenue sur le serveur {member.display_name} ")
    

    #supression d'un message
    async def delete(ctx, number_of_message: int):
    messages = await ctx.channel.history(limit=number_of_message + 1).flatten()
     
    for each_message in messages:
            await each_message.delete()


        



bot = DocBot()
bot.run(os.getenv("TOKEN"))