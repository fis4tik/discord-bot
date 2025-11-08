from discord.ext import commands
from discord import Option
import discord
import re
from datetime import timedelta

invite_links = ["*.gg/*", "*discord.com/invite*", "*discord.gg*", "*steamcommunity.com/gift-card*", "*-# Пользователь находится в федеральном розыске*"]
blackwords = [
    "*блять*", "*ебать*", "*нахуй*", "*долбаеб*", "*сука*", "*Слава Украине*", "*шлюха*", "*москаль*", "*укроп*",
    "*Слава России*", "*далбаеб*", "*блять*", "*сосать*", "*уебан*", "*хохол*", "*бандера*", "*пиздец*", "*пиздюк*",
    "*мать ебал*", "*безмамный*", "*член*", "*пизда*", "*хуй*", "*ZOV*", "*ЗОВ*", "*Зет*", "*Гойда*",
    "*мбам бам бам мы стреляем по хохлам*", "*Путин хуйло*", "*Зеленский клоун*", "*Слава Україні!*",
    "*слава украине*", "*негр*", "*негритянка*", "*Слава Україні*", "*Батько наш Бандера*", "*хахол*",
    "*Слава Українi*", "*долбаёб*", "*далбаёбина*", "*уебан*", "*poshel naxui*", "*idi naxui*",
    "*sosi*", "*сосо*", "*yeban*", "*yebok*", "*dalbaeb*", "*Slava ZSU*",
]

# Функция для создания регулярного выражения для поиска слова с заменами
def create_pattern(word):
    # Заменяем каждую букву на шаблон, который допускает различные замены
    # Например: "б" превращается в "[ббБ]" для учета различных регистров
    pattern = ''.join([f"[{char.lower()}{char.upper()}]" for char in word])
    return re.compile(pattern, re.IGNORECASE)  # Игнорировать регистр

class AutoMod(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot
        # Генерируем регулярные выражения для каждого плохого слова
        self.blackword_patterns = [create_pattern(word) for word in blackwords]

    async def rule_exists(self, ctx: discord.ApplicationContext, rule_name):
        rules = await ctx.guild.fetch_auto_moderation_rules()
        for rule in rules:
            if rule.name == rule_name:
                return True
        return False

    @discord.slash_command(name="automod", description="Устанавливать автоматическую модерацию")    
    @discord.guild_only()
    @commands.has_role("Модератор Discord Сервера")
    async def automod(self, ctx: discord.ApplicationContext, log_channel: Option(discord.TextChannel, "Куда будут отправляться уведомления?", required=True)): # type: ignore
        rules_to_create = {
            "Анти-приглашения": invite_links,
            "Плохие слова": blackwords
        }

        created_rules = []
        for rule_name, keywords in rules_to_create.items():
            if await self.rule_exists(ctx, rule_name):
                continue

            actions = [
                discord.AutoModAction(
                    action_type=discord.AutoModActionType.block_message,
                    metadata=discord.AutoModActionMetadata(),
                ),
                discord.AutoModAction(
                    action_type=discord.AutoModActionType.send_alert_message,
                    metadata=discord.AutoModActionMetadata(channel_id=log_channel.id),
                )
            ]
            
            await ctx.guild.create_auto_moderation_rule(
                name=rule_name,
                event_type=discord.AutoModEventType.message_send,
                trigger_type=discord.AutoModTriggerType.keyword,
                # Здесь просто передаем оригинальные ключевые слова
                trigger_metadata=discord.AutoModTriggerMetadata(keyword_filter=keywords),
                enabled=True,
                actions=actions,
                reason=f"{rule_name}!"
            )
            created_rules.append(rule_name)

        if created_rules:
            await ctx.respond(f":white_check_mark: Автомод активирован!\nДобавлены правила: **{', '.join(created_rules)}**")
        else:
            await ctx.respond(":negative_squared_cross_mark: Все правила уже были созданы!")

    async def on_message(self, message):
        # Здесь обрабатываем сообщение на наличие запрещенных слов с модификациями
        if message.author.bot:
            return

        for pattern in self.blackword_patterns:
            if pattern.search(message.content):
                await message.delete()
                # Здесь вы можете добавить логику для уведомления модераторов, если это необходимо
                return

def setup(bot):
    bot.add_cog(AutoMod(bot))