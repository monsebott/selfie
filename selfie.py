from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_previe()
sleep(5)
camera.capture('/tmp/picture.jpg')
camera.stop_preview()