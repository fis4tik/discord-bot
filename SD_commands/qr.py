import discord
from discord.ext import commands
import time
import random
import qrcode
from io import BytesIO
import io
from PIL import Image
from pyzbar.pyzbar import decode


class QRCodes(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot

    # ! frfr
    qr = discord.Bot().create_group("qr", "QR-коды")

    @qr.command(description="Создает QR-код")
    async def create(self, ctx: discord.ApplicationContext , content: discord.Option(str, "Введите текст.")): # type: ignore
        img = qrcode.make(content, border=2, box_size=5)
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)
        wait_emb = discord.Embed(title="Подождите, QR-Код создается", color=discord.Color.og_blurple())
        message = await ctx.respond(embed=wait_emb)
        wait_s = random.randint(1, 10)
        time.sleep(wait_s)
        emb_pic = discord.Embed(color=discord.Color.gold())
        emb_pic.set_image(url="attachment://qrcode.png")
        emb_suc = discord.Embed(title="Успешно. Наслаждайтесь!", color=discord.Color.green())
        await message.edit(embeds=[emb_pic , emb_suc], file=discord.File(fp=buffer, filename="qrcode.png"))


    @qr.command(description="Расшифровывает QR-код")
    async def read(self, ctx: discord.ApplicationContext, picture: discord.Option(discord.Attachment)): # type: ignore

        attachment = picture


        image_data = await attachment.read()
        image = Image.open(io.BytesIO(image_data))
        decoded_objects = decode(image)

        qr_data = decoded_objects[0].data.decode('utf-8')
        embed = discord.Embed(author=discord.EmbedAuthor(name="Расшифровка QR-кодов"), title=qr_data, color=discord.Color.dark_theme())
        file = discord.File(fp=io.BytesIO(image_data), filename="qrcode.png")
        embed.set_image(url="attachment://qrcode.png")
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(QRCodes(bot))
