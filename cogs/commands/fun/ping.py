import discord
from discord.ext import commands
import time

class BotPing(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.slash_command(description="Проверить задержку бота")
    async def ping(self, ctx: discord.ApplicationContext):
        start_time = time.time()
        message = await ctx.respond("*Загружаю...*", ephemeral=True)
        end_time = time.time()
        # Вычисляем время работы бота
        elapsed_time = time.time() - self.bot.start_time
        seconds = int(elapsed_time)
        minutes = seconds // 60
        seconds = seconds % 60
        hours = minutes // 60
        minutes = minutes % 60

        # Форматируем строку с временем
        uptime_str = f"{hours} ч. {minutes} мин. {seconds} сек. назад"
        
        embed = discord.Embed(color=discord.Color.embed_background(), title="Понг!", description=f"⏱Сокет: `{round(self.bot.latency * 1000)} МС`・Запрос: `{round((end_time - start_time) * 1000)} МС`")
        embed.set_footer(text=f"Бот был запущен {uptime_str}")
        await message.edit(content=None, embed=embed)

def setup(bot):
    bot.add_cog(BotPing(bot))