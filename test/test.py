import ctypes
import time
import win32api, win32con
import pyautogui as pg


user32 = ctypes.windll.user32


def user32_delete():
    for i in range(20):
        user32.keybd_event(0x08, 0, 0, 0)
        user32.keybd_event(0x08, 0, win32con.KEYEVENTF_KEYUP, 0)

def Delete():
    for i in range(20):
        win32api.keybd_event(0x08, 0, 0, 0)
        win32api.keybd_event(0x08, 0, win32con.KEYEVENTF_KEYUP, 0)
def space():
    pg.press('backspace')


# time.sleep(2)
# a = time.time()
# for i in range(1000):
#     Delete()
# b = time.time()
# print(b-a, 'Delete')
#
# time.sleep(1)
# a = time.time()
# for i in range(1000):
#     user32_delete()
# b = time.time()
# print(b-a, 'user32_delete')