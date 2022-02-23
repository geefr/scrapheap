
import sys
import numpy as np
import sounddevice as sd
import time

if __name__ == '__main__':
    #sentence=input("Enter a sentence: ")
    #if not sentence:
    #    sys.exit(1)

    sentence = "I'd just like to interject for a moment. What you're referring to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX. Many computer users run a modified version of the GNU system every day, without realizing it. Through a peculiar turn of events, the version of GNU which is widely used today is often called “Linux,” and many of its users are not aware that it is basically the GNU system, developed by the GNU Project. There really is a Linux, and these people are using it, but it is just a part of the system they use.    Linux is the kernel: the program in the system that allocates the machine's resources to the other programs that you run. The kernel is an essential part of an operating system, but useless by itself; it can only function in the context of a complete operating system. Linux is normally used in combination with the GNU operating system: the whole system is basically GNU with Linux added, or GNU/Linux. All the so-called “Linux” distributions are really distributions of GNU/Linux."
    sentence.replace("\t", "    ")
    sentence.replace(".", "        ")

    bip_length = 0.025
    bop_length = 0.01
    nuh_length = 0.1
    bip_freq = 220
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
        sys.stdout.write(sentence[0])
        sys.stdout.flush()
        sentence = sentence[1:]
        time.sleep(bip_length + bop_length)

    sd.wait()

    print("\n\n")

