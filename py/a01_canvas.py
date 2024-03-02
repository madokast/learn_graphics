from typing import Tuple

class Canvas:
    def __init__(self, width:int, height:int) -> None:
        self.width = int(width)
        self.height = int(height)
        self.half_width = self.width // 2
        self.half_height = self.height // 2
        self.pixel_number = width * height
        self.reds = bytearray(self.pixel_number)
        self.greens = bytearray(self.pixel_number)
        self.blues = bytearray(self.pixel_number)
    def set_color(self, x:int, y:int, color:Tuple[int, int, int]) -> None:
        wx = self.half_width + x
        if wx < 0 or wx >= self.width:
            return
        wy = self.half_height - y
        if wy < 0 or wy >= self.height:
            return 
        index = wx * self.width + wy
        self.reds[index] = color[0]
        self.greens[index] = color[1]
        self.blues[index] = color[2]
    def draw_turtle(self) -> None:
        import turtle
        window = turtle.Screen()
        window.setup(width=self.width, height=self.height)
        pen = turtle.Turtle()
        pen.speed('fastest')
        pen.pensize(1)
        pen.penup()
        index = 0
        for y in range(self.half_height, -self.half_height, -1):
            pen.goto(-self.half_width, y)
            pen.pendown()
            for x in range(-self.half_width, self.half_width):
                print(x, y)
                pen.color((1,0,0))
                pen.forward(1)
                index += 1
            pen.penup() # return
        turtle.done()

        
if __name__ == "__main__":
    canvas = Canvas(400, 300)
    canvas.draw_turtle()
