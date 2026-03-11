from PIL import Image, ImageFilter

before = Image.open("resources/sunset.jpg")
after = before.filter(ImageFilter.FIND_EDGES)
after.save("resources/sunset_edges.jpg")
