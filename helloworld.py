from time import sleep
from picamera import PiCamera
button added
camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
# Camera warm-up time
sleep(5)
camera.capture('foo.jpg')
