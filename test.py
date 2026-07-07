from PIL import Image

img = Image.open("images/shoe01.jpg")

img = img.convert("RGB")

img.save(
    "images/shoe1.jpg",
    "JPEG"
)

print("Done")