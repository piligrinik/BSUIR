import numpy as np
import matplotlib.pyplot as plt

def compute_fft(signal):
    return np.fft.fft(signal)

#
N = 1024  # точки
T = 1.0 / 800.0  # timw
x = np.linspace(0.0, N*T, N, endpoint=False)  # массив знач

frequency = 15 #                          may be changed
signal = np.sin(2.0 * np.pi * frequency * x)

fft_result = compute_fft(signal)

# частоты
frequencies = np.fft.fftfreq(N, T)[:N // 2]

# амплитуда
magnitude = np.abs(fft_result)[:N // 2]

plt.figure(figsize=(12, 6))


plt.subplot(2, 1, 1)
plt.plot(x, signal)
plt.title('Исходный сигнал: sin(2π * {} * x)'.format(frequency))
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда')

plt.subplot(2, 1, 2)
plt.plot(frequencies, magnitude)
plt.title('Спектр частот')
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда')

plt.tight_layout()
plt.show()