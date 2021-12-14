from gpiozero import Button
from picamera import PiCamera
from time import gmtime, strftime
next_overlay_btn = Button(23)
take_picture_btn = Button(25)
take_picture_btn.when_pressed = take_picture
camera = PiCamera()
camera.resolution = (800, 480)
camera.hflip = True
camera.start_preview(alpha=128)
output = strftime("/home/pi/allseeingpi/image-%d-%m %H:%M.png", gmtime())
input()

def take_picture():
    camera.capture(output)
    camera.stop_preview()