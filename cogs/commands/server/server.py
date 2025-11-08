import discord
from discord.ext import commands
from discord.ui import Button, View

class ServerInfo(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot

    @commands.slash_command(description="Показывает информацию о сервере")
    @commands.guild_only()
    async def server(self, ctx: discord.ApplicationContext):
        guild = ctx.guild
        members = guild.members
        bots = len([m for m in members if m.bot])
        humans = len([m for m in members if not m.bot])
        total_members = len(members)

        statuses = {
            "offline": len([m for m in members if m.status == discord.Status.offline]),
            "dnd": len([m for m in members if m.status == discord.Status.do_not_disturb]),
            "idle": len([m for m in members if m.status == discord.Status.idle]),
            "online": len([m for m in members if m.status == discord.Status.online])
        }

        channels = guild.channels
        voice_channels = len([c for c in channels if isinstance(c, discord.VoiceChannel)])
        text_channels = len([c for c in channels if isinstance(c, discord.TextChannel)])
    # announcements_channels = len([c for c in channels if isinstance(c, discord.ch)])
        categories = len([c for c in channels if isinstance(c, discord.CategoryChannel)])
        stages = len([c for c in channels if isinstance(c, discord.StageChannel)])
        forums = len([c for c in channels if isinstance(c, discord.ForumChannel)])
        total_channels = voice_channels + text_channels + stages + forums
        
        owner = ctx.guild.owner.name
        language = ctx.guild_locale

        created_at = int(ctx.guild.created_at.timestamp())

        if owner == "0akame0":
            owner = "Какая то мразота хз" 
        else:
            owner = ctx.guild.owner.name

        if ctx.guild.id == 1135549856392413219:
            color = discord.Color.from_rgb(81, 0, 0)
        elif ctx.guild.id == 1253353282580119654:
            color = discord.Color.from_rgb(125, 125, 125)
        else:
            color = discord.Color.from_rgb(255, 255, 255)

        if ctx.guild_locale == "ru":
            language = ":flag_ru:"
        elif ctx.guild_locale == "de":
            language = ":flag_de:"
        elif ctx.guild_locale == "en-US":
            language = ":flag_lr:"
        elif ctx.guild_locale == "zh-CN":
            language = ":flag_cn:"
        elif ctx.guild_locale == "pl":
            language = ":flag_pl:"
        else:
            language = f"{ctx.guild_locale} (Др.)"

        embed = discord.Embed(title=f"{guild.name}", color=color)
        embed.add_field(name="Участники", value=f"<:members_total:1253643448460906547>Всего: {total_members}\n<:bot:1253643804276297728> Боты: {bots}\n<:members:1253642522132090951>Люди: {humans}", inline=True)
        embed.add_field(name="Статусы", value=f"<:offline:1253291904909578311> Оффлайн: {statuses['offline']}\n<:dnd:1253291903697424425> Не беспокоить: {statuses['dnd']}\n<:idle:1253291906172063816> Неактивен: {statuses['idle']}\n<:online:1253291907363115098> В сети: {statuses['online']}", inline=True)
        embed.add_field(name="Каналы", value=f"<:voice_channel:1253356205259096104> Голосовые: {voice_channels}\n<:text_channel:1253356206505066577> Текстовые: {text_channels}\n<:category:1253356203896209509> Категории: {categories}\n<:stage_channel:1253387098807992401> Трибуны: {stages}\n<:forum_channel:1253386753352536179>Форумы: {forums}\n<:total_channels:1253359158359625759> Всего: {total_channels}", inline=True)
        embed.add_field(name="Создатель", value=f"<:owner_icon:1253387509522628791> {owner}")
        embed.add_field(name="Язык", value=language)
        embed.add_field(name="Создан", value=f"<t:{created_at}:F>")
        button = Button(label="Данная команда еще дорабатывается.", style=discord.ButtonStyle.red, disabled=True)
        view = View(button)

        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
        else:
            url = "https://cdn.discordapp.com/attachments/1253373570218983525/1253373610492563506/discord-avatar-512-E35JI.png?ex=66759ea3&is=66744d23&hm=dc551a6eb7439846489182fca79b4fc8cec993b4c4fe91fbc7d1c836d0a209af&"  # Замените на Ваш URL адрес
            embed.set_thumbnail(url=url)
        debug = False
        if debug == True:
            demb = discord.Embed(title="Данная команда временно выключена, повторите позднее")
            await ctx.respond(embed=demb)
        else:
            await ctx.respond(embed=embed, view=view)


def setup(bot):
    bot.add_cog(ServerInfo(bot))
