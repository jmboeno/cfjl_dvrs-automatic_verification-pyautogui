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
    pyautogui.write('http://192.168.20.51:55107')
    pyautogui.press('enter')

    time.sleep(3)
    pyautogui.write(USER_DVR)
    pyautogui.press('TAB')
    pyautogui.write(PASSWORD_DVR)
    pyautogui.press('enter')

    time.sleep(4)
    pyautogui.click('./buttons/all-layout.PNG')
    pyautogui.click('./buttons/open-all-cams.PNG')
    pyautogui.click('./buttons/extend-layout.PNG')
    pyautogui.screenshot('./images/192.168.20.51_ALLCAMS.png')
    pyautogui.press('esc')
    pyautogui.click('./buttons/vizualization-close.PNG')
    pyautogui.click('./buttons/reprodution-open.PNG')

    time.sleep(2)
    pyautogui.click(1333, 610)

    time.sleep(2)
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')

    pyautogui.click('./buttons/btn-play.PNG')
    pyautogui.screenshot('./images/192.168.20.51_CAM1.png',
                         region=(65, 79, 1300, 690))
    pyautogui.click('./buttons/btn-pause.PNG')

    i = 2
    while i <= 6:
        pyautogui.click(1333, 610)
        pyautogui.press('down')
        pyautogui.click('./buttons/btn-play.PNG')
        pyautogui.screenshot('./images/192.168.20.51_CAM' +
                             str(i)+'.png', region=(63, 79, 1300, 690))
        pyautogui.click('./buttons/btn-pause.PNG')
        i = i + 1

    pyautogui.hotkey('alt', 'F4')
