import time
import blinkenlights

b = blinkenlights.Blinkenlights()

while True:
    b.tick()
    time.sleep(0.2)
