# -*- coding: utf-8 -*-


class SysStatus:
    def __init__(self, port=None, baudrate=115200, timeout=1):
        
        self.serial_list = []
        
        # ��Ŵ��������ͽӿڵ��ֵ�
        self.serial_dict = {}

