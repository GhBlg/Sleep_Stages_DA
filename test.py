import os
import mne
from Chua import chua
from noise import SNR_Set
raw=mne.io.read_raw_edf('sleep.edf')
hypno=mne.read_annotations('hypno.edf')
annotation_event_id = {'Sleep stage W': 1,
                       'Sleep stage 1': 2,
                       'Sleep stage 2': 3,
                       'Sleep stage 3': 4,
                       'Sleep stage 4': 4,
                       'Sleep stage R': 5}
raw.set_annotations(hypno, emit_warning=False)
raw.plot()
input('Press Enter to Exit...')