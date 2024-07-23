import sounddevice as sd
import soundfile as sf
import numpy as np
import simpleaudio as sa
import matplotlib.pyplot as plt
###############################################################################
# Parameters
#
filename1 = 'Audio/waves/VOZ.wav'
###############################################################################
# Open WAVE file
#
voz, fs1 = sf.read(filename1, dtype='float32')  # Extract data and sampling rate from file
###############################################################################
# Normalize WAVE data
#
voz = voz/np.max(np.abs(voz))
###############################################################################
# Requantize WAVE data
#
voz_3bit = np.round(voz * (2**2-1)) / (2**2-1)
voz_5bit = np.round(voz * (2**4-1)) / (2**4-1)
voz_8bit = np.round(voz * (2**7-1)) / (2**7-1)
###############################################################################
# Play WAVE file
#
sd.play(voz, fs1)
status = sd.wait()  # Wait until file is done playing
sd.play(voz_3bit, fs1)
status = sd.wait()  # Wait until file is done playing
sd.play(voz_5bit, fs1)
status = sd.wait()  # Wait until file is done playing
sd.play(voz_8bit, fs1)
status = sd.wait()  # Wait until file is done playing
###############################################################################
# Plot waveforms
#
fig1, ax1 = plt.subplots(2,2)
ax1[0, 0].plot(voz)
ax1[0, 0].set_ylim(bottom=-1, top=1)
ax1[0, 0].set_title('voz original')
ax1[0, 0].grid()
ax1[0, 1].plot(voz_3bit)
ax1[0, 1].set_ylim(bottom=-1, top=1)
ax1[0, 1].set_title('voz 3 bits')
ax1[0, 1].grid()
ax1[1, 0].plot(voz_5bit)
ax1[1, 0].set_ylim(bottom=-1, top=1)
ax1[1, 0].set_title('voz 5 bits')
ax1[1, 0].grid()
ax1[1, 1].plot(voz_8bit)
ax1[1, 1].set_ylim(bottom=-1, top=1)
ax1[1, 1].set_title('voz 8 bits')
ax1[1, 1].grid()
plt.show()