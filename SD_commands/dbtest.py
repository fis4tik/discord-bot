import discord
from discord.ext import commands
import sqlite3

db = sqlite3.connect("database.db")

def createIfNotExists(userId: int):
    cursor = db.cursor()
    result = cursor.execute("""
        SELECT id FROM users 
        WHERE discord_id=(?)
    """, (userId,)).fetchone()

    if result is None:
        cursor = db.cursor()
        cursor.execute("""INSERT INTO users(discord_id) VALUES ((?))""", (userId,))
        db.commit()


class DB(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot



    @commands.slash_command()
    async def get_money(self, ctx: discord.ApplicationContext, user: discord.Option(discord.Member, "Введите пользователя", required=False)): # type: ignore
        if user == None:
            user = ctx.author
        createIfNotExists(user.id)
        cursor = db.cursor()
        result = cursor.execute("SELECT balance FROM users WHERE discord_id=(?)", (user.id,)).fetchone()

        await ctx.respond(f"У вас на счету $**{result[0]}**")


    @commands.slash_command()
    async def add_money(self, ctx: discord.ApplicationContext, amount: discord.Option(int, "Введите сумму пополнения"), user: discord.Option(discord.Member, "Введите пользователя", required=False)): # type: ignore
        if user == None:
            user = ctx.author
        createIfNotExists(user.id)
        cursor = db.cursor()
        cursor.execute("UPDATE users SET balance=balance + (?) WHERE discord_id = (?)", (amount, user.id))
        db.commit()

        await ctx.respond(f"Успешно добавлено $**{amount}** на вас счет.")


def setup(bot):
    bot.add_cog(DB(bot))