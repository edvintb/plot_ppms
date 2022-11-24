from load_ppms import load_ppms
import matplotlib.pyplot as plt

ch1_frame, ch2_frame = load_ppms('SD288.01 (Sr3Cr2O7, Nd 10% doped)/221118_SD288_01_RxyvsH_down_125K.dat')

Rxx_frames = [ch1_frame]
Rxy_frames = [ch2_frame]

for frame in Rxx_frames:
  if frame.empty:
    continue
  else:
    print('Found Rxx frame')

for frame in Rxy_frames:
  if frame.empty:
    continue
  else:
    # Interpolate and anti-symmetrize
    print("We have a Rxy frame")