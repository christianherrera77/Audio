###############################################################################
# Exemplo 1
#
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

###############################################################################
# Parameters
#
start_time = 0      # s
end_time = 1        # s
sample_rate = 200   # samples/s
frequency = 1       # Hertz (cicles/s)
amplitude = 0.5

###############################################################################
# Waveforms synthesis
#
num_samples = np.round(sample_rate*end_time)
time = np.zeros(num_samples)
sinewave = np.zeros(num_samples)
sinewave_2bits = np.zeros(num_samples, dtype=int)
sinewave_3bits = np.zeros(num_samples, dtype=int)
sinewave_4bits = np.zeros(num_samples, dtype=int)
time_increment = 1/sample_rate
for s in range(num_samples):
    time[s] = s * time_increment
    sinewave[s] = 0.5 * (1 + np.sin(2 * np.pi * frequency * time[s]))
    sinewave_4bits[s] = np.round(sinewave[s] * (2**4-1))
    sinewave_2bits[s] = np.round(sinewave[s] * (2**2-1))
    sinewave_3bits[s] = np.round(sinewave[s] * (2**3-1))

###############################################################################
# Plot waveforms
#
fig1, ax1 = plt.subplots(2,2)
ax1[0, 0].step(time,sinewave, where='post', label='post')
ax1[0, 0].grid()
ax1[0, 0].set_title('sinewave')
ax1[0, 1].step(time,sinewave_2bits, where='post', label='post')
ax1[0, 1].grid()
#ax1[0, 1].set_ylim(bottom=0, top=16)
ax1[0, 1].set_title('sinewave_2bits')
ax1[1, 0].step(time,sinewave_3bits, where='post', label='post')
ax1[1, 0].grid()
#ax1[1, 0].set_ylim(bottom=0, top=256)
ax1[1, 0].set_title('sinewave_3bits')
ax1[1, 1].step(time,sinewave_4bits, where='post', label='post')
ax1[1, 1].grid()
#ax1[1, 1].set_ylim(bottom=0, top=2**12)
ax1[1, 1].set_title('sinewave_4bits')
plt.show()