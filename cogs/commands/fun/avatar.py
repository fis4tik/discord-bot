import discord
from discord.ext import commands

class Avatar(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot


    @commands.slash_command(description="Получить аватар пользователя")
    async def avatar(self, ctx: discord.ApplicationContext, user: discord.Option(discord.Member, "Укажите пользователя")): # type: ignore
        if user:
            avatar = user.avatar.url
        else:
            avatar = user.default_avatar.url
        embed = discord.Embed(author=discord.EmbedAuthor(name=f"Аватар пользователя {user.display_name}", icon_url=ctx.author.avatar.url),color=discord.Color.gold(), image=discord.EmbedMedia(url=avatar))
        embed.set_footer(text="ARZ Moderator", icon_url=ctx.me.avatar.url)
        button = discord.ui.Button(label="Ссылка", url=avatar)
        view = discord.ui.View(button)
        await ctx.respond(embed=embed, view=view, ephemeral=True)




def setup(bot):
    bot.add_cog(Avatar(bot))
