fade = 0
movement = 1
motion = 0

def play(strip):
    fade += movement
    motion += 1
    
    if (fade <= 0 or fade >= 100):
        movement *= -1
    if motion >= len(pixels):
        motion = 0
        
    
    strip.fill((fade, fade, fade))
    strip[motion] = (0, 255, 0)
    strip.show()