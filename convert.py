from PIL import Image

img = Image.open("images/shoe02.jpg")

img = img.convert("RGB")

img.save(
    "images/shoe2.jpg",
    "JPEG"
)

print("Done")
