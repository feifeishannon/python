import matplotlib.pyplot as plt
import numpy as np

# ��������
amplitude = 1.0    # ���
frequency = 5.0    # Ƶ�ʣ���������
num_samples = 300  # ��������
sampling_rate = 1000  # ������

# ����ʱ������
time = np.linspace(0, (num_samples - 1) / sampling_rate, num_samples)

# �������Ҳ�������
sin_waveform = amplitude * np.sin(2 * np.pi * frequency * time)

# ���Ʋ���ͼ
plt.plot(time, sin_waveform)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sinusoidal Waveform')
plt.grid(True)
plt.show()
