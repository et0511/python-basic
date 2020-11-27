
class Multiply:
    def __str__(self, x=0, y=0):
        return f'Multiply({self.x}, {self.y})'


    def forward(self, x, y):
        self.x = x
        self.y = y

        z = x * y
        return z


