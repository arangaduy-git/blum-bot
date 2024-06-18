import random
import time
import pyautogui
import keyboard
import cv2
from PIL import ImageGrab
import os
import numpy as np

pyautogui.PAUSE = 0.002


def find_star():
    img = cv2.imread("screenshot.png")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template_star_mini = cv2.imread(os.path.join(os.getcwd(), 'star.png'),
                          cv2.IMREAD_GRAYSCALE)

    template_star_big = cv2.imread(os.path.join(os.getcwd(), 'star1.png'),
                           cv2.IMREAD_GRAYSCALE)

    template_moroz = cv2.imread(os.path.join(os.getcwd(), 'moroz.png'),
                                cv2.IMREAD_GRAYSCALE)


    result_star_mini = cv2.matchTemplate(gray_img, template_star_mini, cv2.TM_CCOEFF_NORMED)
    result_star_big = cv2.matchTemplate(gray_img, template_star_big, cv2.TM_CCOEFF_NORMED)
    result_moroz = cv2.matchTemplate(gray_img, template_moroz, cv2.TM_CCOEFF_NORMED)
    loc_star_mini = np.where(result_star_mini >= 0.8)
    loc_star_big = np.where(result_star_big >= 0.8)
    loc_moroz = np.where(result_moroz >= 0.8)

    for pt in zip(*loc_star_mini[::-1]):
        xr = random.randint(-3, 3)
        yr = random.randint(-3, 3)
        pyautogui.click((pt[0] + 15 + ul[0] + xr, pt[1] + 20 + ul[1] + yr))

    for pt in zip(*loc_star_big[::-1]):
        xr = random.randint(-3, 3)
        yr = random.randint(-3, 3)
        pyautogui.click((pt[0] + 20 + ul[0] + xr, pt[1] + 25 + ul[1] + yr))

    for pt in zip(*loc_moroz[::-1]):
        xr = random.randint(-3, 3)
        yr = random.randint(-3, 3)
        pyautogui.click((pt[0] + 20 + ul[0] + xr, pt[1] + 25 + ul[1] + yr))


if __name__ == '__main__':

    print('Нажмите C в левом верхнем углу')
    while True:
        pos = pyautogui.position()
        ul = (pos.x, pos.y + 100)
        if keyboard.is_pressed("c"):
            break
    print(ul)
    time.sleep(0.5)

    print('Нажмите C в правом нижнем углу')
    while True:
        pos = pyautogui.position()
        dr = (pos.x, pos.y)
        if keyboard.is_pressed("c"):
            break
    print(dr)

    time.sleep(0.5)
    print('Начинаю кликать')

    print(ul[0], ul[1])
    print(dr[0], dr[1])

    while True:
        if keyboard.is_pressed('q'):
            break

        game_window = (ul[0], ul[1], dr[0], dr[1])
        im = ImageGrab.grab(game_window)
        im.save(os.getcwd() + '\\screenshot' + '.png', 'PNG')
        find_star()
