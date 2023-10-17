from PIL import Image, ImageDraw
from kivy.app import App
from kivy.uix.screenmanager import Screen
from os import system

system('pip install Pillow')
import math
import random


class PhotoGalleryApp(App):
    pass


class Display(Screen):
    def displayimage(self):
        return images[index]

    def advance(self):
        global index, images
        if index < len(images):
            index += 1
        else:
            index = 0
        return images[index]

    def back(self):
        global index, images
        if index >= 1:
            index -= 1
        else:
            index = len(images)
        return images[index]


class Filters(Screen):

    def load(self, image):
        self.ids.big_image.source = image






    def black_and_white(self, image):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = pixels[x, y][0]
                green = pixels[x, y][1]
                blue = pixels[x, y][2]

                avg = (red + blue + green) // 3

                pixels[x, y] = (avg, avg, avg)

        index = image.find(".")
        img.save(image[:index] + "b&w.jpg")
        # self.load(img)
        self.ids.big_image.source = image[:index] + "b&w.jpg"

    def invert(self, image):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = 255 - pixels[x, y][0]
                green = 255 - pixels[x, y][1]
                blue = 225 - pixels[x, y][2]
                pixels[x, y] = (red, green, blue)
        index = image.find(".")
        img.save(image[:index] + "invert.jpg")
        # self.load(img)
        self.ids.big_image.source = image[:index] + "invert.jpg"

    def sepia(self, image):
        img = Image.open(image)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = pixels[x, y][0]
                green = pixels[x, y][1]
                blue = pixels[x, y][2]

                r1 = int(red * .393 + green * 0.769 + blue * 0.189)
                g1 = int(red * .349 + green * 0.686 + blue * 0.168)
                b1 = int(red * .272 + green * 0.534 + blue * 0.131)

                pixels[x, y] = (r1, g1, b1)
        index = image.find(".")
        img.save(image[:index]+"sepia.jpg")
        # self.load(img)
        self.ids.big_image.source = image[:index]+"sepia.jpg"

    def pixelate(self, image, startx, starty, width, height):
        img = Image.open(image)
        pixels = img.load()

        for y in range(starty, starty + height, 40):
            for x in range(startx, startx + width, 40):
                color = pixels[x, y]

                for j in range(y, y + 40):
                    for i in range(x, x + 40):
                        pixels[i, j] = color

        index = image.find(".")
        img.save(image[:index] + "pixelated.jpg")
        # self.load(img)
        self.ids.big_image.source = image[:index] + "pixelated.jpg"

    def pointillism(self, image):
        img = Image.open(image)
        pixels = img.load()
        canvas = Image.new("RGB", (img.size[0], img.size[1]), "white")

        for i in range(300000):
            x = random.randint(0, img.size[0] - 1)
            y = random.randint(0, img.size[1] - 1)
            size = random.randint(6, 8)
            ellipsebox = [(x, y), (x + size, y + size)]
            draw = ImageDraw.Draw(canvas)
            draw.ellipse(ellipsebox, fill=(pixels[x, y][0], pixels[x, y][1], pixels[x, y][2]))
            del draw

        index = image.find(".")
        canvas.save(image[:index] + "points.jpg")
        # self.load(img)
        self.ids.big_image.source = image[:index] + "points.jpg"
    def lines_helper(self, pixel):
        avg = (pixel[0] + pixel[1] + pixel[2]) // 3
        return avg

    def lines(self, image):
        img = Image.open(image)
        pixels = img.load()
        canvas = Image.new("RGB", (img.size[0], img.size[1]), "white")

        for y in range(img.size[1] - 1):
            for x in range(img.size[0] - 1):
                potency = self.lines_helper(pixels[x, y])
                if abs(potency - self.lines_helper(pixels[x + 1, y])) > 20 or abs(
                        potency - self.lines_helper(pixels[x - 1, y])) > 20 or abs(
                    potency - self.lines_helper(pixels[x, y + 1])) > 20 or abs(
                    potency - self.lines_helper(pixels[x, y - 1])) > 20:
                    ellipsebox = [(x - 1, y - 1), (x, y)]
                    draw = ImageDraw.Draw(canvas)
                    draw.ellipse(ellipsebox, fill=(0, 0, 0))
                    del draw

        index = image.find(".")
        canvas.save(image[:index] + "lines.jpg")
        # self.load(img)
        self.ids.big_image.source = image[:index] + "lines.jpg"


images = ['erosionbird.jfif', 'smurfcat.jfif']
index = 0
PhotoGalleryApp().run()
