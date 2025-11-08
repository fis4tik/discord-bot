import discord
from discord.ext import commands
import os
import random
from PIL import Image
import io
import responses

class WIPcommands(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot






def setup(bot):
    bot.add_cog(WIPcommands(bot))