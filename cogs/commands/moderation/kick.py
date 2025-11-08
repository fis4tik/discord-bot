import discord
from discord.ext import commands
import datetime

class KickCommand(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot

    @commands.slash_command(description="Кикнуть пользователя")
    @commands.guild_only()
    async def kick(self, ctx: discord.ApplicationContext, member: discord.Option(discord.Member, "Пользователь (упоминание или id)"), reason: discord.Option(str, "Введите причину", min_lenght=8, max_lenght=120, required=False)): # type: ignore

        if reason is not None:
            embed = discord.Embed(description=f"Пользователь {member.mention} кикнут с сервера **{ctx.guild.name}**!", color=discord.Color.red())
            
            # await user.kick(reason=reason)
            await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(description=f"Пользователь {member.mention} кикнут с сервера **{ctx.guild.name}**!", color=discord.Color.red())
            # await user.kick()
            await ctx.respond(embed=embed)

        log_channel = self.bot.get_channel(1235617006225461258)
        timestamp = f'<t:{int(datetime.datetime.now().timestamp())}>'

        emd = discord.Embed(title="Пользователь кикнут с сервера", 
                            description=f"**Кикнут:** {member.mention}\n**Кикнул:** {ctx.author.mention}\n**Время:** {timestamp}",
                            color=0xDC143C)
        
        await log_channel.send(embed=emd)

        




def setup(bot):
    bot.add_cog(KickCommand(bot))    