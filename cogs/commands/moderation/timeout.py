import discord
from discord.ext import commands
import datetime

class Timeout(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.slash_command(description="Выдать пользователю тайм-аут", name="time-out")
    @commands.has_permissions(moderate_members=True)
    async def t_timeout(self, ctx, member: discord.Member, duration: int):
        try:               
            await member.timeout_for(duration=datetime.timedelta(minutes=duration))
            await ctx.send(f"{member.mention} был помещен в тайм-аут на {duration} минут.")
        except Exception as e:
            await ctx.send(f"Не удалось поместить {member.mention} в тайм-аут. Ошибка: {e}")


def setup(bot):
    bot.add_cog(Timeout(bot))