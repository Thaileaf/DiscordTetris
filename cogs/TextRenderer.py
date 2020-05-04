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
    def create_grid(self, width, height, outline, fill_mat=' '):
        grid = []
        for i in range(height):
            row = []
            for j in range(width):
                if j == 0 or j == width - 1 or i == 0 or i == height - 1:
                    row.append(outline)
                else:
                    row.append(fill_mat)
            grid.append(row)
        self.grid = grid
        return grid

    # Creates a shape with a position
    async def create_shape(self, name, image, x, y, material):
        if name in self.shapes.keys():
            raise Exception('There is already a shape named that')
        self.shapes[name] = Shape(image, x, y, material)

    #
    async def draw_shape(self, shape):
        positions = []
        for i, row in enumerate(shape.image):
            for j, point in enumerate(row):
                if point == '0':
                    positions.append((j + shape.x, i + shape.y))
        for pos in positions:
            if self.grid[pos[1]][pos[0]] != ' ':
                shape.position.collide()
            self.grid[pos[1]][pos[0]] = shape.material




    @tasks.loop(seconds=1.0)
    async def draw_grid(self, grid):
        pass


class Shape:

    def __init__(self, image, x, y, material, velocity):
        self.image = image
        self.position = (x, y)
        self.material = material
        self.velocity = velocity
        self.collision = False
        self.ex_image = [['*', '*', '*', '*', '*', ],
                         ['*', ' ', ' ', ' ', '*', ],
                         ['*', ' ', ' ', ' ', '*', ],
                         ['*', '*', '*', '*', '*', ]
                         ]

        def collide():
            self.collision = True


def setup(client):
    client.add_cog(TextRenderer(client))

test = TextRenderer(None)
grid = test.create_grid(20, 8, '*')
print(grid)
for row in grid:
    print(''.join(row))