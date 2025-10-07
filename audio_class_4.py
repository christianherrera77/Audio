###############################################################################
# Abre um arquivo de áudio com um sinal de voz
# Normaliza e filtra o sinal de voz
#
import matplotlib.pyplot as plt
import numpy as np
import wave
import simpleaudio as sa

###############################################################################
# Open Audio from Wav File 
spf = wave.open('VOZ.wav','r')

###############################################################################
# Extract Raw Audio from Wav File 
signal_raw = spf.readframes(-1)
signal_raw = np.frombuffer(signal_raw, 'int16')
# maps raw audio in +1/-1 range
signal = signal_raw/(2**15)
# and normalize
signal_normalized = signal/np.max(np.abs(signal))
###############################################################################
# Waveform processing
signal_processed = np.zeros(len(signal))
for s in range(len(signal)-1):
    signal_processed[s+1] = signal_normalized[s+1] - 1.4*signal_normalized[s]

###############################################################################
# Waveform conditioning
audio_normalized = signal_normalized * (2**15 - 1)
audio_normalized = audio_normalized.astype(np.int16) # Convert to 16-bit data
audio_processed = signal_processed * (2**15 - 1)
audio_processed = audio_processed.astype(np.int16) # Convert to 16-bit data
###############################################################################
# Audio playback
#play_obj = sa.play_buffer(signal_raw, 1, 2, 44100) # Start playback
#play_obj.wait_done() # Wait for playback to finish before exiting
play_obj = sa.play_buffer(audio_normalized, 1, 2, 44100) # Start playback
play_obj.wait_done() # Wait for playback to finish before exiting
play_obj = sa.play_buffer(audio_processed, 1, 2, 44100) # Start playback
play_obj.wait_done() # Wait for playback to finish before exiting
###############################################################################
# Plot audio signals
fig1, ax1 = plt.subplots(2,2)
ax1[0, 0].plot(signal_raw)
ax1[0, 0].grid()
ax1[0, 0].set_title('signal_raw')
ax1[0, 1].plot(signal)
ax1[0, 1].set_ylim(bottom=-1, top=1)
ax1[0, 1].grid()
ax1[0, 1].set_title('signal')
ax1[1, 0].plot(signal_normalized)
ax1[1, 0].grid()
ax1[1, 0].set_title('signal_normalized')
ax1[1, 0].set_ylim(bottom=-1, top=1)
ax1[1, 1].plot(signal_processed)
ax1[1, 1].grid()
ax1[1, 1].set_title('signal_processed')
ax1[1, 1].set_ylim(bottom=-1, top=1)
plt.show()

