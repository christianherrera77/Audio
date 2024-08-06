import pyaudio
import wave
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
###############################################################################
# Parameters
#
start_time = 0
end_time = 1
sample_rate = 48000
frequency = 440
amplitude = 1
num_bits = 8

FORMAT = pyaudio.paInt16
CHANNELS = 1
WAVE_OUTPUT_FILENAME = "output.wav"

###############################################################################
# Waveforms synthesis
#
time = np.arange(start_time, end_time, 1/sample_rate) # Time vector
sinewave = amplitude * (np.sin(2 * np.pi * frequency * time)) # Sine waveform
###############################################################################
# Waveform conditioning
#
audio = sinewave * (2**15 - 1) / np.max(np.abs(sinewave)) # Ensure that highest value is in 16-bit range
audio = audio.astype(np.int16) # Convert to 16-bit data
###############################################################################
# Audio playback
#
sd.play(audio, sample_rate)
status = sd.wait()  # Wait until file is done playing
#play_obj = sa.play_buffer(audio, CHANNELS, 2, sample_rate) # Start playback
#play_obj.wait_done() # Wait for playback to finish before exiting
###############################################################################
# Audiofile saving
#
p = pyaudio.PyAudio()
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(sample_rate)
wf.writeframes(bytes(audio))
#wf.writeframes(b''.join(audio))
wf.close()
###############################################################################
# Plot waveforms
#
fig= plt.figure()
#plt.step(time,sinewave, where='post', label='post')
plt.plot(time,audio, 'o--', color='grey', alpha=0.3)
plt.grid()
plt.show()
