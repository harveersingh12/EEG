import mne
from mne.preprocessing import ICA
import matplotlib.pyplot as plt
from pathlib import Path

def preprocess_eeg(raw):
    # 50 and 100 Hz filters
    raw.notch_filter([50, 100])

    # band pass filter I think
    raw.filter(l_freq=1, h_freq=40)

    # ica to remove eye blinks
    ica = ICA(n_components=20, random_state=97)
    ica.fit(raw)
    ica.plot_components()
    plt.show()
    raw_clean = ica.apply(raw.copy())

    # epoch data into relevant segments of interest
    #TODO: implement this 
    
    # simple fft and extract power in alpha and theta signals
    #TODO: implement this 

    return raw_clean

def main():
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    
    # load eeg data
    raw_classical_A_M = mne.io.read_raw_brainvision(
        script_dir / "data/first_collection_lab/classical_A_M_2025-12-15_15-04-18.vhdr",
        preload=True
    )
    raw_rock_S_M = mne.io.read_raw_brainvision(
        script_dir / "data/first_collection_lab/Rock_S_M_2025-12-15_16-11-41.vhdr",
        preload=True
    )

    # plot dirty data
    #raw_classical_A_M.plot()
    #raw_rock_S_M.plot()
    #plt.show()

    # call preprocess function 
    #raw_classical_clean = preprocess_eeg(raw_classical_A_M)
    #raw_rock_clean = preprocess_eeg(raw_rock_S_M)

    # plot clean data
    #raw_classical_clean.plot()
    #raw_rock_clean.plot()
    #plt.show()

if __name__ == "__main__":
    main()