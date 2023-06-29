import threading
import time
import tkinter as tk
from tkinter import ttk

import serial
import serial.tools.list_ports

added_ports = [port for port in new_serial_dict if port not in serial_dict]
            removed_ports = [port for port in serial_dict if port not in new_serial_dict]
# 串口操作类
class SerialPort:
    def __init__(self, port):
        self.port = port
        self.serial = None

    def open(self):
        try:
            self.serial = serial.Serial(self.port, 9600)  # 使用波特率9600打开串口
            print(f"串口 {self.port} 已打开")
        except serial.SerialException as e:
            print(f"无法打开串口 {self.port}: {e}")

    def close(self):
        if self.serial and self.serial.is_open:
            self.serial.close()
            print(f"串口 {self.port} 已关闭")


# 获取串口列表的线程
class SerialListThread(threading.Thread):
    def __init__(self, combo):
        threading.Thread.__init__(self)
        self.combo = combo
        self.stop_event = threading.Event()

    def run(self):
        while not self.stop_event.is_set():
            ports = serial.tools.list_ports.comports()
            port_names = [port.device for port in ports]
            self.combo['values'] = port_names
            time.sleep(1)

    def stop(self):
        self.stop_event.set()


# 主应用程序
class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("串口工具")
        self.geometry("300x200")

        # 下拉列表框
        self.combo = ttk.Combobox(self)
        self.combo.pack(pady=10)
        self.combo.bind("<<ComboboxSelected>>", self.on_combo_select)

        # 打开按钮
        self.open_button = tk.Button(self, text="打开串口", command=self.open_serial)
        self.open_button.pack(pady=10)

        # 关闭按钮
        self.close_button = tk.Button(self, text="关闭串口", command=self.close_serial)
        self.close_button.pack(pady=10)

        # 创建串口列表线程
        self.serial_thread = SerialListThread(self.combo)
        self.serial_thread.start()

    def update_ports(self, port_names):
        self.combo["values"] = port_names

    def on_combo_select(self, event):
        selected_port = self.combo.get()
        print(f"选择串口: {selected_port}")

    def open_serial(self):
        selected_port = self.combo.get()
        if selected_port:
            port = SerialPort(selected_port)
            port.open()

    def close_serial(self):
        selected_port = self.combo.get()
        if selected_port:
            port = SerialPort(selected_port)
            port.close()

    def destroy(self):
        self.serial_thread.stop()  # 停止串口列表线程
        self.serial_thread.join()  # 等待线程退出
        super().destroy()


# 启动应用程序
app = Application()
app.mainloop()
