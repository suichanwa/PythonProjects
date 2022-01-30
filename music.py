from dis import dis
import discord 
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice in None:
            await ctx.send("you aren't in voice")
        voice_channel = ctx.author.voice.channel
        
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_channel.move_to(voice_channel)
    
    @commands.command()
    async def discconect(self, ctx): 
        await ctx.voice_client.dissconect() 
        
    @commands.command()
    async def play(self, ctx, url):
        ctx.voice_client_stop()
        FFMPEG_OPTIONS = {'before_options' : '-reconnect 1 -reconnect_streanmed 1 -reconnect_delay_max 5', 
                           'options' : '-vn'}
        YDL_OPTIONS = {'format' : "bestaudio"}
        vc = ctx.voice_channel
        
        with youtube_dl.YouTubeDL(YDL_OPTIONS) as ydl:
            info = ydl.exctract_info(url, download = False)
            url2 = info['format'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)
            
    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("pause")
    
    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send("resume")
    
    @commands.command(name='volume')
    async def _volume(self, ctx: commands.Context, *, volume: int):
        """Sets the volume of the player."""

        if not ctx.voice_state.is_playing:
            return await ctx.send('Nothing being played at the moment.')

        if 0 > volume > 100:
            return await ctx.send('Volume must be between 0 and 100')

        ctx.voice_state.volume = volume / 100
        await ctx.send('Volume of the player set to {}%'.format(volume))  
        
        
def setup(client):
    client.add_cog(music(client))
    
