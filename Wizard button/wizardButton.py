# coding=UTF-8
import pygetwindow as gw
import ctypes
import time
from pynput import mouse

# Windows API常量
WM_LBUTTONDOWN = 0x0201
WM_LBUTTONUP = 0x0202

shellrun = False


# 调用Windows API函数发送鼠标单击事件
def send_mouse_click(hwnd, x, y):
    # 发送鼠标按下消息
    ctypes.windll.user32.SendMessageW(hwnd, WM_LBUTTONDOWN, 0, x + (y << 16))
    time.sleep(0.1)  # 可根据需要适当调整延迟
    # 发送鼠标释放消息
    ctypes.windll.user32.SendMessageW(hwnd, WM_LBUTTONUP, 0, x + (y << 16))


# 鼠标按下事件回调函数
def on_mouse_press(x, y, button, pressed):
    global shellrun
    try:
        print(button)
        if button == mouse.Button.x1:
            if pressed:
                print('鼠标按下: 鼠标侧键1', '坐标:')
                shellrun = not shellrun
    except Exception as e:
        print('发生异常:', e)


# 获取所有打开的窗口
x = 100
y = 100
window = gw.getWindowsWithTitle('Minecraft* 1.19.4 - 多人游戏（第三方服务器）')[0]
# 创建鼠标监听器
mouse_listener = mouse.Listener(on_click=on_mouse_press)

# 启动监听器
mouse_listener.start()
while 1:

    # 阻塞主线程
    # mouse_listener.join()
    if shellrun is True:
        send_mouse_click(window._hWnd, x, y)
    time.sleep(1)
