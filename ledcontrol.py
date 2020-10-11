import board
import neopixel
import subprocess
import control_server
import lightpatterns

subprocess.call("cd /home/pi/theaterLEDcontrol", shell=True)
subprocess.call("git pull", shell=True)

pixels = neopixel.NeoPixel(board.D18, 150)

control_server.startServer()



mode = "wave"

while True:
    if mode == "test":
        lightpatterns.testpattern.play(pixels)
    elif mode == "wave":
        lightpatterns.wavepattern.play(pixels)
