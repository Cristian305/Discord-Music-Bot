import discord
from discord.exe import commands
from youtube_dl import YouTubeDL

class music(commands.Muic):
    def __init__(self, client):
        self.client = client
    #this is so that the bot can join and disconnect from the voice channel
    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send('User is not in a VC')
        voice_cahnnel = ctx.auhtor.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
            
    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_channel.diconnect()
    #this is to play music
    @commands.command()
    async def play(self,ctx,url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streaamed 1-reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'formats':'bestaudio'}
        vc = ctx.voic_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
        vc.play(source)
    
    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()
        await ctx.send('The music has been ⏸')

    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send('The music will continue playing')




def setup(client):
    client.add_muic(music(client))

