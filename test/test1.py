import serial.tools.list_ports


# 枚举串口并返回串口字典
def enumerate_serial_ports():
    ports = list(serial.tools.list_ports.comports())
    serial_dict = {}
    for port in ports:
        serial_dict[port.description] = port.device
    return serial_dict


# 初始化串口字典
serial_dict = enumerate_serial_ports()


# 动态同步更新串口字典
def update_serial_dict():
    global serial_dict
    new_serial_dict = enumerate_serial_ports()
    if new_serial_dict != serial_dict:
        print("Serial ports updated:")
        added_ports = [port for port in new_serial_dict if port not in serial_dict]
        removed_ports = [port for port in serial_dict if port not in new_serial_dict]
        for port in added_ports:
            print("Added Serial Port: ", port, new_serial_dict[port])
        for port in removed_ports:
            print("Removed Serial Port: ", port, serial_dict[port])
        serial_dict = new_serial_dict


# 示例：定期调用更新函数
while True:
    update_serial_dict()
    # 执行其他操作...