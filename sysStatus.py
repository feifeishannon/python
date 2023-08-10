# -*- coding: utf-8 -*-


class SysStatus:
    def __init__(self, port=None, baudrate=115200, timeout=1):
        
        self.serial_list = []
        
        # 存放串口描述和接口的字典
        self.serial_dict = {}

