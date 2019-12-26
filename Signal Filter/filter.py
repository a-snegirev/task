import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

figure = plt.figure()
time = np.arange(0, 30, 0.01)

def SigGenerate(period):
    sig = np.sin(2 * np.pi / period * time) + 0.5*np.random.sample() * np.random.randn(time.size)
    return sig

common_sig = SigGenerate(1) + SigGenerate(2) + SigGenerate(3)
signal = plt.Axes(figure, [.2, .8, .6, .24])
figure.add_axes(signal)

signal.plot(time,common_sig)
plt.xlabel('time ')
plt.ylabel('amplitude')
print(common_sig)

Fourier = plt.Axes(figure, [.2, .1, .6, .24])
figure.add_axes(Fourier)
spectrum = fftpack.rfft(common_sig)
Fourier.plot(fftpack.rfftfreq(len(time), 1 / 0.01),np.abs(spectrum) / 0.01)
plt.xlabel('frequence')

clean_spectrum = np.array([])
for x in spectrum:
    if np.abs(x) < np.max(np.abs(spectrum))/10:
        x = 0
    clean_spectrum = np.append(clean_spectrum,[x])

clean = plt.Axes(figure, [.2, .5, .6, .24])
figure.add_axes(clean)
clean_sig = fftpack.irfft(clean_spectrum)
clean.plot(time, clean_sig)
plt.xlabel('time ')
plt.ylabel('amplitude')

plt.show()
