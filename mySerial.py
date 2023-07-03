# -*- coding: utf-8 -*-
import threading
import time

import serial
import serial.tools.list_ports


class SerThread(threading.Thread):
    def __init__(self, port=None, comb=None):
        super().__init__()
        # 绑定窗体的下拉列表
        self.comb = comb
        
        # 初始化串口句柄
        self.serialPort = SerialPort(port, baudrate=4800, timeout=0.01)
        self.serialPort.serial.stopbits = serial.STOPBITS_TWO
        
        # 绑定串口接收、发送、更新进程回调函数
        self.receive_thread = threading.Thread(target=self.receive_data)
        self.send_thread = threading.Thread(target=self.send_data)
        self.updata_serial_port_thread = threading.Thread(target=self.update_serial_port)
        
        # 串口接收、发送、更新进程开启标志
        self.receive_data_flag = False
        self.send_data_flag = False
        self.update_flag = False
        
        # 接收数据缓存
        self.data_buffer = ""

    def receive_data(self):
        while self.receive_data_flag:
            data = self.serialPort.read_data()
            if data:
                print("Received data:", data)
            else:
                # print("No data received.")
                pass
            time.sleep(0.1)

    def send_data(self):
        while self.send_data_flag:
            if self.send_data_flag:
                if self.data_buffer:
                    self.serialPort.write_data(self.data_buffer)
                    self.data_buffer = ""
            time.sleep(0.1)

    def update_serial_port(self):
        while self.update_flag:
            if self.serialPort.enumerate_ports():
                print("get New Serial port")
                self.comb.clear()
                self.comb.addItems(self.serialPort.serial_descript_list)
            time.sleep(0.1)

    def run(self):
        self.receive_data_flag = True
        self.send_data_flag = True
        self.update_flag = True
        self.receive_thread.start()
        self.send_thread.start()
        self.updata_serial_port_thread.start()

    def stop(self):
        self.receive_data_flag = False
        self.send_data_flag = False
        self.update_flag = False
        self.receive_thread.join()
        self.send_thread.join()
        self.updata_serial_port_thread.join()
        self.serialPort.serial.close()


class SerialPort:
    def __init__(self, port=None, baudrate=115200, timeout=1):
        self.serial = serial.Serial(port, baudrate, timeout=timeout)
        
        self.serial_list = []
        self.serial_descript_list = []
        
        # 存放串口描述和接口的字典
        self.serial_dict = {}

    # 枚举串口并更新到列表
    def enumerate_ports(self):
        # 串口表有更新标志
        getnewport = False
        # 获取串口表
        new_serial_list = serial.tools.list_ports.comports()
        if new_serial_list != self.serial_list:
            getnewport = True
            print("Serial ports updated")
        # 如果串口有变动，更新串口列表和串口词典
        if getnewport:
            self.serial_list = new_serial_list
            self.updata_serial_dict()
        return getnewport

    def updata_serial_dict(self):
        newDict = self.make_serial_dict()  # 获取最新的串口字典
        
        # 比较新旧字典变动
        added_ports = [portDescript for portDescript in newDict if portDescript not in self.serial_dict]
        removed_ports = [portDescript for portDescript in self.serial_dict if portDescript not in newDict]
        
        # 更新旧字典内容
        for port in added_ports:
            self.serial_dict[port] = newDict[port]
            print("Added Serial Port: ", port, newDict[port])
        for port in removed_ports:
            self.serial_dict.pop(port)
            print("Removed Serial Port: ", port)

    # 创建字典 description ： device
    def make_serial_dict(self):
        serial_dict = {}
        self.serial_descript_list = []
        for port in self.serial_list:
            self.serial_descript_list.append(port.description)
            serial_dict[port.description] = port.device
        return serial_dict

    def set_ports(self, port):
        self.port = port

    def set_baudrate(self, baudrate):
        self.baudrate = baudrate

    def set_stopbits(self, stopbits):
        self.stopbits = stopbits

    def open_port(self):
        try:
            self.serial = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            if self.serial.is_open:
                print(f"Serial port {self.port} opened successfully.")
        except serial.SerialException as e:
            print(f"Failed to open serial port {self.port}. Error: {e}")

    def close_port(self):
        if self.serial and self.serial.is_open:
            self.serial.close()
            print(f"Serial port {self.port} closed.")
        else:
            print("No open serial port.")

    def write_data(self, data):
        if self.serial and self.serial.is_open:
            try:
                self.serial.write(data.encode())
                print(f"Sent data: {data}")
            except serial.SerialException as e:
                print(f"Failed to send data. Error: {e}")
        else:
            pass
            # print("No open serial port.")

    def read_data(self, num_bytes=1):
        if self.serial and self.serial.is_open:
            try:
                received_data = None
                received_data = self.serial.readline()
                if received_data:
                    print(f"Received data: {received_data.decode()}")
                    return received_data.decode()
                else:
                    # print("No open serial port.")
                    return None
            except BaseException as e:
                print(f"Failed to receive data. Error: {e}")
        else:
            return None
