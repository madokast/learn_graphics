import tkinter

width, height=400, 300

root = tkinter.Tk()
root.overrideredirect(True)

canvas = tkinter.Canvas(root, width=width, height=height, bg="white")
canvas.pack()

canvas.bind("<Double-Button-1>", lambda e:root.destroy()) # 双击退出

img_data = bytearray(width * height * 3)

for x in range(0, width):
    for y in range(0, height):
        img_data[3 * (y*width + x) + 0] = 0
        img_data[3 * (y*width + x) + 1] = 255
        img_data[3 * (y*width + x) + 2] = 255
    img = tkinter.PhotoImage(data=f'P6\n{width} {height}\n255\n'.encode('ascii') + img_data)
    canvas.create_image(0, 0, anchor=tkinter.NW, image=img)
    root.update()

root.mainloop()

