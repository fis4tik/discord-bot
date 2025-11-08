import discord
from discord.ext import commands
import random

class Guess(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot

    @commands.slash_command(name="угадай", description="Игра, где надо угадать число (Автор идеи: Mideev)")
    async def guess(self, ctx: discord.ApplicationContext, число: discord.Option(int, description="Введите число", min_value=1, max_value=9999)): # type: ignore
        number = random.randint(1, 9999)
        if число == number:
            embed = discord.Embed(title="Информация об выпавшем числе:", 
                                  description=f"Загаданное число: **{number}**\nВаше число: **{число}**\n\n**{number}** = **{число}**. Поздравляем!",
                                  
                                  color=0x20e672)
            await ctx.respond(embed=embed)
        elif число != number:
            embed = discord.Embed(title="Информация об выпавшем числе:", 
                                  description=f"Загаданное число: **{number}**\nВаше число: **{число}**\n\n**{number}** ≠ **{число}**",
                                  
                                  color=0xd4210d)
            await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Guess(bot))
