from PIL import Image

ImageList=["Image1.jpg","Image2.jpeg","Image3.jpg"]
frames=[Image.open(file) for file in ImageList]

frames[0].save("output.gif", save_all=True, append_images=frames[1:], duration=500, loop=0)

