import discord
import random
import responses

from discord.ext import commands

class EightBall(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot

    @commands.slash_command(name='8ball')
    async def _8ball(self, ctx: discord.ApplicationContext, question: discord.Option(str, "Задавай вопрос!")): # type: ignore
        """/8ball - Дорабатывается"""
        icon_url = 'https://i.imgur.com/XhNqADi.png'
        responses = [
            'Бесспорно.',
            'Предрешено!',
            'Никаких сомнений',
            'Определённо - да',
            'Можешь быть уверен в этом',
            'Мне кажется — да',
            'Вероятнее всего',
            'Хорошие перспективы',
            'Знаки говорят — да',
            'Да',
            'Пока не ясно, попробуй снова',
            'Спроси позже.',
            'Лучше не рассказывать',
            'Сейчас нельзя предсказать',
            'Сконцентрируйся и спроси опять',
            'Даже не думай',
            'Мой ответ — нет',
            'По моим данным — нет',
            'Перспективы не очень хорошие',
            'Весьма сомнительно.'
        ]
        random_c = random.choice(responses)
        index = responses.index(random_c)

        # Определение цвета в зависимости от выбранного ответа
        if index < 5:
            color = discord.Color.blue()  # Синий для первых 5 ответов
        elif index < 10:
            color = discord.Color.green()  # Зеленый для вторых 5 ответов
        elif index < 15:
            color = discord.Color.gold()  # Желтый для третьих 5 ответов
        else:
            color = discord.Color.red()  # Красный для последних 5 ответов

        if question == "__debug: responses[good]":
            color = discord.Color.blue()
            question = ""
            random_c = "*Использован префикс _debug. Отображение структурной версии*"
        elif question == "__debug: responses[cool]":
            color = discord.Color.green()
            question = ""
            random_c = "*Использован префикс _debug. Отображение структурной версии*"
        elif question == "__debug: responses[neutral]":
            color = discord.Color.gold()
            question = ""
            random_c = "*Использован префикс _debug. Отображение структурной версии*"
        elif question == "__debug: responses[bad]":
            color = discord.Color.red()
            question = ""
            random_c = "*Использован префикс _debug. Отображение структурной версии*"

        embed = discord.Embed(colour=color, description=question)
        embed.add_field(name=f'Ответ:', value=random_c)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(EightBall(bot))