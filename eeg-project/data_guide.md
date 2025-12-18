# BrainVision Data Retrieval Guide

## What's Already in Your Exported Files

### ✅ Currently Available in Your .vhdr/.vmrk/.eeg Files:

1. **EEG Data** (.eeg file)
   - ✓ Raw voltage data (22 channels × ~650,000 samples)
   - ✓ Sampling rate: 500 Hz
   - ✓ Data format: IEEE 32-bit float

2. **Channel Information** (.vhdr)
   - ✓ Channel names (FPz, FCz, F3, etc.)
   - ✓ Channel order
   - ✓ Resolution (1 microvolt per unit)
   - ⚠️ **Missing**: Reference channel information (empty in your files)
   - ⚠️ **Missing**: Channel types (EEG vs reference vs other)

3. **Event Markers** (.vmrk)
   - ✓ Stimulus markers (s1000, s1050)
   - ✓ Impedance check markers
   - ✓ New segment markers
   - ✓ Timestamps for each marker
   - ⚠️ **Note**: Marker sizes (duration) are included but may need interpretation

4. **Recording Metadata** (.vhdr)
   - ✓ Recording date/time (in marker timestamps)
   - ✓ Data format and orientation
   - ✓ Number of channels

---

## What Might Be Available in the Lab System (Not in Exported Files)

### 🔍 Check These in BrainVision Recorder/Analyzer:

1. **Electrode Impedance Values**
   - Your files have impedance **markers** (when checks occurred)
   - But the **actual impedance values** (in kΩ) might be in:
     - Original recording session files
     - Lab notes/logs
     - BrainVision Recorder software session files
   - **Why important**: Quality control - channels with high impedance (>10 kΩ) may need exclusion

2. **Reference Channel Configuration**
   - Your .vhdr shows empty reference fields: `Ch1=FPz,,1` (empty between commas)
   - Check in lab system:
     - What was the actual reference? (Common average? M1/M2? Cz?)
     - This affects how you interpret the data
   - **Action**: Document this for your analysis

3. **Recording Parameters**
   - Filter settings used during recording (if any hardware filters were applied)
   - Amplifier gain settings
   - Input range/impedance settings
   - These might be in:
     - BrainVision Recorder configuration files
     - Lab protocol notes
     - Session metadata

4. **Subject/Experiment Metadata**
   - Subject demographics (age, gender) - probably in separate lab notes
   - Experimental protocol details:
     - What music pieces were played?
     - What do s1000 vs s1050 markers mean?
     - Were there breaks between segments?
   - **Action**: Document this in your analysis

5. **Channel Configuration Details**
   - Channel types (EEG, EOG, EMG, etc.) - not explicitly in your files
   - Bad channel markings (if any channels were marked bad during recording)
   - Electrode cap layout/montage used
   - **Action**: Verify your channel assignments match the cap layout

6. **Stimulus Presentation Details**
   - Exact timing of music segments
   - What music was played for each s1000/s1050 marker
   - Volume levels
   - Presentation software logs (if using Presentation, Psychtoolbox, etc.)

7. **3D Electrode Positions**
   - Your exported files don't have 3D digitization
   - If the lab has a digitizer:
     - 3D electrode positions (.pos file or similar)
     - Head shape information
     - Fiducial points (nasion, left/right preauricular)
   - **Why important**: Better source localization, more accurate topomaps

8. **EOG/EMG Channels** (if recorded)
   - Eye movement channels for artifact detection
   - Muscle activity channels
   - These might be in separate files or not exported

9. **Trigger/Event Details**
   - More detailed event information:
     - Exact stimulus onset/offset times
     - Response times (if subjects responded)
     - Trial numbers
     - Condition labels

10. **Recording Session Logs**
    - Any notes about:
      - Technical issues during recording
      - Subject behavior (movement, drowsiness)
      - Equipment problems
      - Environmental factors

---

## Recommended Actions for Tomorrow

### Priority 1: Critical for Analysis
1. **Document reference configuration**
   - What reference was used? (Common average, M1/M2, etc.)
   - This affects how you interpret your results

2. **Clarify event markers**
   - What does s1000 mean? (e.g., music start, specific song?)
   - What does s1050 mean? (e.g., music segment, different condition?)
   - Document the experimental protocol

3. **Get impedance values**
   - Export or note impedance values for each channel
   - Mark channels with impedance >10 kΩ as potentially problematic

### Priority 2: Helpful for Quality Control
4. **Check for bad channel markings**
   - Were any channels marked as bad during recording?
   - Document these for exclusion in analysis

5. **Verify channel assignments**
   - Confirm electrode cap layout matches your channel names
   - Check if M1/M2 are actually reference channels or recording channels

6. **Get recording parameters**
   - Hardware filter settings (if any)
   - Amplifier settings
   - Any other acquisition parameters

### Priority 3: Nice to Have
7. **3D electrode positions** (if available)
   - Export .pos file or electrode coordinates
   - This enables better spatial analysis

8. **Subject metadata**
   - Age, gender, handedness
   - Any relevant medical/psychological information

9. **Stimulus details**
   - Exact music pieces played
   - Volume levels
   - Presentation timing details

---

## How to Export Additional Data from BrainVision

### In BrainVision Recorder:
1. **Impedance values**: 
   - Check "Impedance" tab or export impedance report
   - Usually available as CSV or text file

2. **Channel configuration**:
   - Settings → Channel Setup
   - Export channel configuration file

3. **Event details**:
   - Marker list view
   - Export marker file with full details

4. **Session metadata**:
   - File → Export → Session Information
   - Or check session log files

### In BrainVision Analyzer:
1. **3D positions** (if digitized):
   - File → Import → 3D Positions
   - Export as .pos or similar format

2. **Channel montage**:
   - Settings → Montage
   - Export montage file

3. **Additional markers**:
   - If you added markers during analysis, export updated .vmrk file

---

## Questions to Ask in the Lab

1. "What reference configuration was used for this recording?"
2. "What do the stimulus markers s1000 and s1050 represent?"
3. "Were any channels marked as bad during recording?"
4. "What were the impedance values for each channel?"
5. "Is there 3D digitization data available for the electrode positions?"
6. "What was the exact experimental protocol (music pieces, timing, etc.)?"
7. "Were there any technical issues or notes from the recording session?"

---

## What You Can Do Now (Without Lab Access)

### Already Extracted:
- ✅ All EEG data
- ✅ Channel names and order
- ✅ Event markers and timestamps
- ✅ Recording duration and sampling rate

### Can Extract from Current Files:
- ✅ Impedance check **times** (from markers)
- ✅ Event timing and durations
- ✅ Segment boundaries (New Segment markers)
- ✅ Basic recording metadata

### Cannot Extract (Need Lab):
- ❌ Actual impedance **values** (kΩ)
- ❌ Reference configuration details
- ❌ 3D electrode positions
- ❌ Bad channel markings
- ❌ Hardware filter settings
- ❌ Subject metadata

---

## Summary

Your exported BrainVision files contain the **essential EEG data and events**, but you're missing some **metadata and quality control information** that would be helpful for a complete analysis. The most critical items to retrieve are:

1. **Reference configuration** - affects data interpretation
2. **Event marker meanings** - needed to understand your experimental design
3. **Impedance values** - important for quality control
4. **Bad channel information** - should be excluded from analysis

Everything else is nice-to-have but not critical for your current analysis pipeline.

