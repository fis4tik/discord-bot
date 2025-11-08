import discord
from discord.ext import commands

class Ansi(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot

    
    @commands.slash_command(name="update", description="Отправляет статистику об обновлении бота (только для создателя!)", 
                            guild_ids=[1251166687445647360, 1253353282580119654],
                            )
    @commands.is_owner()
    async def ansi(self, ctx: discord.ApplicationContext, veriant: discord.Option(str, "Выберите способ", choices=["ANSI-текст", "EMBED (NEW!)"])): # type: ignore
        channel = self.bot.get_channel(1212019948151513138)
        if veriant == "ANSI-текст":
            with open('files/ansi.txt', 'r', encoding='utf-8') as file:
                content = file.read()
            await channel.send(f"< @everyone >\n{content}", file=discord.File("files/image.png"))
            await ctx.respond("Отправлено!", ephemeral=True)
        else:
            embed = discord.Embed(title="cooly - НОВАЯ КОМАНДА <:new_1:1258852540087275693><:new_2:1258852538787037316>", color=0xf0d826)
            
            embed.add_field(name="</8ball:1258845659448999966> - Выдает 20 случайных ответов на вопрос. Просто мини-игра, да...", value="",inline=False)

            await channel.send("< @everyone >",embed=embed)
            await ctx.respond("Отправлено!", ephemeral=True)




def setup(bot):
    bot.add_cog(Ansi(bot))
