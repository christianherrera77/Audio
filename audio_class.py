###############################################################################
# Sintetiza um sinal senoidal e plota.
#
import pyaudio
import wave
import numpy as np
import simpleaudio as sa
import matplotlib.pyplot as plt
###############################################################################
# Parameters
#
start_time = 0
end_time = 1
sample_rate = 200
theta = 0
frequency = 1
amplitude = 0.5

num_bits = 8

#modulation_index = 0
#modulation_freq = 0.1
#FORMAT = pyaudio.paInt16
#CHANNELS = 2
#WAVE_OUTPUT_FILENAME = "output.wav"
###############################################################################
# Waveforms synthesis
#
time = np.arange(start_time, end_time, 1/sample_rate) # Time vector
sinewave = amplitude * (1 + np.sin(2 * np.pi * frequency * time + theta)) # Sine waveform
sinewave = np.round(sinewave*(2**num_bits))
#modwave = modulation_index * np.sin(2 * np.pi * modulation_freq * time + theta)
#finalwave = sinewave * modwave
###############################################################################
# Waveform conditioning
#
#audio = finalwave * (2**15 - 1) / np.max(np.abs(finalwave)) # Ensure that highest value is in 16-bit range
#audio = audio.astype(np.int16) # Convert to 16-bit data
###############################################################################
# Audio playback
#
#play_obj = sa.play_buffer(audio, CHANNELS, 2, sample_rate) # Start playback
#play_obj.wait_done() # Wait for playback to finish before exiting
###############################################################################
# Audiofile saving
#
#p = pyaudio.PyAudio()

#wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#wf.setnchannels(CHANNELS)
#wf.setsampwidth(p.get_sample_size(FORMAT))
#wf.setframerate(sample_rate)
#wf.writeframes(b''.join(audio))
#wf.close()
###############################################################################
# Plot waveforms
#
fig= plt.figure(figsize=(18,6))
plt.step(time,sinewave, where='post', label='post')
plt.plot(time,sinewave, 'o--', color='grey', alpha=0.3)
plt.grid()
#plt.plot(time,modwave)
#plt.plot(time,finalwave)
#plt.plot(time,audio)
plt.show()

