from moviepy.editor import VideoFileClip
from PIL import Image, ImageDraw, ImageFont
import os
import hashlib

# Directory
directory = "Onbewerkt screenshots"
# Parent Directory path
parent_dir = "C:/Temp"
# mode
mode = 0o666
# Path
path = os.path.join(parent_dir, directory)
os.mkdir(path, mode)
print("Directory '% s' created" % directory)

# Directory
directory = "Bewerkte screenshots"
# Parent Directory path
parent_dir = "C:/Temp"
# mode
mode = 0o666
# Path
path = os.path.join(parent_dir, directory)
os.mkdir(path, mode)
print("Directory '% s' created" % directory)

# pad naar het filmbestand
filename = r'C:\Temp\XVR_ch1_main_20221221115846_20221221120430.mp4'

# haal het pad naar de map op
map_pad = os.path.split(filename)[0]

# laad de videoclip in
clip = VideoFileClip(filename)

# print aantal frames, frames per seconde, totale duur van de clip en duur van 1 frame
print("Aantal frames: ", int(clip.fps * clip.duration))
print("Frames per seconde: ", clip.fps)
print("Totale duur: ", clip.duration)
print("Duur van 1 frame: ", 1/clip.fps)

# bereken MD5-hash van het bestand
with open(filename, 'rb') as video_file:
    md5 = hashlib.md5(video_file.read()).hexdigest()
    print("MD5-hash: ", md5)

# maak schermafdruk van eerste 10 frames
for i, frame in enumerate(clip.iter_frames()):
    if i >= 10:
        break
    screenshot_file = os.path.join(onbewerkt_pad, f"{filename}_{i+1}.png")  # nummering vanaf 1
    img = Image.fromarray(frame)

    # voeg nummer toe rechtsonder in hoek
    number_img = Image.new('RGBA', img.size, (255, 255, 255, 0))
    number_img_draw = ImageDraw.Draw(number_img)
    font = ImageFont.truetype("arial.ttf", 50)  # grotere lettergrootte
    number_img_draw.text((img.width - 80, img.height - 100), str(i + 1), fill=(255, 0, 0), font=font)  # grotere lettergrootte
    img = Image.alpha_composite(img.convert('RGBA'), number_img)

    img.save(screenshot_file)

# sluit de videoclip
clip.close()

# print een bericht dat de schermafdrukken zijn gemaakt
print("Schermafdrukken zijn gemaakt.")

