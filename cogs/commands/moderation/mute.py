import discord
from discord.ext import commands
from datetime import datetime
from datetime import timedelta
import re
from discord.utils import escape_mentions, escape_markdown

class MuteCommand(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot
    
    @commands.slash_command(name='mute', description="Замутить пользователя")
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def text_mute(self, ctx: discord.ApplicationContext, member: discord.Option(discord.Member, "Пользователь (упоминание или id)"), duration: discord.Option(str, "Длительности (2h, 5m)"), reason: discord.Option(str, "Укажите причину мута")): # type: ignore
        # Создаем роль "Muted", если она еще не существует
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            muted_role = await ctx.guild.create_role(name="Muted")

        # Парсим продолжительность мута
        match = re.match(r"(\d+)([mh])", duration)
        if match:
            amount, unit = match.groups()
            amount = int(amount)
            if unit == 'm':
                delta = timedelta(minutes=amount)
            elif unit == 'h':
                delta = timedelta(hours=amount)
            # Форматируем время до снятия наказания в удобочитаемый формат
            unban_time = self.format_duration(delta)
            # Вычисляем время снятия наказания
            unban_datetime = datetime.now() + delta
            unban_datetime_str = unban_datetime.strftime("%d.%m.%Y %H:%M")
        else:
            await ctx.respond("Неверный формат времени. Используйте 'm' для минут и 'h' для часов.")
            return
        
        log_channel = self.bot.get_channel(1235617006225461258)
        timestamp = f'<t:{int(datetime.now().timestamp())}>'

        emd = discord.Embed(description=f"Пользователь: {member.mention}\nМодератор: {ctx.author.mention}\nВремя: {timestamp}", title="Пользователь замьючен", color=0xE32636)
        await log_channel.send(embed=emd)
        

        # Добавляем роль "Muted" пользователю
        await member.add_roles(muted_role)

        embed = discord.Embed(description=f"**Причина:** {escape_mentions(text=escape_markdown(reason))}", color=0xDC143C)
        embed.set_author(name=f"Пользователь {member.display_name} был замьючен на {unban_time}", icon_url=member.avatar.url if member.avatar else member.default_avatar.url)
        embed.set_footer(text=f"Модератор: {ctx.author.display_name}, Время снятия наказания: {unban_datetime_str}", icon_url=ctx.guild.icon.url if ctx.guild.icon else "https://cdn.discordapp.com/attachments/1253373570218983525/1253373610492563506/discord-avatar-512-E35JI.png?ex=66759ea3&is=66744d23&hm=dc551a6eb7439846489182fca79b4fc8cec993b4c4fe91fbc7d1c836d0a209af&")
        await ctx.respond(embed=embed)

        # Ждем указанное время и убираем роль
        await discord.utils.sleep_until(discord.utils.utcnow() + delta)
        await member.remove_roles(muted_role)
        emd = discord.Embed(title="Наказание было снято", 
                            description=f"**Пользователь:** {member.mention}\n**Модератор:** {ctx.author.mention}\n**Время:** {timestamp}",
                            color=0x00BFFF)
            
        await log_channel.send(embed=emd)

        # Отправляем сообщение пользователю о снятии мута
        # embed = discord.Embed(title=f"Ваш мут прошел! Вы можете общаться дальше на **{ctx.guild.name}**", color=discord.Color.brand_green())
        # await user.send(embed=embed)

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
    


    @commands.slash_command(description="Размутить пользователя")
    async def unmute(self, ctx: discord.ApplicationContext, member: discord.Option(discord.User, "Укажите ID или ник пользователя"), reason: discord.Option(str, "Введите причину",)):  # type: ignore
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if muted_role in member.roles:

            log_channel = self.bot.get_channel(1235617006225461258)
            timestamp = f'<t:{int(datetime.now().timestamp())}>'

            emd = discord.Embed(title="Наказание было снято", 
                                description=f"**Пользователь:** {member.mention}\n**Модератор:** {ctx.author.mention}\nПричина: {reason}\n**Время:** {timestamp}",
                                color=0x00BFFF)
            
            await log_channel.send(embed=emd)
            await member.remove_roles(muted_role)
            embed = discord.Embed(description=f"**Причина:** {escape_mentions(text=escape_markdown(reason))}",author=discord.EmbedAuthor(name=f"Пользователь {member.name} был размьючен", icon_url=member.avatar.url), color=0x50C878)
            embed.set_footer(text=f"Модератор: {ctx.author.name}", icon_url=ctx.author.avatar.url)
            await ctx.respond(embed=embed)

        else:
            embed = discord.Embed(title='Ошибка', description="Пользователь не замьчен!", color=discord.Color.red())
            await ctx.respond(embed=embed, ephemeral=True)



def setup(bot):
    bot.add_cog(MuteCommand(bot))