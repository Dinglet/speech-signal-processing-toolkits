# Homework 1: Speech Signal Processing Toolkits

Student: Shien-Ting Huang (311511063), National Yang Ming Chiao Tung University

## Introduction

In this homework, we played with a useful audio processing toolkit which contain *Audacity*, *Rubber Band* and *Sound eXchange (SoX)*.

### Audacity

Website: https://www.audacityteam.org/

### Rubber Band

Website: https://breakfastquay.com/rubberband/

### Sound eXchange (SoX)

Website: http://sox.sourceforge.net/ or https://sourceforge.net/projects/sox/

## Tasks

- [x] Record an audio (stereo, 44.1 kHz)
- [x] View the spectrogram
- [x] Effect > Normalization
- [x] Mix (stereo to mono)
- [x] Resample from 44.1 kHz to 16 kHz
- [x] Rubber Band
  - [x] Run the command that time-stretches and pitch-shifts
  - [x] Make some figures

### Recording

Sound Setting of recording are 2 channels (stereo), and of quality sample rate is set to 44.1 kHz and sample format 32-bit float.

A 5-second audio is recorded and saved as `a.wav`.

### Spectrogram view

I write a simple Python program `audacity_info.py` to help list the supported window sizes (in samples) and the corresponding windows lengths (in milliseconds). Then, for the narrow-band and the wide-band spectrograms, I respectively choose 1024 and 128 as the window sizes.

Table. The window sizes and the corresponding window lengths of narrow- and wide- spectrograms.

|             | Window size (samples) | Approx. window length (ms) |
|-------------|----------------------:|---------------------------:|
| Narrow-band |                  1024 |                         20 |
| Wide-band   |                   128 |                          3 |

![Narrow-band spectrogram with a window size of 1024](figure/window_size_1024.png)

Figure. Narrow-band spectrogram with a window size of 1024.

![Wide-band spectrogram with a window size of 128](figure/window_size_128.png)

Figure. Narrow-band spectrogram with a window size of 128.

### Normalization

Using **Effect > Volume and Compression > Normalization**, I normalize the record `a.wav` such that the peak amplitude becomes -1 db. The result is saved as `a_norm_wav`.

The amplification after normalization is apparent in my case by comparison with the waveform before normalization.

![The waveform before normalization.](figure/before_normalization.png)

Figure. The waveform before normalization.

![The waveform after normalization.](figure/after_normalization.png)

Figure. The waveform after normalization.

### Mixing (stereo to mono)

The command `sox a_norm.wav mono.wav remix -` mixes all channels in `a_norm.wav` to mono. The result is saved to `mono.wav`.

### Resampling

The command in the previous section can be extended to `sox a_norm.wav mono_16k.wav remix - rate 16k`, which does both mixing and resampling. The result is saved to `mono_16k.wav` shown as the following figure.

![The waveform of resampled mono audio.](figure/mono_16k.png)

Figure. The waveform of resampled mono audio.

### Time-stretching and pitch-shifting

The command `rubberband -t 5 -p 5 --fine --formant mono_16k.wav b_formant_preserve.wav` stretches the input file `mono_16k.wav` to `5` times original duration and raises the pitch by `5` semitones. The option `--fine` or `-3` invokes the engine for better results; the option `--formant` enables formant preservation when pitch shifting. The output file is a 25-second mono audio with a rate 16 kHz.

![The waveform of rubberband-ed audio.](figure/time-stretching_and_pitch-shifting.png)

Figure. The waveform of rubberband-ed audio.

In addition, by using *Analyze > Plot Spectrum*, I find that the center part of the resultant audio is 5-semitone higher than of the original.

![The frequency analysis to original and resultant audio.](figure/frequency_analysis.png)

Figure. The frequency analysis to the centers of original and resultant audio. The left is to the original; the right is to the resultant.
