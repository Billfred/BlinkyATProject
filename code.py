import board
import neopixel
import digitalio

from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.solid import Solid

from adafruit_led_animation.group import AnimationGroup
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.sequence import AnimateOnce
from adafruit_led_animation import color

from adafruit_seesaw.seesaw import Seesaw
from adafruit_seesaw.analoginput import AnalogInput
import adafruit_seesaw.neopixel # It has to be imported this way since we're also using standard neopixel libraries.

# Defining which pins are doing what on our QT Py RP2040.
pixel_pinA = board.A0
pixel_pinB = board.A1
pixel_pinC = board.A2

switch = digitalio.DigitalInOut(board.TX)
switch.switch_to_input(pull=digitalio.Pull.UP)

# Creating the two NeoSliders used to adjust brightness and intensity.
# Note that you need to cut the A0 address jumper on the bottom of the intensity NeoSlider to set a different I2C address.
# Read more about the address jumpers at https://learn.adafruit.com/adafruit-neoslider/pinouts

brightslider = Seesaw(board.STEMMA_I2C(), 0x30)
brightpot = AnalogInput(brightslider, 18)

intensityslider = Seesaw(board.STEMMA_I2C(), 0x31)
intensitypot = AnalogInput(intensityslider, 18)

# Update to match the number of NeoPixels you have connected
pixel_num = 20

def brightslider_to_brightness(value):
    return value / 1023

def intensityslider_to_intensity(value):
    return value / 512

# Sets system-level brightness. This is a number between 0 and 1.
# Because the NeoSliders send readings between 0 and 1023, we do math.
system_brightness = brightslider_to_brightness(brightpot.value)

# Sets system-level animation speed. Each animation has a constant multiplied by this.
# 1.0 is normal speed. 0.5 is double speed, 2.0 is half speed, etc.
system_speed = intensityslider_to_intensity(intensitypot.value)

pixelsA = neopixel.NeoPixel(pixel_pinA, pixel_num, brightness=system_brightness, auto_write=False)
pixelsB = neopixel.NeoPixel(pixel_pinB, pixel_num, brightness=system_brightness, auto_write=False)
pixelsC = neopixel.NeoPixel(pixel_pinC, pixel_num, brightness=system_brightness, auto_write=False)

# These variables dictate the garnetcycle animation.  We use the hex codes universally instead of the
# Adafruit libraries for colors because we want to define garnet to the University of South Carolina's
# definition.  And then we redefine white so it isn't quite so eye-searingly bright while running.
garnetcycle_speed = 0.25 * system_speed
garnet = 0x73000a
white = 0x555555

# This section defines the animations for the first NeoPixel strip.

garnetcycleA = ColorCycle(pixelsA, garnetcycle_speed, colors=(garnet, white, white))
sparkleA = Sparkle(pixelsA, speed=0.02*system_speed, color=0x73000a, num_sparkles=6)
cometA = Comet(pixelsA, 0.05*system_speed, garnet, tail_length=5)
cometrevA = Comet(pixelsA, 0.05*system_speed, garnet, tail_length=5, reverse=True)
rainbowA = Rainbow(pixelsA, 0.20*system_speed, precompute_rainbow=True)
rainbowchaseA = RainbowChase(pixelsA, 0.03*system_speed, size=2, spacing=3, reverse=True)
rainbowcometA = RainbowComet(pixelsA, 0.05*system_speed)
rainbowcometrevA = RainbowComet(pixelsA, 0.05*system_speed, reverse=True)
offA = Solid(pixelsA, 1, 0x000000)

# And the second strip. Note that some things are unique, like the reversal of cometB.

garnetcycleB = ColorCycle(pixelsB, garnetcycle_speed, colors=(white, garnet, white))
sparkleB = Sparkle(pixelsB, speed=0.02*system_speed, color=0x73000a, num_sparkles=6)
cometB = Comet(pixelsB, 0.05*system_speed, garnet, tail_length=5)
cometrevB = Comet(pixelsB, 0.05*system_speed, garnet, tail_length=5, reverse=True)
rainbowB = Rainbow(pixelsB, 0.20*system_speed, precompute_rainbow=True)
rainbowchaseB = RainbowChase(pixelsB, 0.03*system_speed, size=2, spacing=3)
rainbowcometB = RainbowComet(pixelsB, 0.05*system_speed)
rainbowcometrevB = RainbowComet(pixelsB, 0.05*system_speed, reverse=True)
offB = Solid(pixelsB, 1, 0x000000)

# And the third strip.  Still other things are unique, like the garnetcycle color order.

garnetcycleC = ColorCycle(pixelsC, garnetcycle_speed, colors=(white, white, garnet))
sparkleC = Sparkle(pixelsC, speed=0.02*system_speed, color=0x73000a, num_sparkles=6)
cometC = Comet(pixelsC, 0.05*system_speed, garnet, tail_length=5)
cometrevC = Comet(pixelsC, 0.05*system_speed, garnet, tail_length=5, reverse=True)
rainbowC = Rainbow(pixelsC, 0.20*system_speed, precompute_rainbow=True)
rainbowchaseC = RainbowChase(pixelsC, 0.03*system_speed, size=2, spacing=3, reverse=True)
rainbowcometC = RainbowComet(pixelsC, 0.05*system_speed)
rainbowcometrevC = RainbowComet(pixelsC, 0.05*system_speed, reverse=True)
offC = Solid(pixelsC, 1, 0x000000)

# These functions group and sequence animations to keep them neater in the main list.

cometone = AnimationSequence(cometA, cometrevB, cometC, cometrevA, cometB, cometrevC, advance_on_cycle_complete=True)
    # AnimationSequence will only start the next strip when the first is complete.
cometall = AnimationGroup(cometA, cometB, cometC)
    # AnimationGroup has all three running comets at once.
garnetcycle = AnimationGroup(garnetcycleA, garnetcycleB, garnetcycleC)
rainbowchaseall = AnimationGroup(rainbowchaseA, rainbowchaseB, rainbowchaseC)
rainbowall = AnimationGroup(rainbowA, rainbowB, rainbowC)
rainbowcometone = AnimationSequence(rainbowcometA, rainbowcometrevB, rainbowcometC, rainbowcometrevA, rainbowcometB, rainbowcometrevC, advance_on_cycle_complete=True)
rainbowcometall = AnimationGroup(rainbowcometA, rainbowcometB, rainbowcometC)
offall = AnimationGroup(offA, offB, offC)

animations = AnimationSequence(
    cometone,
    rainbowchaseall,
    cometall,
    garnetcycle,
    rainbowall,
    rainbowcometone,
    rainbowcometall,
    auto_clear=True,
)

offall.animate()

while True:

    if switch.value: # While this switch is NOT pressed
        offall.animate()
        animations.random()
        pass
    else:
        animations.animate()
        pass

system_brightness = brightslider_to_brightness(brightpot.value)
system_speed = intensityslider_to_intensity(intensitypot.value)
