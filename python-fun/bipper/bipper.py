
import sys
import numpy as np
import sounddevice as sd

if __name__ == '__main__':
    sentence=input("Enter a sentence: ")
    if not sentence:
        sys.exit(1)

    bip_length = 0.1
    bop_length = 0.025
    nuh_length = 0.2
    bip_freq = 300
    sample_rate = 48000

    t = np.empty(0)
    s = np.empty(0)
    
    t_bip = np.arange(0.0, bip_length, 1/sample_rate)
    bip = np.sin(2 * np.pi * bip_freq * t_bip)
    bop = np.zeros(int(bop_length * sample_rate))
    nuh = np.zeros(int(nuh_length * sample_rate))

    for c in sentence:
        if not c.isspace():
            s = np.append(s, bip)
            s = np.append(s, bop)
        else:
            s = np.append(s, nuh)

    sd.play(s, sample_rate)
    sd.wait()

