from PIL import ImageGrab
import os
import time
import cv2
import numpy as np
import keyboard
import pyautogui


pyautogui.PAUSE = 0.002
def find_mana():
    img = cv2.imread("screenshot.png")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(os.path.join(os.getcwd(), 'star.png'),
                          cv2.IMREAD_GRAYSCALE)  # +15

    template1 = cv2.imread(os.path.join(os.getcwd(), 'star1.png'),
                          cv2.IMREAD_GRAYSCALE)  # 20

    result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
    result1 = cv2.matchTemplate(gray_img, template1, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.8)
    loc1 = np.where(result1 >= 0.8)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img, pt, (pt[0] + 30, pt[1] + 30), (0, 255, 0), 1)
        pyautogui.click((pt[0] + 15 + 1370, pt[1] + 15 + 226))

    for pt in zip(*loc1[::-1]):
        cv2.rectangle(img, pt, (pt[0] + 40, pt[1] + 40), (0, 255, 0), 1)
        pyautogui.click((pt[0] + 20 + 1370, pt[1] + 20 + 226))

    cv2.imshow("img", img)
    cv2.waitKey(1)


def main():
    game_window = (1370, 226, 1734, 758)
    im = ImageGrab.grab(game_window)
    im.save(os.getcwd() + '\\screenshot' + '.png', 'PNG')

    find_mana()


if __name__ == '__main__':
    while True:
        if keyboard.is_pressed('q'):
            break
        main()
        time.sleep(0.01)
