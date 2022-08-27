import math
import operator
import time
from functools import reduce
import mouse
import pyscreenshot
import pywhatkit
from PIL import Image
from PIL import ImageChops
import os


def mouseMovement():
    mouse.move(1900, 1950, absolute=True, duration=2)
    time.sleep(4)


def takeScreenShot():
    image = pyscreenshot.grab()  # can pass the size of the box will do once it is completed
    image.save(fr"C:\Users\NikhilBajpai\Pictures\Screenshots\iamStupid{i}.png".format(i))
    # image.save(r"C:\Users\NikhilBajpai\Pictures\Screenshots\iamStupid.png") #to take the first screenshot
    print("screenShot done")


def rmsDiff(im1, im2):
    h = ImageChops.difference(im1, im2).histogram()
    # calculate rms
    return math.sqrt(reduce(operator.add,
                            map(lambda h, i: h * (i ** 2), h, range(256))
                            ) / (float(im1.size[0]) * im1.size[1]))


def main():
    global i
    i = 1
    while True:
        mouseMovement()
        takeScreenShot()
        # static image do change the file name
        staticImage = Image.open(
            r"Enter your static image file path")
        dynamicImage = Image.open(
            fr"Enter your dynamic image file path\iamStupid{i}.png".format(i))
        change = rmsDiff(staticImage, dynamicImage)
        if change > 5.0:
            # open browser and play the video
            print("pass reached " + str(change) + str(i))
            os.remove(fr"Enter the dynamic image file path\iamStupid{i}.png".format(i))
            pywhatkit.playonyt("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            # rerun required
            break
        else:
            os.remove(fr"Enter the dynamic image file path\iamStupid{i}.png".format(i))
            i += 1
            print("pass reached" + str(change) + str(i))
        time.sleep(4)
        mouseMovement()


if __name__ == '__main__':
    main()
