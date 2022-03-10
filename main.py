list = []
radio.set_group(1) 
radio.set_transmit_power(7)
learn = 0

def on_logo_long_pressed():
    global learn
    learn = 1
    radio.send_value("learn", 1)
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

def alarm():
    if pins.digital_read_pin(DigitalPin.P1):
        music.play_tone(Note.C, 1000)
        


