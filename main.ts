let list = []
radio.setGroup(1)
radio.setTransmitPower(7)
let learn = 0
input.onLogoEvent(TouchButtonEvent.LongPressed, function on_logo_long_pressed() {
    
    learn = 1
    radio.sendValue("learn", 1)
})
function alarm() {
    if (pins.digitalReadPin(DigitalPin.P1)) {
        music.playTone(Note.C, 1000)
    }
    
}

