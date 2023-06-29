import serial.tools.list_ports

# ö�ٴ��ڲ����ش����ֵ�
def enumerate_serial_ports():
    ports = list(serial.tools.list_ports.comports())
    serial_dict = {}
    for port in ports:
        serial_dict[port.description] = port.device
    return serial_dict

# ��ʼ�������ֵ�
serial_dict = enumerate_serial_ports()

# ��̬ͬ�����´����ֵ�
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

# ʾ�������ڵ��ø��º���
while True:
    update_serial_dict()
    # ִ����������...