import discord
from discord.ext import commands


class Tetris(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def start_game(self, ctx):
        ctx.send()





def setup(client):
    client.add_cog(Tetris(client))