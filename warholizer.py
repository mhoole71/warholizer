from gpiozero import LED, Button, Buzzer
from time import sleep
from picamera import PiCamera
from random import randint
import subprocess
import os

camera = PiCamera()
red_led = LED (23)
green_led = LED (24)
btn = Button (16)
buzzer = Buzzer(15)
image_directory = "warhol"
dir_num = 1

effects = ['negative', 'solarize', 'sketch', 'emboss', 'oilpaint', 'hatch', 'pastel','watercolor', 'film', 'cartoon']


while True:
     if btn.is_pressed:
          os.chdir("/home/pi/warholizer")
          image_directory = "warhol" + str(dir_num)
          os.mkdir(image_directory)
          os.chdir(image_directory)
          camera.start_preview(alpha = 192)
          for i in range(5):
               red_led.on()
               green_led.on()
               buzzer.on()
               sleep(0.5)
               red_led.off()
               green_led.off()
               buzzer.off()
               sleep(0.5)
          for j in range (4):
               camera.image_effect = effects[randint(0,len(effects)-1)]
               
               camera.capture('image%d.jpg' %j)
               print("Picture captured number", j)
               sleep(1)
          camera.stop_preview()
          image_args = ["gm", "montage",  "-geometry", "512x384+2+2", "-bordercolor", "red", "+tile", "image0.jpg", "image1.jpg", "image2.jpg", "image3.jpg", "warhol.jpg"]

          subprocess.check_call(image_args)
          
          print ("Warhol image created")

          os.chdir("/home/pi/warholizer")
          dir_num = dir_num+1
          
     else:
          red_led.off()
          green_led.off()
          buzzer.off()
          
