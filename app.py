import discord
from time import sleep

token="NzA2NDY0MzUyMTUyMTkxMDA3.Xq6oUQ.tk12kQXRqP_xfQ3JSs5J189lyas"

client = discord.Client()

async def play_despacito(message):
    for vc in message.guild.voice_channels:
        if message.author in vc.members:
            vcClient = await vc.connect()
            opus_audio = await discord.FFmpegOpusAudio.from_probe("Alexa_D.m4a")
            vcClient.play(opus_audio)
            while vcClient.is_playing():
                sleep(0.5)
            await vcClient.disconnect()
            return
    await message.channel.send("You are currently not in any voice channels!")
    return

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.id in message.raw_mentions:
        await play_despacito(message)
    elif "this is so sad" in message.content.lower():
        await play_despacito(message)
    '''
    # loose sad matching
    elif "sad" in map(lambda x: x.lower(), message.content.split()):
        for vc in message.guild.voice_channels:
            if message.author in vc.members:
                vcClient = await vc.connect()
                opus_audio = await discord.FFmpegOpusAudio.from_probe("Alexa_D.m4a")
                vcClient.play(opus_audio)
                while vcClient.is_playing():
                    sleep(0.5)
                await vcClient.disconnect()
                return
        return
    '''

client.run(token)