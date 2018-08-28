#!/bin/env python
#-*- coding:utf-8 -*-

from screen_shot import Screenshot
from pyzbar.pyzbar import decode
from PIL import Image

picture=r"C:/Users/when-/Pictures/screen.png"
screen=Screenshot()
screen.getScreen(picture)
image = Image.open(picture)
print(str(decode(image)[0].data, encoding='utf-8'))