import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

plt.style.use('ggplot')

fs, x = wavfile.read('audio.wav')

f, t, S = signal.spectrogram(x, fs)
plt.figure(figsize=(10, 10))
plt.pcolormesh(t, f, S)
plt.ylabel('freq [Hz]')
plt.xlabel('time [s]')
plt.show()

w = len(t) // 32
s = 22
plt.plot(f, np.mean(S[:, w*s:w*(s+1)], axis=1))
plt.grid(False)
plt.xlabel('freq')
plt.ylabel('amp')
plt.show()

# https://en.wikipedia.org/wiki/Dual-tone_multi-frequency_signaling
tones = {
    '1': (1209, 697),
    '2': (1336, 697),
    '3': (1477, 697),
    '4': (1209, 770),
    '5': (1336, 770),
    '6': (1477, 770),
    '7': (1209, 852),
    '8': (1336, 852),
    '9': (1477, 852),
    '*': (1209, 941),
    '0': (1336, 941),
    '#': (1477, 941),
    'A': (1633, 697),
    'B': (1633, 770),
    'C': (1633, 852),
    'D': (1633, 941),
}

def prob_tone(sig, tn, fs):
    res = 0
    for t in tn:
        f_idx = np.argmin(np.abs(fs - t))
        res += sig[f_idx]
    return res / len(tn)

w = len(t) // 32  # tone width, empirically determined
res = ''
for i, s in enumerate(range(t.shape[0]//w)):
    sig = np.sum(S[:, w*s:w*(s+1)], axis=1)
    best_lk = 0
    best_n = None
    for n in tones:
        lk = prob_tone(sig, tones[n], f)
        if lk > best_lk:
            best_lk = lk
            best_n = n
    res += best_n

res

'658AD5B581AD1B556123A845523178AA'
