from PIL import Image
import sys
filename = sys.argv[1]


thumb_filename = filename.replace(".jpg", "small.jpg")

img = Image.open(filename)
img.thumbnail((100,100))
img.save(thumb_filename)
print("created thumbnail", thumb_filename)
