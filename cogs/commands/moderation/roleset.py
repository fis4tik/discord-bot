import discord
from discord.ext import commands
import datetime

class RoleSet(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot


    @commands.slash_command(name="role_set")
    async def role_add(self, ctx: discord.ApplicationContext, user: discord.Option(discord.Member, "Укажите пользователя"), role: discord.Option(discord.Role, "Укажите роль"), reason: discord.Option(str, "Введите причину", max_length=60)): # type: ignore
        if role.position >= ctx.guild.me.top_role.position:
            await ctx.respond("Данная роль стоит выше роли бота. Бот не имеет права выдать ее", ephemeral=True)
        else:
            await user.add_roles(role)
            
            if user.avatar.url:
                avatar = user.avatar.url
            else:
                avatar = user.default_avatar.url

            embed = discord.Embed(title="", description=f"{ctx.author.mention} выдал роль {role.mention} пользователю {user.mention}\n**Причина:** {reason}", timestamp=datetime.datetime.now(), color=0x00afff)
            embed.set_footer(text="ARZ Moderator", icon_url=ctx.guild.me.avatar.url)
            embed.set_thumbnail(url=avatar)
            await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(RoleSet(bot))