import qrcode
img = qrcode.make('tenso')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")
