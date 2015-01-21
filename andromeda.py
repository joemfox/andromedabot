import os
import random
from PIL import Image
import twitter
from auth import *

api = twitter.Api(consumer_key=Akey,consumer_secret=Askey,access_token_key = Atoken,access_token_secret = Astoken)

tile = random.randint(0,len(os.listdir("tiles"))-2)
print str(len(os.listdir("tiles")))+" tiles"
# image = Image.open("tiles/image_"+str(tile)+".png")
image = Image.open("tiles/"+os.listdir("tiles")[tile])
number = int(os.listdir("tiles")[tile].split("_")[1].split(".")[0])+1
print number
w = random.randint(500,2200)
print w

maxx,maxy = image.size
maxx = maxx-w
maxy = maxy-w


x = random.randint(0,maxx)
y = random.randint(0,maxy)

box = (x,y,x+w,y+w)
print box
thumb = image.crop(box)

thumb.save("thumb.jpg","JPEG")

thumbfile = open("thumb.jpg","rb")
print image

# status = twitter.Status(status="test", media=thumbfile)
status = "Coordinates: " + str(box[0]+(((number-1)%14)*5000)) + "," + str(box[1]+((number/14)*5000))+". " + str(w) + "x" + str(w) + "px"
print status
api.PostMedia(status,thumbfile)