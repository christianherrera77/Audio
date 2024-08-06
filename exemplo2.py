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
sample_rate1 = 400   # samples/s
sample_rate2 = 40   # samples/s
sample_rate3 = 4   # samples/s
frequency = 1       # Hertz (cicles/s)
amplitude = 0.5

###############################################################################
# Waveforms synthesis
#
num_samples_1 = np.round(sample_rate1*end_time)
num_samples_2 = np.round(sample_rate2*end_time)
num_samples_3 = np.round(sample_rate3*end_time)
time_1 = np.zeros(num_samples_1)
time_2 = np.zeros(num_samples_2)
time_3 = np.zeros(num_samples_3)
sinewave_1 = np.zeros(num_samples_1)
sinewave_2 = np.zeros(num_samples_2)
sinewave_3 = np.zeros(num_samples_3)
time_increment_1 = 1/sample_rate1
time_increment_2 = 1/sample_rate2
time_increment_3 = 1/sample_rate3
for s in range(num_samples_1):
    time_1[s] = s * time_increment_1
    sinewave_1[s] = 0.5 * (1 + np.sin(2 * np.pi * frequency * time_1[s]))
for s in range(num_samples_2):
    time_2[s] = s * time_increment_2
    sinewave_2[s] = 0.5 * (1 + np.sin(2 * np.pi * frequency * time_2[s]))
for s in range(num_samples_3):
    time_3[s] = s * time_increment_3
    sinewave_3[s] = 0.5 * (1 + np.sin(2 * np.pi * frequency * time_3[s]))

###############################################################################
# Plot waveforms
#
fig1, ax1 = plt.subplots(3,1)
ax1[0].stem(time_1,sinewave_1)
ax1[0].grid()
ax1[0].set_title('sinewave 1')
ax1[1].stem(time_2,sinewave_2)
ax1[1].grid()
ax1[1].set_title('sinewave 2')
ax1[2].stem(time_3,sinewave_3)
ax1[2].grid()
ax1[2].set_title('sinewave 3')
plt.show()