import discord
import subprocess

client = discord.Client()

@client.event
async def on_ready():
    print('Logged on as {0.user}!'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('c!run'):
        runServer = subprocess.run('python3 ./runServer.py', shell=True)
        print('returncode:', runServer.returncode)
        await message.channel.send('El servidor esta arrancando!')

    if message.content.startswith('c!help'):
        await message.channel.send('Lista de comandos \n ------------- \n \n c!help: Ayuda sobre comandos \n c!run: Arrancar servidor (ejecutar solo una vez) \n c!stop: Detener servidor')

client.run('OTk3NjIyMTk4NTI3MzI4Mzk4.GC-LqR.Q0m-b9RrPQtobFpsKxkFV86C-Ad8OPsiKlHKk0')
