now = 0
parlaklik = 255
firstTime = input.running_time()

def on_forever():
    global parlaklik, now, firstTime
    if parlaklik > 0:
        parlaklik += -3
    led.plot_brightness(randint(0, 4), randint(0, 4), parlaklik)
    now = input.running_time() - firstTime
    if now > 3000:
        firstTime = input.running_time()
        parlaklik = 255
basic.forever(on_forever)
