import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 150)

fade = 0
movement = 1
motion = 0

while True:
    fade += movement
    motion += 1
    
    if (fade <= 0 or fade >= 100):
        movement *= -1
    if motion >= len(pixels):
        motion = 0
        
    
    pixels.fill((fade, fade, fade))
    pixels[motion] = (0, 255, 0)
    pixels.show()
