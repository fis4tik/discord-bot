import discord
from discord.ext import commands
import asyncio
from datetime import timedelta
from datetime import datetime
import re


class Ban(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot

    @commands.slash_command(description="Заблокировать пользователя")
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx: discord.ApplicationContext, 
                user: discord.Option(discord.Member, "Пользователь (упоминание или ID)"), # type: ignore
                duration: discord.Option(str, "Укажите время бана в днях (необязательно)", required=False), # type: ignore
                reason: discord.Option(str, "Введите причину", min_length=8, max_length=500, required=False), # type: ignore
                delete_messages: discord.Option(int, "Дни очистки", min_value=1, max_value=7, required=False), # type: ignore
                silent: discord.Option(str, description="Выдать тихий бан?", choices=[discord.OptionChoice(name="True", value="True"), discord.OptionChoice(name="False", value="False")], required=False)): # type: ignore
        if user in ctx.guild.bans():
            if user.id == ctx.author.id:
                err = discord.Embed(description="Вы не можете заблокировать себя!", color=discord.Color.red())
                await ctx.respond(embed=err, ephemeral=True)
                return
            
            if user.bot:
                err = discord.Embed(description="Вы не можете банить ботов!", color=discord.Color.red())
                await ctx.respond(embed=err, ephemeral=True)
                return
            
            embed = discord.Embed(description=f"Пользователь {user.mention} забанен на сервере **{ctx.guild.name}**!", color=0xE32636)
            embed.set_footer(text="Это сообщение пропадет через 10 сек.")
            
            ban_kwargs = {}

            if reason:
                embed.add_field(name="Причина", value=reason, inline=False)
                ban_kwargs['reason'] = reason
            else:
                reason = "*Без причины*"

            if delete_messages is not None:
                times = delete_messages * 24 * 60 * 60
                embed.add_field(name="Удалить сообщения за", value=f"{delete_messages} дн.", inline=False)
                ban_kwargs['delete_message_seconds'] = times

            if duration:
                # Проверяем, что формат времени - это только дни с 'd'
                match = re.match(r"(\d+)([d])", duration)
                if match:
                    amount = int(match.group(1))

                    # Проверяем, что количество дней не превышает 2000
                    if amount > 2000:
                        errembed = discord.Embed(title="Вы не можете банить больше, чем на 2000 дней!", color=discord.Color.red())
                        await ctx.respond(embed=errembed, ephemeral=True)
                        return

                    delta = timedelta(days=amount)

                    # Форматируем время до снятия наказания в удобочитаемый формат
                    unban_time = self.format_duration(delta)
                    embed.add_field(name="Время бана", value=f"{unban_time}", inline=True)
                else:
                    errembed = discord.Embed(title="Неверный формат времени!", description="Используйте только **'d'** для дней.", color=discord.Color.red())
                    await ctx.respond(embed=errembed, ephemeral=True)
                    return

            if silent == "False":
                emd = discord.Embed(title="Информация о бане", description=f"**Заблокирован:** {user.mention}\n**Заблокировал:** {ctx.author.mention}\n**Причина:** {reason}", color=0xDC143C)
                emd.set_author(name="© ARZ Security Team™", icon_url=self.bot.user.avatar.url)
                emd.set_footer(text="Команда по безопасности Discord сервера.", icon_url=ctx.guild.icon.url)
                emd.set_thumbnail(url=user.avatar.url if user.avatar else user.default_avatar.url)
                await ctx.send(embed=emd)
                    
            log_channel = self.bot.get_channel(1235617006225461258)
            message = await ctx.respond(embed=embed)
            
            emd = discord.Embed(title="Информация о бане", description=f"**Заблокирован:** {user.mention}\n**Заблокировал:** {ctx.author.mention}\n**Причина:** {reason}", color=0x960018)

            await log_channel.send(embed=emd)
            await asyncio.sleep(10)
            await message.delete_original_response()
            
            await user.ban(**ban_kwargs) 
            if delta:
                await discord.utils.sleep_until(discord.utils.utcnow() + delta)
                await user.unban()

    def format_duration(self, delta):
        minutes = delta.total_seconds() / 60
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        duration = []
        if days:
            duration.append(f"{int(days)}дн.")
        if hours:
            duration.append(f"{int(hours)}ч.")
        if minutes:
            duration.append(f"{int(minutes)}мин.")
        return ' '.join(duration)
    
    

    @commands.slash_command(description="Разбанить пользователя")
    async def unban(self, ctx: discord.ApplicationContext, user: discord.Option(discord.User, "Пользователь (упоминание или ID)"), reason: discord.Option(str, "Введите причину", required=False)): # type: ignore

        banned_users = ctx.guild.bans()
        banned_user = None
        async for ban_entry in banned_users:
            if ban_entry.user.id == user.id:
                banned_user = ban_entry
                break

        if banned_user:
            if reason:
                await ctx.guild.unban(user)
                embed = discord.Embed(author=discord.EmbedAuthor(name=f"Пользователь '{user.display_name}' был разбанен", icon_url=user.avatar.url), color=0x960018,description=f"**Причина:** {reason}")
                embed.set_footer(text=f"Модератор: '{ctx.author.display_name}'", icon_url=ctx.author.avatar.url)
                await ctx.respond(embed=embed)
            else:
                await ctx.guild.unban(user)
                embed = discord.Embed(author=discord.EmbedAuthor(name=f"Пользователь '{user.display_name}' был разбанен", icon_url=user.avatar.url), color=0x960018)
                embed.set_footer(text=f"Модератор: '{ctx.author.display_name}'", icon_url=ctx.author.avatar.url)
                await ctx.respond(embed=embed)

            log_channel = self.bot.get_channel(1235617006225461258)
            timestamp = f'<t:{int(datetime.now().timestamp())}>'
            emd = discord.Embed(title="Пользователь раблокирован", 
                                description=f"**Разблокирован:** {user.mention}\n**Разблокировал:** {ctx.author.mention}\n**Время:** {timestamp}",
                                color=0x50C878)
            await log_channel.send(embed=emd)
            

        else:
            embed = discord.Embed(description="Данный пользователь не забанен на сервере!", color=0x2B2D31)
            await ctx.respond(embed=embed, ephemeral=True)



def setup(bot):
    bot.add_cog(Ban(bot))


