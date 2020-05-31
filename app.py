import discord
import os
from time import sleep
from datetime import datetime

token=os.environ["DISCORD_TOKEN"]

client = discord.Client()

audio_dict = {
    "despacito" : "Alexa_D.m4a",
    "jerk" : "jerk.webm"
}

async def play_audio(message, audio_name):
    print(f"{datetime.now().strftime('%d-%b-%Y (%H:%M:%S.%f)')}\t{audio_name}")
    for vc in message.guild.voice_channels:
        if message.author in vc.members:
            vcClient = await vc.connect()
            opus_audio = await discord.FFmpegOpusAudio.from_probe(audio_dict[audio_name])
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
        await play_audio(message, "despacito")
    elif "this is so sad" in message.content.lower():
        await play_audio(message, "despacito")
    elif "oink oink" in message.content.lower():
        await play_audio(message, "jerk")

client.run(token)