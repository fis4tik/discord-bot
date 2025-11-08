import discord
from discord.ext import commands

class InviteInfo(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.slash_command()
    async def inviteinfo(self, ctx, invite_code):
        try:
            invite = await self.bot.fetch_invite(invite_code)
            emd = discord.Embed(author=discord.EmbedAuthor(name=f"{invite.guild.name} (ID: {invite.guild.id})", url=invite_code), thumbnail=discord.EmbedMedia(url=invite.guild.icon.url))
            emd.add_field(name="Уровень проверки", value=invite.guild.verification_level)
            emd.add_field(name="Канал для приглашений", value=f"`{invite.channel.name} (ID: {invite.channel.id})`", inline=True)
            emd.set_footer(text=f"{ctx.author.name} (ID: {ctx.author.id})", icon_url=ctx.author.avatar.url)
            await ctx.respond(embed=emd)
        except discord.errors.NotFound:
            await ctx.respond('Приглашение не найдено.')

def setup(bot):
    bot.add_cog(InviteInfo(bot))