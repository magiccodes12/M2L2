import os, random
import discord
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def Imágenes(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def Qué_es_la_contaminación(ctx):
    await ctx.send(f"La contaminación es un problema que está afectando gravemente a nuestro planeta. En otras palabras,se refiere a las sustancias nocivas en el aire, agua o suelo. Esto puede ser muy dañino al medio ambiente, a los seres vivos y a nuestra salud. Debido a eso, es muy importante saber tomar medidas de precaución para mejorar nuestro futuro, como por ejemplo: reciclar, reducir y reutilizar.")

@bot.command()
async def Clasifica_residuos(ctx):
    await ctx.send(f"Hay 3 categorías principales: Residuos Reciclables: Son materiales que pueden ser reciclados y reutilizados para hacer nuevos productos. Por ejemplo botellas de plástico, latas de aluminio, periódicos, cartones limpios, y envases de vidrio. Es importante colocarlos en los contenedores correctos para que puedan ser recogidos y procesados correctamente. Residuos Orgánicos: Son desechos biodegradables, materiales que provienen de plantas o animales y se descomponen naturalmente. Los restos de comida y de jardinería entran en esta categoría. Pueden ser compostados para convertirse en abono para plantas. Residuos No Reciclables: Son materiales que no pueden ser reciclados o compostados y van a los vertederos. Esto incluye cosas como pañales o envases de comida, y algunos tipos de plásticos que no son aceptados por los programas de reciclaje locales. Es importante tratar de reducir su cantidad al mínimo y buscar alternativas más ecológicas.")

@bot.command()
async def Hay_algo_más_que_puedo_hacer(ctx):
    await ctx.send(f"Algo más podría ser que si tienes objetos que ya no vayas a utilizar como jugetes, ropa o mantas, no los deseches. Se los puedes regalar a personas pobres o en malas condiciones que probablemente lo necesiten más que tú. Esto puede ayudar extendiendo la vida útil de muchos recursos y evitar la fabricación de nuevos.")

bot.run("INSERT BOT TOKEN")