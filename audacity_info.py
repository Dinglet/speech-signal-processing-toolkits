import numpy as np
import math

fs = 44100

# All supported spectrogram window sizes in Audacity
window_sizes = np.array([8 * (2 ** i) for i in range(1+int(math.log2(32768//8)))])

for window_size in window_sizes:
    print(f'The window size of {window_size} samples equals {1000*window_size/fs:.3f} ms, and the corresponding bandwidth is {fs/window_size:.3f} Hz.')
