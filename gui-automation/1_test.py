import pyautogui as pg

# Every pyautogui function call will wait 1 second before moving forward
# You can use this to get back control of your mouse or keyboard etc
pg.PAUSE = 1

# By moving cursor to top right, it raises a FailSageException
# If not caught, the program will crash
# Great for debugging as long as you dont catch this exception :P
pg.FAILSAGE = True

# Get width and height of your screen
size = pg.size()
print(size)

# Moving mouse
# moveTo works with absolute coordinates
# for i in range(10):
#     pg.moveTo(100, 100, duration=0.25)
#     pg.moveTo(200, 100, duration=0.25)
#     pg.moveTo(200, 200, duration=0.25)
#     pg.moveTo(100, 200, duration=0.25)

# moveRel works with relative coordinates
for i in range(10):
    pg.moveRel(100, 0, duration=0.25)
    pg.moveRel(0, 100, duration=0.25)
    pg.moveRel(-100, 0, duration=0.25)
    pg.moveRel(0, -100, duration=0.25)

# get mouse position
# try:
#     while True:
#         x, y = pg.position()
#         posStr = 'X: ' + str(x).rjust(4) + ' Y: '+str(y).rjust(4)
#         print(posStr, end='')
#         print('\b' * len(posStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\nDone.')

x = 942
y = 44
# click mouse position
pg.click(942, 44)

# In the same way, you can scroll, drag and also send keyboard keys and do cool stuff
