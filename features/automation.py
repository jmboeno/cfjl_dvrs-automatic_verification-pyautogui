import pyautogui
import time
from config.constants import USER_DVR, PASSWORD_DVR, DIR_BTNS, DIR_IMAGES

pyautogui.PAUSE = 2
pyautogui.PAUSE = True


def checkDvr(ip, qtd_cams, modelo):

    print("Iniciar verificação no DVR " + modelo + " IP: " + ip)
    pyautogui.hotkey('win', 'r')
    pyautogui.write('c:\program files\internet explorer\iexplore.exe')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'o')
    pyautogui.write(ip)
    pyautogui.press('enter')
    time.sleep(3)

    if modelo == 'MHDX 1208':
        pyautogui.write(USER_DVR)
        pyautogui.press('TAB')
        pyautogui.write(PASSWORD_DVR)
        pyautogui.press('enter')
        time.sleep(4)
        pyautogui.click(DIR_BTNS+'all-layout.PNG')
        pyautogui.click(DIR_BTNS+'open-all-cams.PNG')
        pyautogui.click(DIR_BTNS+'extend-layout.PNG')
        pyautogui.screenshot(DIR_IMAGES+'192.168.20.51_ALLCAMS.png')
        pyautogui.press('esc')
        pyautogui.click(DIR_BTNS+'vizualization-close.PNG')
        pyautogui.click(DIR_BTNS+'reprodution-open.PNG')
        time.sleep(2)
        pyautogui.click(1333, 610)
        time.sleep(2)
        pyautogui.press('up')
        pyautogui.press('up')
        pyautogui.press('up')
        pyautogui.click(DIR_BTNS+'btn-play.PNG')
        pyautogui.screenshot(DIR_IMAGES+'192.168.20.51_CAM1.png',
                             region=(65, 79, 1300, 690))
        pyautogui.click(DIR_BTNS+'btn-pause.PNG')
        i = 2
        while i <= qtd_cams:
            pyautogui.click(1333, 610)
            pyautogui.press('down')
            pyautogui.click(DIR_BTNS+'btn-play.PNG')
            pyautogui.screenshot(DIR_IMAGES+'192.168.20.51_CAM' +
                                 str(i)+'.png', region=(63, 79, 1300, 690))
            pyautogui.click(DIR_BTNS+'btn-pause.PNG')
            i = i + 1

    if modelo == 'MHDX 3016-C':
        pyautogui.click(700, 360)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('DEL')
        pyautogui.write(USER_DVR)
        pyautogui.press('TAB')
        pyautogui.write(PASSWORD_DVR)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.screenshot(DIR_IMAGES+'192.168.20.52_ALLCAMS_ERRO_HD.png',
                             region=(63, 79, 1300, 690))
        pyautogui.click(770, 466)
        pyautogui.click(DIR_BTNS+'down-cams-2.PNG', clicks=2)
        pyautogui.click(596, 673)
        pyautogui.click(DIR_BTNS+'open-all-cams-2.PNG')
        pyautogui.click(DIR_BTNS+'extend-layout-2.PNG')
        pyautogui.screenshot(DIR_IMAGES+'192.168.20.52_ALLCAMS.png')
        pyautogui.press('esc')
        pyautogui.click(DIR_BTNS+'vizualization-close-2.PNG')
        pyautogui.click(1350, 100, clicks=2)
        pyautogui.click(550, 125)
        time.sleep(2)
        pyautogui.click(DIR_BTNS+'one-cam-layout.PNG')
        pyautogui.click(DIR_BTNS+'btn-play-2.PNG')
        pyautogui.screenshot(DIR_IMAGES+'192.168.20.52_CAM1.png',
                             region=(63, 79, 1300, 690))
        pyautogui.click(DIR_BTNS+'btn-pause-2.PNG')
        pyautogui.click(DIR_BTNS+'down-cams-rec-2.PNG')
        i = 2
        position_cam = 555
        while i <= qtd_cams:
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
            pyautogui.click(DIR_BTNS+'btn-play-2.PNG')
            pyautogui.screenshot(DIR_IMAGES+'192.168.20.52_CAM' +
                                 str(i)+'.png', region=(63, 79, 1300, 690))
            pyautogui.click(DIR_BTNS+'btn-pause-2.PNG')
            if i != qtd_cams:
                pyautogui.click(DIR_BTNS+'down-cams-rec-2.PNG')
            i += 1

    pyautogui.hotkey('alt', 'F4')
