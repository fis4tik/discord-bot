import discord
from discord.ext import commands

class ExecuteCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids=[1253353282580119654])
    async def command_exec(self, ctx: discord.ApplicationContext, command_name: str):
            # Получаем команду по имени
            command = self.bot.get_command(command_name)
            
            if command is None:
                await ctx.respond(f"Команда '{command_name}' не найдена.")
                return
            
            # Создаем контекст для выполнения команды
            ctx.command = command
            await command(ctx)


def setup(bot):
    bot.add_cog(ExecuteCommands(bot))