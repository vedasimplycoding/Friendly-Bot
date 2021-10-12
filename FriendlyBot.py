import discord
import random

TOKEN = 'your token '

client = discord.Client()

@client.event
async def on_ready():
    print('We hvae logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')


    if message.author == client.user:
        return

    if message.channel.name == 'general':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == '!random':
            response = f'This is you random number:{random.randrange(1000000)}'
            await message.channel.send(response)
            return
        elif user_message.lower() == 'version':
            await message.channel.send(f'1.0.1')
            return
        elif user_message.lower() == 'happy new year':
            await message.channel.send(f'Happy New Year!:tanabata_tree::tada:{username}')
            return
        elif user_message.lower() == 'good morning':
            await message.channel.send(f'Good Morning:sunny::sun_with_face::white_sun_small_cloud::city_sunset:{username}')
            return
        elif user_message.lower() == 'hi':
            await message.channel.send(f'Hi:man_raising_hand: {username}')
            return


    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere')
        return

    if user_message.lower() == '!youtube':
        await message.channel.send('Channel: https://bit.ly/VedaSimplyCoding')
        return

    if user_message.lower() == '!web1':
        await message.channel.send('Calculator:https://vedasimplycoding.github.io/Online-Calculator/')
        return

    if user_message.lower() == '!web2':
        await message.channel.send('Tamil:https://vedasimplycoding.github.io/Tamil-1/')
        return

    if user_message.lower() == '!web3':
        await message.channel.send('Reach for the top:https://vedasimplycoding.github.io/Reach-for-the-Top-Summary/')
        return

    if user_message.lower() == '.ping':
        await message.channel.send('pong!')
        return

    if user_message.lower() == 'discord':
        await message.channel.send('https://discord.com/')
        return

    if user_message.lower() == 'friends':
        await message.channel.send(':blush:')
        return

    if user_message.lower() == 'enemy':
        await message.channel.send(':cry:')
        return

    if user_message.lower() == 'exam':
        await message.channel.send('All the best!:thumbsup::first_place::thumbsup:')
        return

    if user_message.lower() == 'exam':
        await message.channel.send('All the best!:thumbsup::first_place::thumbsup:')
        return

    if user_message.lower() == '.x':
        await message.channel.send('o')
        return

    if user_message.lower() == '.date':
        await message.channel.send('11-10-2021')
        return

    if user_message.lower() == '.veda':
        await message.channel.send('Hello Veda.SimplyCoding')
        return

    if user_message.lower() == '.samarth':
        await message.channel.send('Hello Samarth')
        return

client.run(TOKEN)
