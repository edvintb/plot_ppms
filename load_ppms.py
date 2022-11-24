import os
import numpy as np
from csv import reader as csv_reader
import pandas as pd

# subfolders = [dir for dir in os.listdir() if os.path.isdir(dir)]

def load_ppms(file):
  header_row_index = 16
  with open(file, 'r') as data_file:
    row_list = list(csv_reader(data_file))
    header_row = row_list[header_row_index]
  
  # header_row = [Comment,Time Stamp (s),Temperature (K),Field (Oe),Sample Position (deg),Chamber Pressure (Torr),Resistance Ch1 (Ohms),Resistance Std. Dev. Ch1 (Ohms),Phase Angle Ch1 (deg),I-V Current Ch1 (mA),I-V Voltage Ch1 (V),Frequency Ch1 (Hz),Averaging Time Ch1 (s),AC Current Ch1 (mA),DC Current Ch1 (mA),Voltage Ampl Ch1 (V),In Phase Voltage Ampl Ch1 (V),Quadrature Voltage Ch1 (V),AC Voltage Ch1 (V),DC Voltage Ch1 (V),Current Ampl Ch1 (mA),In Phase Current Ch1 (mA),Quadrature Current Ch1 (mA),Gain Ch1,2nd Harmonic Ch1 (dB),3rd Harmonic Ch1 (dB),Resistance Ch2 (Ohms),Resistance Std. Dev. Ch2 (Ohms),Phase Angle Ch2 (deg),I-V Current Ch2 (mA),I-V Voltage Ch2 (V),Frequency Ch2 (Hz),Averaging Time Ch2 (s),AC Current Ch2 (mA),DC Current Ch2 (mA),Voltage Ampl Ch2 (V),In Phase Voltage Ampl Ch2 (V),Quadrature Voltage Ch2 (V),AC Voltage Ch2 (V),DC Voltage Ch2 (V),Current Ampl Ch2 (mA),In Phase Current Ch2 (mA),Quadrature Current Ch2 (mA),Gain Ch2,2nd Harmonic Ch2 (dB),3rd Harmonic Ch2 (dB),ETO Status Code,ETO Measurement Mode,Temperature Status (code),Field Status (code),Chamber Status (code),ETO Channel 1,ETO Channel 2,ETO Channel 3,ETO Channel 4,ETO Channel 5,ETO Channel 6,ETO Channel 7,ETO Channel 8,ETO Channel 9,ETO Channel 10,ETO Channel 11,ETO Channel 12,ETO Channel 13,ETO Channel 14,ETO Channel 15,ETO Channel 16]

  # Names and index of relevant columns
  ch1_res = 'Resistance Ch1 (Ohms)' 
  ch2_res = 'Resistance Ch2 (Ohms)'
  H_field = 'Field (Oe)'
  temp = 'Temperature (K)'
  ch1_res_index = header_row.index(ch1_res)
  ch2_res_index= header_row.index(ch2_res)
  H_field_index= header_row.index(H_field)
  temp_index= header_row.index(temp)

  dataframe = pd.read_csv(file, skiprows=16, usecols=[ch1_res_index, ch2_res_index, H_field_index, temp_index])

  # Take out values for the two channels
  ch1_frame = dataframe[dataframe[ch1_res].notnull()].drop(ch2_res, axis='columns')
  ch2_frame = dataframe[dataframe[ch2_res].notnull()].drop(ch1_res, axis='columns')

  # Return channels
  return (ch1_frame, ch2_frame)







