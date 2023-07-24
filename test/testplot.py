import matplotlib.pyplot as plt
import numpy as np

# 参数设置
amplitude = 1.0    # 振幅
frequency = 5.0    # 频率（周期数）
num_samples = 300  # 样本点数
sampling_rate = 1000  # 采样率

# 生成时间序列
time = np.linspace(0, (num_samples - 1) / sampling_rate, num_samples)

# 生成正弦波形数列
sin_waveform = amplitude * np.sin(2 * np.pi * frequency * time)

# 绘制波形图
plt.plot(time, sin_waveform)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sinusoidal Waveform')
plt.grid(True)
plt.show()
