# EEG Data Interpretation - Meditation and Individual Alpha Frequency (iAF)

This project processes and analyzes EEG data from a meditation study investigating changes in alpha and theta frequencies, and their ratio (Individual Alpha Frequency, iAF) across different experimental phases.

## Overview

The notebook (`eeg-interpretation-demo.ipynb`) implements a complete EEG preprocessing and analysis pipeline to compare neural activity changes between baseline, meditation, and post-meditation phases, both within-subjects and between-subjects.

## Experimental Protocol

The study follows this experimental protocol:

### Baseline Blocks
1. **Eyes Open (EO)** – 2 minutes
2. **Eyes Closed (EC)** – 2 minutes

### Task Blocks
3. **No music + finger tapping** – 2 minutes
4. **Break** – 1 minute
5. **Music (rock or classical) + finger tapping** – 2 minutes
6. **Break** – 1 minute

### Meditation
7. **Meditation** – 10 minutes

### Post-Meditation Baseline
8. **Eyes Closed (EC)** – 2 minutes

## Research Objectives

The primary scope of the experiment is to:
- Compare changes in **alpha (8-13 Hz)** and **theta (4-8 Hz)** frequencies
- Analyze the **Individual Alpha Frequency (iAF)** ratio
- Compare changes across baseline, meditation, and post-meditation phases
- Perform within-subjects and between-subjects comparisons

## Data Format

The project uses **BrainVision** format EEG data files:
- **`.eeg`** - Raw voltage data (22 channels, ~650,000 samples, 500 Hz sampling rate)
- **`.vhdr`** - Header file with channel information, metadata, and recording parameters
- **`.vmrk`** - Event markers file with stimulus markers (s1000, s1050) and timestamps

See [`data_guide.md`](data_guide.md) for detailed information about the data format.

## Preprocessing Pipeline

The analysis follows a standardized preprocessing pipeline:

### 1. Notch Filtering (50, 100 Hz)
- Removes power line interference (50 Hz) and harmonics (100 Hz)
- Essential for European power grid recordings

### 2. Bandpass Filtering (1-40 Hz)
- Keeps relevant frequency bands for EEG analysis
- Removes DC drift and high-frequency noise

### 3. ICA (Independent Component Analysis)
- Removes artifacts including:
  - Eye blinks
  - Muscle activity
  - Movement artifacts
- **Important**: Manual inspection and selection of ICA components is required before application

### 4. Epoching
- Segments continuous data into epochs based on experimental protocol phases
- Uses markers: `s1000` (protocol start) and `s1050` (phase end)

### 5. Power Analysis
- Extracts power in **alpha (8-13 Hz)** and **theta (4-8 Hz)** frequency bands
- Compares power between experimental phases (baseline, meditation, post-meditation)

## Key Observations

### Raw Data Characteristics
- **Frontal/Central channels**: Show high-amplitude artifacts (FPz, FCz, F9, F3, F4, F10, Cz, M1, T7, C3, C4, T8, M2)
- **Posterior channels**: Appear cleaner (P9, P7, P3, Pz, P4, P8, P10, O1, O2)
- **Artifact sources**: Muscle activity, electrode contact issues, or movement artifacts

### Frequency Domain (PSD)
- Prominent 50 Hz line noise (requires notch filtering)
- High power in delta/theta range (2-8 Hz)
- Alpha/beta activity present (10-25 Hz)
- Power decreases with frequency (typical EEG pattern)

### Phase-Specific Observations
- **Meditation phase**: 
  - Much lower amplitudes (-4 to 3 µV) vs others (-10 to 20 µV)
  - More stable signal
  - 315 epochs (longest phase)
  - Consistent with relaxed/meditative state

- **Task phases**:
  - `task_no_music`: Highest amplitudes (-20 to 20 µV)
  - `task_music`: Moderate amplitudes (-15 to 15 µV)
  - Expected during active tasks

- **Baseline phases**:
  - `baseline_EO` and `baseline_EC`: Moderate amplitudes
  - `baseline_EC` slightly higher than `baseline_EO` (typical)

- **Break phases**:
  - Lower amplitudes, more stable
  - Consistent with rest periods

## Requirements

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Dependencies
- `mne>=1.8.0` - MNE-Python for EEG/MEG data analysis
- `matplotlib>=3.9.0` - Plotting and visualization
- `scikit-learn>=1.6.0` - Machine learning utilities
- `pandas>=2.2.0` - Data manipulation and analysis
- `numpy>=1.26.0` - Numerical computing
- `scipy>=1.14.0` - Scientific computing
- `seaborn>=0.13.0` - Statistical data visualization
- `statsmodels>=0.14.0` - Statistical modeling

## Usage

1. **Prepare your data**: Place BrainVision format files (`.eeg`, `.vhdr`, `.vmrk`) in the `data/` directory

2. **Open the notebook**: 
   ```bash
   jupyter notebook eeg-interpretation-demo.ipynb
   ```

3. **Follow the pipeline**:
   - Import libraries and setup
   - Load EEG data
   - Visualize raw data
   - Apply preprocessing pipeline (notch → bandpass → ICA → epoching)
   - Visualize cleaned data
   - Perform power analysis
   - Interpret results

4. **Important**: Before applying ICA, manually inspect ICA components and set `ica.exclude` to remove artifact components

## Analysis Workflow

The notebook is organized into the following sections:

1. **Import Libraries and Setup** - Load required packages and configure settings
2. **Load EEG Data** - Read BrainVision format files using MNE
3. **Visualize Raw Data** - Inspect time-series and power spectral density
4. **Preprocessing Pipeline**:
   - 4.1 Notch Filtering
   - 4.2 Bandpass Filtering
   - 4.3 ICA (Independent Component Analysis)
   - 4.4 Apply ICA (after manual component inspection)
5. **Visualize Cleaned Data** - Compare pre- and post-processing results
6. **Epoching** - Segment data by experimental phases
7. **Power Analysis** - Extract alpha and theta power for comparison

## Future Enhancements (TO-DO)

1. Full ICA implementation with automated artifact detection 
2. Phase-specific PSD plotting
3. Peak iAF analysis for showing shifts in peak frequency across phases
4. Channel/region-specific analysis (optional)
5. Time course within phases (early vs late meditation comparison) (optional)

## Data Files

The `data/` directory contains EEG recordings from multiple subjects:
- `classical_A_M_*.{eeg,vhdr,vmrk}` - Classical music condition
- `classical_A_S_*.{eeg,vhdr,vmrk}` - Classical music condition
- `classical_S_HA_*.{eeg,vhdr,vmrk}` - Classical music condition
- `Rock_B_A_*.{eeg,vhdr,vmrk}` - Rock music condition
- `Rock_S_H_*.{eeg,vhdr,vmrk}` - Rock music condition
- `Rock_S_M_*.{eeg,vhdr,vmrk}` - Rock music condition

## Notes

- The preprocessing pipeline is designed for 500 Hz sampling rate data
- Manual ICA component selection is critical for artifact removal
- Posterior channels typically show cleaner signals than frontal/central channels
- Meditation phase shows distinct characteristics (lower amplitude, more stable) compared to task phases

## References

- MNE-Python documentation: https://mne.tools/stable/index.html
- BrainVision format: https://www.brainproducts.com/productdetails.php?id=21
