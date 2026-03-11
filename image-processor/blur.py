from PIL import ImageFilter, Image

before = Image.open("resources/dog.jpg")
after = before.filter(ImageFilter.BoxBlur(5))
# after = before.filter(ImageFilter.GaussianBlur(radius=4))
after.save("resources/dog-blurred.jpg")
