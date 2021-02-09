let now = 0
let parlaklik = 255
let firstTime = input.runningTime()
basic.forever(function () {
    if (parlaklik > 0) {
        parlaklik += -3
    }
    led.plotBrightness(randint(0, 4), randint(0, 4), parlaklik)
    now = input.runningTime() - firstTime
    if (now > 3000) {
        firstTime = input.runningTime()
        parlaklik = 255
    }
})
