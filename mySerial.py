# -*- coding: utf-8 -*-
import serial
import serial.tools.list_ports


class SerialPort:
    def __init__(self, port=None, baudrate=115200, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial = None

    def enumerate_ports(self):
        ports = serial.tools.list_ports.comports()
        available_ports = []
        for port in ports:
            available_ports.append(port.device)
        # port_list = [port.device for port in ports]
        return available_ports

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

    def send_data(self, data):
        if self.serial and self.serial.is_open:
            try:
                self.serial.write(data.encode())
                print(f"Sent data: {data}")
            except serial.SerialException as e:
                print(f"Failed to send data. Error: {e}")
        else:
            print("No open serial port.")

    def receive_data(self, num_bytes=1):
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
