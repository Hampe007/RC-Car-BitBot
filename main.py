def on_received_value(name, value):
    global speed, A, B
    if name == "acc":
        speed = value
    elif name == "A":
        A = value
    elif name == "B":
        B = value
radio.on_received_value(on_received_value)

B = 0
A = 0
speed = 0
radio.set_group(1)
music.set_volume(250)
music.play_melody("C5 A F E D G B F ", 240)
basic.show_icon(IconNames.SQUARE)
basic.clear_screen()
basic.show_icon(IconNames.DIAMOND)
basic.clear_screen()
basic.show_icon(IconNames.SMALL_SQUARE)
basic.clear_screen()
basic.show_icon(IconNames.SMALL_DIAMOND)
basic.clear_screen()
basic.show_leds("""
    . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
""")
basic.clear_screen()
basic.show_leds("""
    . . . . .
        . # . # .
        . # # # .
        . # . # .
        . . . . .
""")
basic.clear_screen()
basic.show_icon(IconNames.YES)
basic.clear_screen()
music.set_volume(0)
music.stop_all_sounds()

def on_forever():
    bitbot.select_model(BBModel.CLASSIC)
    bitbot.bb_enable_bluetooth(BBBluetooth.BT_ENABLE)
basic.forever(on_forever)

def on_forever2():
    if A == 1:
        bitbot.set_pixel_color(0, 0x00FF00)
        bitbot.set_pixel_color(1, 0x00FF00)
        bitbot.set_pixel_color(2, 0x00FF00)
        bitbot.move(BBMotor.RIGHT, BBDirection.FORWARD, speed)
    else:
        bitbot.set_pixel_color(0, 0xFF0000)
        bitbot.set_pixel_color(1, 0xFF0000)
        bitbot.set_pixel_color(2, 0xFF0000)
        bitbot.move(BBMotor.RIGHT, BBDirection.FORWARD, 0)
    if B == 1:
        bitbot.set_pixel_color(6, 0x00FF00)
        bitbot.set_pixel_color(7, 0x00FF00)
        bitbot.set_pixel_color(8, 0x00FF00)
        bitbot.move(BBMotor.LEFT, BBDirection.FORWARD, speed)
    else:
        bitbot.set_pixel_color(6, 0xFF0000)
        bitbot.set_pixel_color(7, 0xFF0000)
        bitbot.set_pixel_color(8, 0xFF0000)
        bitbot.move(BBMotor.LEFT, BBDirection.FORWARD, 0)
basic.forever(on_forever2)
