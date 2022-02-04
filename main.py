degrees = input.compass_heading()
if degrees < 45:
    basic.show_string("N")
if degrees < 135:
    basic.show_string("E")
if degrees < 225:
    basic.show_string("S")
if degrees < 315:
    basic.show_string("W")

def on_forever():
    pass
basic.forever(on_forever)
