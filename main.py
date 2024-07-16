from base64 import urlsafe_b64encode
from fastapi import FastAPI
from cv2 import VideoCapture, imwrite
from PIL import Image

import cv2
import json

app = FastAPI()

CAMERA_PORT = 1

camera = VideoCapture(CAMERA_PORT) 
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # roblox editableimage max resolution is 1k both sides
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
  

@app.get("/experiments/webcamera")
def read_item():
    result, imageBuffer = camera.read()

    if result:
        imwrite("test.png", imageBuffer)

        image = Image.open("test.png")

        pixels = {}

        for x in range(image.size[0]):
            pixels[x + 1] = {}

            for y in range(image.size[1]):
                red, green, blue = image.getpixel((x, y))
                pixels[x + 1][y + 1] = [ red, green, blue ]

        #dumpedPixelData = json.dumps(pixels).encode()
        #base64Data = urlsafe_b64encode(dumpedPixelData)

        return { "data": pixels }

    return { "data": None }