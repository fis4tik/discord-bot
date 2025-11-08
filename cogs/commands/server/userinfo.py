import discord
from discord.ext import commands

class UserInfo(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot

    @discord.slash_command(name="user-info", desciption="Получить информацию о пользователе")
    async def userinfo(self, ctx: discord.ApplicationContext, member: discord.Option(
    discord.Member,
    description="Укажите пользователя",
    required=False,
    default=None)): # type: ignore
        

        if not member:
            member = ctx.author

        color = None
        if isinstance(member, discord.Member):
            color = member.color
        else:
            color = discord.Color.brand_green()

        created_at = int(member.created_at.timestamp())

        embed = discord.Embed(title=f"{member}", color=color)
     # Формируем сообщение с использованием Discord timestamp

        
        embed.add_field(name="Дата создания аккаунта", value=f"<t:{created_at}:F>", inline=False)
        
        if isinstance(member, discord.Member):
            joined_at = int(member.joined_at.timestamp())
            
            embed.add_field(name="Дата создания аккаунта", value=f"<t:{joined_at}:F>", inline=False)


        decoration = member.avatar_decoration
        decoration_e = f"[Ссылка на декорацию]({decoration})"
        if decoration == None:
            decoration_e = "Нет"
        else:
            decoration_e = f"[Ссылка на декорацию]({decoration})"

        embed.add_field(name="Декорация профиля", value=decoration_e, inline=True)


        if isinstance(member, discord.Member):
            status = member.status
            if status == discord.Status.online:
                status = "<:online:1264911677602926613> В сети"
            elif status == discord.Status.idle:
                status = "<:idle:1264911651438596176> Неактивен"
            elif status == discord.Status.do_not_disturb:
                status = "<:dnd:1264911625421459466> Не беспокоить"
            elif status == discord.Status.offline or discord.Status.invisible:
                status = "<:offline:1264911588956311642> Не в сети"
            else:
                status = ":x: Не определено"

            embed.add_field(name="Статус", value=status, inline=True)
        
        if isinstance(member, discord.Member):
            device = member.is_on_mobile()
            if device == True:
                device = "Телефон"
            else:
                device = "Компьютер"
            embed.add_field(name="Устроство", value=device, inline=True)

        if member.avatar :
            embed.set_thumbnail(url=member.avatar.url)
        else:
            url = "https://cdn.discordapp.com/attachments/1253373570218983525/1253373610492563506/discord-avatar-512-E35JI.png?ex=66759ea3&is=66744d23&hm=dc551a6eb7439846489182fca79b4fc8cec993b4c4fe91fbc7d1c836d0a209af&"
            embed.set_thumbnail(url=url)

        if isinstance(member, discord.Member):
            await ctx.respond(embed=embed)
        else:
            embed.set_footer(text="Используйте эту команду на сервере, чтобы получить больше информации!")
            await ctx.respond(embed=embed)




def setup(bot):
    bot.add_cog(UserInfo(bot))
