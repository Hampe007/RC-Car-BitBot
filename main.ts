radio.onReceivedValue(function (name, value) {
    if (name == "acc") {
        speed = value
    } else if (name == "A") {
        A = value
    } else if (name == "B") {
        B = value
    }
})
let B = 0
let A = 0
let speed = 0
radio.setGroup(1)
music.setVolume(250)
music.playMelody("C5 A F E D G B F ", 240)
basic.showIcon(IconNames.Square)
basic.clearScreen()
basic.showIcon(IconNames.Diamond)
basic.clearScreen()
basic.showIcon(IconNames.SmallSquare)
basic.clearScreen()
basic.showIcon(IconNames.SmallDiamond)
basic.clearScreen()
basic.showLeds(`
    . . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . .
    `)
basic.clearScreen()
basic.showLeds(`
    . . . . .
    . # . # .
    . # # # .
    . # . # .
    . . . . .
    `)
basic.clearScreen()
basic.showIcon(IconNames.Yes)
basic.clearScreen()
music.setVolume(0)
music.stopAllSounds()
basic.forever(function () {
    bitbot.select_model(BBModel.Classic)
    bitbot.bbEnableBluetooth(BBBluetooth.btEnable)
})
basic.forever(function () {
    if (A == 1) {
        bitbot.setPixelColor(0, 0x00FF00)
        bitbot.setPixelColor(1, 0x00FF00)
        bitbot.setPixelColor(2, 0x00FF00)
        bitbot.move(BBMotor.Right, BBDirection.Forward, speed)
    } else {
        bitbot.setPixelColor(0, 0xFF0000)
        bitbot.setPixelColor(1, 0xFF0000)
        bitbot.setPixelColor(2, 0xFF0000)
        bitbot.move(BBMotor.Right, BBDirection.Forward, 0)
    }
    if (B == 1) {
        bitbot.setPixelColor(6, 0x00FF00)
        bitbot.setPixelColor(7, 0x00FF00)
        bitbot.setPixelColor(8, 0x00FF00)
        bitbot.move(BBMotor.Left, BBDirection.Forward, speed)
    } else {
        bitbot.setPixelColor(6, 0xFF0000)
        bitbot.setPixelColor(7, 0xFF0000)
        bitbot.setPixelColor(8, 0xFF0000)
        bitbot.move(BBMotor.Left, BBDirection.Forward, 0)
    }
})
