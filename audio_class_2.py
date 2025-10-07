###############################################################################
# Abre um arquivo com um sinal de voz e um sinal de ruído 
# Soma os dois sinais
#
import pyaudio
import wave
import sounddevice as sd
import soundfile as sf
import numpy as np
import simpleaudio as sa
import matplotlib.pyplot as plt
###############################################################################
# Parameters
#
filename1 = 'VOZ.wav'
#filename2 = 'brown_noise.wav'
#filename2 = 'pink_noise.wav'
filename2 = 'white_noise.wav'
amp_voz = 1.0
amp_ruido = 0.8
###############################################################################
# Play WAVE file
#
# Extract data and sampling rate from file
voz_raw, fs1 = sf.read(filename1, dtype='float32')  
voz = amp_voz * voz_raw
ruido_raw, fs2 = sf.read(filename2, dtype='float32') 
ruido = amp_ruido * ruido_raw
data_output = voz + ruido 
sd.play(voz, fs1)
status = sd.wait()  # Wait until file is done playing
sd.play(ruido, fs2)
status = sd.wait()  # Wait until file is done playing
sd.play(data_output, fs2)
status = sd.wait()  # Wait until file is done playing
###############################################################################
# Plot waveforms
#
fig1, ax1 = plt.subplots(2,2)
ax1[0, 0].plot(data_output)
ax1[0, 0].set_ylim(bottom=-1, top=1)
ax1[0, 0].set_title('voz + ruído')
ax1[0, 1].plot(voz)
ax1[0, 1].set_ylim(bottom=-1, top=1)
ax1[0, 1].set_title('voz')
ax1[1, 0].plot(ruido)
ax1[1, 0].set_ylim(bottom=-1, top=1)
ax1[1, 0].set_title('ruído')
plt.show()
###############################################################################
# Plot frequency spectrum
#
data_output_fft = np.fft.fft(data_output[0:4095])
voz_fft = np.fft.fft(voz[0:4095])
ruido_fft = np.fft.fft(ruido[0:4095])
freq_vector = np.arange(0, 44100, 44100 / 4095)
fig2, ax2 = plt.subplots(2,2)
ax2[0, 0].semilogx(freq_vector, 20*np.log10(np.abs(data_output_fft)))
ax2[0, 0].set_xlim(left=20, right=10000)
ax2[0, 0].set_ylim(bottom=-20, top=40)
ax2[0, 0].grid()
ax2[0, 0].set_title('voz + ruído')
ax2[0, 1].semilogx(freq_vector, 20*np.log10(np.abs(voz_fft)))
ax2[0, 1].set_xlim(left=20, right=10000)
ax2[0, 1].set_ylim(bottom=-20, top=40)
ax2[0, 1].grid()
ax2[0, 1].set_title('voz')
ax2[1, 0].semilogx(freq_vector, 20*np.log10(np.abs(ruido_fft)))
ax2[1, 0].set_xlim(left=20, right=10000)
ax2[1, 0].set_ylim(bottom=-20, top=40)
ax2[1, 0].grid()
ax2[1, 0].set_title('ruído')

plt.show()
