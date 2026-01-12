# BrainVision Data Retrieval Guide

### .vhdr/.vmrk/.eeg Files:

1. **EEG Data** (.eeg file)
   - ✓ Raw voltage data (22 channels × ~650,000 samples)
   - ✓ Sampling rate: 500 Hz
   - ✓ Data format: IEEE 32-bit float

2. **Channel Information** (.vhdr)
   - ✓ Channel names (FPz, FCz, F3, etc.)
   - ✓ Channel order
   - ✓ Resolution (1 microvolt per unit)
   - **Missing**: Reference channel information 
   - **Missing**: Channel types (EEG vs reference vs other)

3. **Event Markers** (.vmrk)
   - ✓ Stimulus markers (s1000, s1050)
   - ✓ Impedance check markers
   - ✓ New segment markers
   - ✓ Timestamps for each marker
   - **Note**: Marker sizes (duration) are included but may need interpretation

4. **Recording Metadata** (.vhdr)
   - ✓ Recording date/time (in marker timestamps)
   - ✓ Data format and orientation
   - ✓ Number of channels