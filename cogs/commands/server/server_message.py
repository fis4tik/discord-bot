import discord
from discord.ext import commands
import datetime

class ServerMessage(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.slash_command()
    async def сообщение(self, ctx: discord.ApplicationContext,
                        code: discord.Option(str, "Укажите код сообщения, данный вам техническим администратором.")): # type: ignore
        if code == "12H-GHI":
            embed = discord.Embed(title="Важная новость", color=discord.Color.greyple(), timestamp=datetime.datetime.now())
            embed.description = """
С 8 октября Discord был заблокирован на территории Российской Федерации ([Подробнее](https://rb.ru/news/discord-blok-experty/))
В этом сообщении я коротко расскажу как обойти блокировку.

## Как обойти блокировку
- По [ссылке](https://github.com/Flowseal/zapret-discord-youtube) скачиваем последний релиз
- Распоковываем архив
- Запускаем файл `discord.bat` **от имени администратора**
- Наслаждаемся!
Если у вас не сработало, почитайте гайд на [странице проекта](https://github.com/Flowseal/zapret-discord-youtube?tab=readme-ov-file#guides)
"""
        embed.footer = discord.EmbedFooter(text="Пересылайте эту инструкцию своим друзьям!")
        channel = self.bot.get_channel(1253379693177208883)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(ServerMessage(bot))