import discord
from discord.ext import commands, tasks

class TextRenderer(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.shapes = []
        self.grid = []

    @commands.Cog.listener()
    async def on_ready(self):
        print('Text Renderer online')

    # Draws a grid onto Discord chat.
    # Automatically refreshes with task refresh_grid called
    @commands.command()
    async def create_grid(self, ctx, width, height, outline, fill_mat=' '):
        grid = []
        for i in range(height):
            row = []
            for j in range(width):
                if j == 0 or j == width - 1 or i == 0 or i == height - 1:
                    row.append(outline)
                else:
                    row.append(fill_mat)
            row.append('\n')
            grid.append(row)
        self.grid = grid

    # Creates a shape with a position
    async def create_shape(self, name, image, x, y):
        if name not in self.shapes.keys():
            self.shapes[name] = Shape(image, x, y)
        else:
            raise Exception('There is already a shape named that')

    #
    async def draw_shape(self):
        pass

    @tasks.loop(seconds=1.0)
    async def draw_grid(self, grid):
        pass


class Shape:

    def __init__(self, image, x, y):
        self.image = image
        self.position = (x, y)
        self.ex_image = [[]]




def setup(client):
    client.add_cog(TextRenderer(client))