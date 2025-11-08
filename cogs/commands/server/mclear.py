import discord
from discord.ext import commands

class Mclear(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.slash_command(description="Удалить сообщения")
    @commands.has_permissions(manage_messages=True)
    async def mclear(self, ctx: discord.ApplicationContext, 
                     amount: discord.Option(int, "Целое число", min_value=3, max_value=500),  # type: ignore
                     user: discord.Option(discord.Member, "Пользователь (упоминание или id)", required=False)):   # type: ignore

        def check(msg):
            return user is None or msg.author == user

        
        
        # Сначала отправляем сообщение об удалении
        embed = discord.Embed(author=discord.EmbedAuthor(name=ctx.author.display_name, icon_url=ctx.author.avatar.url), 
                              description=f"Удалено 0 сообщений", 
                              color=discord.Color.dark_theme())
        embed.set_footer(text="ARZ Moderator", icon_url=ctx.guild.me.avatar.url)
        

        # Затем удаляем сообщения
        deleted = await ctx.channel.purge(limit=amount, check=check)
        response_message = await ctx.respond(embed=embed, delete_after=10)
        # Обновляем сообщение об удалении
        embed.description = f"Удалено {len(deleted)} сообщений"
        await response_message.edit(embed=embed)

def setup(bot):
    bot.add_cog(Mclear(bot))