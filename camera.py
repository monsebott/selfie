from gpiozero import button
next_overlay_btn = Button(23)
take_pic_btn = Button(25)
next_overlay_btn.when_pressed = next_overlay
take_pic_btn.when_pressed = take_picture
def next_overlay():
    print("Next overlay")

def take_picture():
    print("Take a picture")