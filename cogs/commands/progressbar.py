import discord
from discord.ext import commands

import discord
from discord.ext import commands
from PIL import Image, ImageDraw
import io



def create_rounded_progress_bar(progress, total):

    # Размеры изображения
    width = 500  # Увеличиваем ширину для лучшего качества
    height = 100  # Увеличиваем высоту для лучшего качества
    radius = height // 2  # Радиус закругления

    # Создаем новое изображение с прозрачным фоном
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Рисуем закругленный фон
    draw.rounded_rectangle([0, 0, width, height], radius=radius, fill='black')

    # Вычисляем ширину прогресс-бара
    bar_width = int((progress / total) * (width - radius * 2))  # Учитываем радиусы

    # Рисуем закругленный прогресс-бар
    draw.rounded_rectangle([0, 0, bar_width + radius, height], radius=radius, fill='white')

    # Уменьшаем изображение для сглаживания
    img = img.resize((width // 2, height // 2), Image.Resampling.LANCZOS)

    return img

class ProgressBar(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[1253353282580119654])
    async def progress(self, ctx: discord.ApplicationContext, progress: int, total: int):
        if progress < 0 or total <= 0 or progress > total:
            await ctx.send("Пожалуйста, введите корректные значения для прогресса и общего количества.")
            return

        img = create_rounded_progress_bar(progress, total)

        # Создаем объект BytesIO для хранения изображения в памяти
        with io.BytesIO() as image_binary:
            img.save(image_binary, 'PNG')
            image_binary.seek(0)  # Перемещаем указатель в начало

            # Отправляем изображение в канал
            await ctx.respond(content=f"Данные: Беллый закругленный, {progress}/{total}",file=discord.File(image_binary, 'progress_bar.png'))


def setup(bot):
    bot.add_cog(ProgressBar(bot))