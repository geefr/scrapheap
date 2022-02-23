
import sys
import numpy as np
import sounddevice as sd
import time

if __name__ == '__main__':
    sentence=input("Enter a sentence: ")
    if not sentence:
       sys.exit(1)

    sentence = sentence.replace("\t", "    ")
    sentence = sentence.replace(".", " ")
    sentence = sentence.replace("\n", "        ")

    bip_length = 0.025
    bop_length = 0.02
    nuh_length = 0.1
    bip_freq = 600
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

    print("\n\n")

    sd.play(s, sample_rate)

    while sentence:
        c = sentence[0]

        if not c.isspace():
            t = bip_length + bop_length
        else:
            t = nuh_length
        next_time = time.time() + t

        sys.stdout.write(c)
        sys.stdout.flush()
        sentence = sentence[1:]

        sleep_time = next_time - time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)

    sd.wait()

    print("\n\n")

