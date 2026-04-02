import qrcode

image = qrcode.make("https://youtu.be/xvFZjo5PgG0")
image.save("resources/qr.png", "png")
