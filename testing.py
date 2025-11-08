# import requests
# from deep_translator import GoogleTranslator

# response = requests.get("https://catfact.ninja/fact")
# data = response.json()  # Преобразуем JSON-ответ в словарь
# fact = data["fact"]

# # Переводим текст
# translated_fact = GoogleTranslator(source='auto', target='ru').translate(fact)
# print(translated_fact)  # Выводим переведенный текст

# import collections
# from prettytable import PrettyTable

# def table_create(list: list, titles: list):
#     """
#     Создать таблицу по указанным данным.

#     Значения:
#     --------
#     `list`: Список значений в таблице
#     `titles`: Заголовки таблицы

#     Пример:
#     -------
#     ``python
#     table_create(list=[
#         ["1 июля", "Понедельник", "+32"],
#         ["2 июля", "Вторник", "+31"], 
#         ["3 июля", "Среда", "+45"],
#         ["4 июля", "Четверг", "+33"]
#         ],
#         titles = ["Дата", "День", "Темп."])



#     """
#     data = list

#     table = PrettyTable(titles)
#     for row in data:
#         table.add_row(row)

#     return table


# result = table_create([["Харуко Ватабле", "Хороший"], ["Игорь", "Плохой"]], titles=["Человек", "Репутация"])
# print(result)







# from collections import namedtuple

# Address = namedtuple(
#     "Address",
#     "house street sity"
#                     )

# address = Address(
#     "Дом #1",
#     "Улица Пушкина",
#     "Москва"
#     )

# print(address.house)
# print(address.street)
# print(address.sity)



# from itertools import permutations


# from tqdm import tqdm
# def coco(n):
#     for _ in tqdm(
#         range(n),
#         desc="Подождите...",
#         ncols=70,
#         colour="#009FBD"
#     ):
#         letters = ["D", "D", "S", "E", "F", "G", "Y", "H", "J", "O", "B", "M", "Q", "X", "Z", "V", "K", "B"]
#         result = print(list(permutations(letters)))
#     return result
    
# print(coco(20))




# @bot.command()
# async def button_command(ctx: discord.ApplicationContext):
#     embed = discord.Embed(title="json saving and loading test", color=discord.Color.blue())
    
#     btn1 = discord.ui.Button(style=discord.ButtonStyle.primary, label="variable1 +=1")
#     btn2 = discord.ui.Button(style=discord.ButtonStyle.primary, label="variable1 +=1")
#     btn3 = discord.ui.Button(style=discord.ButtonStyle.primary, label="variable1 +=1")
    
#     view = discord.ui.View(btn1, btn2, btn3)
#     message = await ctx.respond(embed=embed, view=view)
#     with open('cogs/tickets/data.json', 'r') as file:
#         data = json.load(file)
#         v1 = data['variable1']
#         v2 = data['variable2']
#         v3 = data['variable3']
#         await message.edit_original_response(content=f"{v1}\n{v2}\n{v3}")
    



#     async def button1_callback(interaction):
#         with open('cogs/tickets/data.json', 'r') as file:
#             data = json.load(file)
#         data["variable1"] += 1

#         with open('cogs/tickets/data.json', 'w') as file:
#             json.dump(data, file,)
#         await interaction.response.send_message("Значение переменной 1 успешно обновлено!", ephemeral=True)
#         await message.edit_original_response(content=f"{data["variable2"]}\n{data["variable2"]}\n{data["variable3"]}")

#     async def button2_callback(interaction):
#         with open('cogs/tickets/data.json', 'r') as file:
#             data = json.load(file)
#         data["variable2"] += 1
#         v1 = data['variable1']
#         v2 = data['variable2']
#         v3 = data['variable3']
#         with open('cogs/tickets/data.json', 'w') as file:
#             json.dump(data, file,)
#         await interaction.response.send_message("Значение переменной 2 успешно обновлено!", ephemeral=True)
#         await message.edit_original_response(content=f"{v1}\n{v2}\n{v3}")

#     async def button3_callback(interaction):
#         with open('cogs/tickets/data.json', 'r') as file:
#             data = json.load(file)
#         data["variable3"] += 1
#         v1 = data['variable1']
#         v2 = data['variable2']
#         v3 = data['variable3']
#         with open('cogs/tickets/data.json', 'w') as file:
#             json.dump(data, file,)
#         await interaction.response.send_message("Значение переменной 3 успешно обновлено!", ephemeral=True)
#         await message.edit_original_response(content=f"{v1}\n{v2}\n{v3}")

#     btn1.callback = button1_callback
#     btn2.callback = button2_callback
#     btn3.callback = button3_callback

# @bot.command()
# async def cc(ctx: discord.ApplicationContext, category: discord.Option(str)): # type: ignore
#     with open('cc.json', 'r') as file:
#         data = json.load(file)
#     data["counter"] = 0
#     for channel in ctx.guild.channels:
#         if channel.category_id == int(category):
            
#             data["counter"] += 1
            
#     data["counter"] = data["counter"]
#     with open('cc.json', 'w') as file:
#         json.dump(data, file)

#     await ctx.respond(data["counter"])

# @bot.command()
# async def ca(ctx: discord.ApplicationContext):
#     await ctx.defer(invisible=False)
#     with open('cc.json', 'r') as file:
#         data = json.load(file)
    
#     messages_count = len(await ctx.channel.history(limit=None).flatten())
    
#     if "messages_count" in data:
#         data["messages_count"] += messages_count
#     else:
#         data["messages_count"] = messages_count

#     with open('cc.json', 'w') as file:
#         json.dump(data, file)

#     await ctx.respond(f'> `{data["messages_count"]}`')