import discord
from discord.ext import commands
import datetime

class SetName(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.slash_command(name="set-name", description="Изменить никнейм пользователю")
    async def setname(self, ctx: discord.ApplicationContext, member: discord.Option(discord.Member, description="Пользователь (упоминание или id)"), name: discord.Option(str, "Новый никнейм")): # type: ignore
        await member.edit(nick=name)

        embed = discord.Embed(title="✅ | Никнейм успешно изменён", 
                            description=f"Модератор {ctx.author.mention} установил пользователю {member.mention} новый никнейм!", 
                            color=discord.Color.brand_green(),
                            timestamp=datetime.datetime.now(),
                            footer=discord.EmbedFooter(text="ARZ Moderator", icon_url=self.bot.user.avatar.url))

        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(SetName(bot))