import numpy as np
import scipy as sp
from scipy.io.wavfile import read
from scipy.io.wavfile import write
from scipy import signal
import matplotlib.pyplot as plt
# from IPython import get_ipython

# get_ipython().magic('matplotlib inline')

(Frequency, array) = read('my_record/1.wav')

len(array)

plt.plot(array)
plt.title('Original Signal Spectrum')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')

FourierTransformation = sp.fft(array)

scale = sp.linspace(0, Frequency, len(array))

plt.stem(scale[0:5000], np.abs(FourierTransformation[0:5000]), 'r')
plt.title('Signal spectrum after FFT')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')


GuassianNoise = np.random.randn(len(FourierTransformation))


NewSound = GuassianNoise + array

write("New-Sound-Added-With-Guassian-Noise.wav", Frequency, NewSound)

b, a = signal.butter(5, 1000/(Frequency/2), btype='highpass')

filteredSignal = signal.lfilter(b, a, NewSound)
plt.plot(filteredSignal)  # plotting the signal.
plt.title('Highpass Filter')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')


# ButterWorth low-filter
c, d = signal.butter(5, 380/(Frequency/2), btype='lowpass')
# Applying the filter to the signal
newFilteredSignal = signal.lfilter(c, d, filteredSignal)
plt.plot(newFilteredSignal)  # plotting the signal.
plt.title('Lowpass Filter')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')

write("New-Filtered-Sound.wav", Frequency, newFilteredSignal)
