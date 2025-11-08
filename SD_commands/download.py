import discord
from discord.ext import commands


class DownloadMessages(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot

    @commands.slash_command(description="Скачивает ВСЕ сообщения с канала в файл")
    @commands.has_permissions(administrator = True)
    async def download_messages(self, ctx: discord.ApplicationContext, channel: discord.Option(discord.TextChannel, "Укажите канал")): # type: ignore
        channel_name = channel.name
        channel = discord.utils.get(ctx.guild.channels, name=channel_name)
        if channel:
            with open('messages.txt', 'w', encoding='utf-8') as file:
                async for message in channel.history(limit=None):
                    file.write(f"{message}")
            await ctx.respond("Подождите, информация собирается...")
            await ctx.send('Сообщения успешно скачаны и записаны в файл messages.txt', file=discord.File("messages.txt"))
        else:
            await ctx.respond('Канал не найден')






def setup(bot):
    bot.add_cog(DownloadMessages(bot))
