# -*- coding: utf-8 -*-
import threading
import time

import serial
import serial.tools.list_ports


class SerThread(threading.Thread):
    def __init__(self, port=None):
        super().__init__()
        self.serial = SerialPort(port, baudrate=115200, timeout=0.01)
        self.receive_thread = threading.Thread(target=self.receive_data)
        self.send_thread = threading.Thread(target=self.send_data)
        self.updata_serial_port_thread = threading.Thread(target=self.update_serial_port)
        self.receive_data_flag = False
        self.send_data_flag = False
        self.update_flag = False
        self.data_buffer = ""

        self.portsDict = Ports_dict()

    def receive_data(self):
        while self.receive_data_flag:
            data = self.serial.read_data()
            if data:
                print("Received data:", data)
            else:
                print("No data received.")
            time.sleep(0.1)

    def send_data(self):
        while self.send_data_flag:
            if self.send_data_flag:
                if self.data_buffer:
                    self.serial.write_data(self.data_buffer)
                    self.data_buffer = ""
            time.sleep(0.1)

    def update_serial_port(self):
        while self.update_flag:
            if self.serial.get_serial_dict():
                newportsDict = self.serial.get_serial_dict()
                if self.serial.enumerate_ports():
                    added_ports = [portDescript for portDescript in newportsDict if portDescript not in self.serial_dict]
                    removed_ports = [portDescript for portDescript in self.serial_dict if portDescript not in newportsDict]
                    for port in added_ports:
                        self.portsDict[port] = newportsDict.device
                        print("Added Serial Port: ", port, newportsDict[port])
                    for port in removed_ports:
                        self.portsDict.pop(port)
                        print("Removed Serial Port: ", port, self.serial_dict[port])
                        
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
        self.serial.close()


# 接口信息描述类
class Ports_dict():
    def __init__(self):
        self.port_dict = {}
        # self.port_dict.device = []
        # self.port_dict.descript = []


class SerialPort:
    def __init__(self, port=None, baudrate=115200, timeout=1):
        self.serial = serial.Serial(port, baudrate, timeout=timeout)
        self.serial_list = []

    # 枚举串口并更新到列表
    def enumerate_ports(self):
        new_serial_list = []
        getnewport = False
        ports = serial.tools.list_ports.comports()
        for port in ports:
            new_serial_list.append(port.device)
            if new_serial_list != self.serial_list:
                getnewport = True
                self.serial_list = new_serial_list
                print("Serial ports updated")
        return getnewport

    def get_serial_dict(self):
        serial_dict = {}
        for port in self.serial_list:
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
            print("No open serial port.")

    def read_data(self, num_bytes=1):
        if self.serial and self.serial.is_open:
            try:
                received_data = self.serial.read(num_bytes)
                print(f"Received data: {received_data.decode()}")
                return received_data.decode()
            except serial.SerialException as e:
                print(f"Failed to receive data. Error: {e}")
        else:
            print("No open serial port.")
            return None
