from PIL import Image, ImageEnhance, ImageFiter
import os

path = "./imgs"
pathOut = "/editedImgs"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    
    edit = img.filter(ImageFiter.SHARPEN).convert('L').rotate(-90)
    
    clean_name = os.path.splitext(filename)[0]
    
    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')