import discord
from discord.ext import commands
from datetime import timedelta
import re
from datetime import datetime

class VoiceCommands(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot

    voice = discord.Bot().create_group("voice", "Голосвые команды")


    @voice.command(description="Замутить пользователя в войсе")
    async def voice_mute(self, ctx: discord.ApplicationContext, member: discord.Option(discord.Member, "Пользователь (упоминание или id)"), duration: discord.Option(str, "Длительность (1m, 2h) "), reason: discord.Option(str, "Введите причину")): # type: ignore
        # Создаем роль "Muted", если она еще не существует
        muted_role = discord.utils.get(ctx.guild.roles, name="VMuted")
        if not muted_role:
            muted_role = await ctx.guild.create_role(name="VMuted")

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
        else:
            await ctx.respond("Неверный формат времени. Используйте 'м' для минут, 'ч' для часов, 'д' для дней.")
            return

        # Добавляем роль "Muted" пользователю
        await member.add_roles(muted_role)

        embed = discord.Embed(description=f"**Причина:** {reason}", color=0xDC143C)
        embed.set_author(name=f"Пользователь {member.display_name} был замьючен в голосовых каналах.", icon_url=member.avatar.url if member.avatar else member.default_avatar.url)
        embed.set_footer(text=f"Модератор: {ctx.author.display_name}, Время снятия наказания: {unban_time}", icon_url=ctx.guild.icon.url if ctx.guild.icon else "https://cdn.discordapp.com/attachments/1253373570218983525/1253373610492563506/discord-avatar-512-E35JI.png?ex=66759ea3&is=66744d23&hm=dc551a6eb7439846489182fca79b4fc8cec993b4c4fe91fbc7d1c836d0a209af&")
        await ctx.respond(embed=embed)

        # Ждем указанное время и убираем роль
        await discord.utils.sleep_until(discord.utils.utcnow() + delta)
        await member.remove_roles(muted_role)

        # Отправляем сообщение пользователю о снятии мута
        embed = discord.Embed(title=f"Ваш мут прошел! Вы можете общаться дальше на **{ctx.guild.name}**", color=discord.Color.brand_green())
        await member.send(embed=embed)

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
    
    @voice.command(name="unmute",description="Размутить пользователя в войсе")
    async def voice_unmute(self, ctx: discord.ApplicationContext, user: discord.Option(discord.User, "Укажите ID или ник пользователя"), reason: discord.Option(str, "Введите причину", required=False)):  # type: ignore
        muted_role = discord.utils.get(ctx.guild.roles, name="VMuted")
        if muted_role in user.roles:
            
            log_channel = self.bot.get_channel(1235617006225461258)
            timestamp = f'<t:{int(datetime.now().timestamp())}>'

            emd = discord.Embed(title="Пользователь размучен в голосовых каналах", 
                                description=f"**Размученный:** {user.mention}\n**Размутил:** {ctx.author.mention}\n**Время:** {timestamp}",
                                color=0x50C878)
            
            await log_channel.send(embed=emd)
            await user.remove_roles(muted_role)
            embed = discord.Embed(description=f"**Причина:** {reason}",author=discord.EmbedAuthor(name=f"Пользователь {user.name} был размучен", icon_url=user.avatar.url), color=0x50C878)
            embed.set_footer(text=f"Модератор: {ctx.author.name}", icon_url=ctx.author.avatar.url)
            await ctx.respond(embed=embed)

        else:
            embed = discord.Embed(title='Ошибка', description="Пользователь не замьчен в голосовых каналах!", color=discord.Color.red())
            await ctx.respond(embed=embed, ephemeral=True)


    @voice.command(name="kick", description="Кикнуть пользователя с войса")
    async def v_kick(self, ctx: discord.ApplicationContext, member: discord.Option(discord.Member, "Пользователь (упоминание или id)"), reason: discord.Option(str, "Введите причину", required=False)): # type: ignore
        if member.voice:
            voice_channel = member.voice.channel
            if member in voice_channel.members:
                await member.move_to(None)
                if reason:
                    embed = discord.Embed(author=discord.EmbedAuthor(name=f"{member.display_name} был кикнут с канала {voice_channel.name}"), 
                                        color=discord.Color.dark_grey(), 
                                        footer=discord.EmbedFooter(text="ARZ Moderator", icon_url=ctx.guild.me.avatar.url),
                                        description=f"**Причина:** {reason}")
                    await ctx.respond(embed=embed)
                else:
                    embed = discord.Embed(author=discord.EmbedAuthor(name=f"{member.display_name} был кикнут с канала {voice_channel.name}"), 
                                        color=discord.Color.dark_grey(), 
                                        footer=discord.EmbedFooter(text="ARZ Moderator", icon_url=ctx.guild.me.avatar.url))
                    await ctx.respond(embed=embed)

            else:
                embed = discord.Embed(title="❌ | Произошла ошибка", description="**Пользователь не находится в голосовом канале!**", color=discord.Color.brand_red())
                embed.set_footer(text="ARZ Moderator | Ошибка", icon_url=self.bot.user.avatar.url)
                await ctx.respond(embed=embed, ephemeral=True)

        else:
            embed = discord.Embed(title="❌ | Произошла ошибка", description="**Пользователь не находится в голосовом канале!**", color=discord.Color.brand_red())
            embed.set_footer(text="ARZ Moderator | Ошибка", icon_url=self.bot.user.avatar.url)
            await ctx.respond(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(VoiceCommands(bot))