import pyautogui
import time

from ..contants import PASSWORD_DVR, USER_DVR

pyautogui.PAUSE = 2.5
pyautogui.PAUSE = True


def verDvr():
    pyautogui.hotkey('win', 'r')
    pyautogui.write('c:\program files\internet explorer\iexplore.exe')
    pyautogui.press('enter')

    time.sleep(2)
    pyautogui.hotkey('ctrl', 'o')
    pyautogui.write('http://192.168.20.52:55110/')
    pyautogui.press('enter')

    time.sleep(3)
    pyautogui.click(700, 360)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('DEL')
    pyautogui.write(USER_DVR)
    pyautogui.press('TAB')
    pyautogui.write(PASSWORD_DVR)
    pyautogui.press('enter')

    time.sleep(2)
    pyautogui.screenshot('./cams/192.168.20.52_ALLCAMS_ERRO_HD.png',
                         region=(63, 79, 1300, 690))
    pyautogui.click(770, 466)
    pyautogui.click('./buttons/down-cams-2.PNG', clicks=2)
    pyautogui.click(596, 673)
    pyautogui.click('./buttons/open-all-cams-2.PNG')
    pyautogui.click('./buttons/extend-layout-2.PNG')
    pyautogui.screenshot('./cams/192.168.20.52_ALLCAMS.png')
    pyautogui.press('esc')
    pyautogui.click('./buttons/vizualization-close-2.PNG')
    pyautogui.click(1350, 100, clicks=2)
    pyautogui.click(550, 125)

    time.sleep(2)
    pyautogui.click('./buttons/one-cam-layout.PNG')
    pyautogui.click('./buttons/btn-play-2.PNG')
    pyautogui.screenshot('./cams/192.168.20.52_CAM1.png',
                         region=(63, 79, 1300, 690))
    pyautogui.click('./buttons/btn-pause-2.PNG')
    pyautogui.click('./buttons/down-cams-rec-2.PNG')

    i = 2
    position_cam = 555
    while i <= 13:

        if i <= 6:
            pyautogui.click(1205, position_cam)
            position_cam += 25
        if i == 7 or i == 9 or i == 10 or i == 11 or i == 12:
            pyautogui.click(1260, 655)
            pyautogui.click(1205, 655)
        if i == 8 or i == 13:
            pyautogui.click(1260, 655)
            pyautogui.click(1260, 655)
            pyautogui.click(1205, 655)

        pyautogui.click('./buttons/btn-play-2.PNG')
        pyautogui.screenshot('./cams/192.168.20.52_CAM' +
                             str(i)+'.png', region=(63, 79, 1300, 690))
        pyautogui.click('./buttons/btn-pause-2.PNG')

        if i != 13:
            pyautogui.click('./buttons/down-cams-rec-2.PNG')

        i += 1

    pyautogui.hotkey('alt', 'F4')
