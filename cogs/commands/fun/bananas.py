import discord
from discord.ext import commands
import asyncio

class CountBananas(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.slash_command()
    async def bananas(self, ctx: discord.ApplicationContext):
        async def count_bananas(n):
            count = 0
            total_bars = 6  # Общее количество "ячейк" в прогресс баре
            progress_message = await ctx.respond("⬜⬜⬜⬜⬜⬜ 0%")
            
            for i in range(n):
                count += 1
                filled_bars = int((i + 1) / n * total_bars)  # Количество заполненных ячеек
                empty_bars = total_bars - filled_bars  # Количество пустых ячеек
                
                progress_bar = "🟩" * filled_bars + "⬜" * empty_bars  # Создание прогресс бара
                percent = (i + 1) / n * 100  # Процент завершения
                
                await progress_message.edit(content=f"{progress_bar} {percent:.0f}%")
                await asyncio.sleep(0.1)  # Асинхронная пауза

            return count
        
        bananas_count = await count_bananas(20)
        await ctx.edit(content=f"Бананов: {bananas_count}")


def setup(bot):
    bot.add_cog(CountBananas(bot))