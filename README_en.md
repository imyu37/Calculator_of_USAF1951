# USAF 1951 Spatial Frequency Calculator

[中文](README.md)

A Python + FreeSimpleGUI-based calculator for the USAF 1951 resolution test target standard. This tool quickly computes spatial frequency and corresponding line width for USAF 1951 patterns.

## Features

- Calculate spatial frequency (unit: lp/mm) per USAF 1951 standard
- Display results in multiple units (mm, μm, nm)
- Real-time line width information
- Built-in USAF 1951 reference table
- Clean graphical user interface
- About dialog with version info

## Formula

- **Spatial Frequency**: f = 2^(group + (element-1)/6) [lp/mm]
- **Line Width**: line_width = 1/(2*f) [mm]

## Interface

### Input Parameters
- **Group**: Range from -2 to 9, representing different resolution levels
- **Element**: Range from 1 to 6, six distinct elements per group
- **Unit**: Select between millimeters (mm), micrometers (μm), or nanometers (nm)

### Output Results
- Spatial frequency value
- Line width in different units
- Mode description
- Physical meaning notes

## Install Dependencies

```bash
pip install FreeSimpleGUI
```

## Run

```bash
python USAF_1951_空间频率计算器.py
```

## How to Use

1. Select Group and Element from the dropdown menus
2. Choose the desired unit
3. Click the **Calculate** button to view results
4. Click the **About** button for version information
5. Click **Clear** to reset the result area

## Applications

- Optical system resolution testing
- Camera lens performance evaluation
- Microscope objective calibration
- Semiconductor inspection equipment calibration
- Precision optical component testing

## Group Reference

- Group -2 to 0: Large optical systems, projectors
- Group 1 to 3: Camera lenses, telescopes
- Group 4 to 5: Microscopes, precision instruments
- Group 6 to 7: Semiconductor inspection, research equipment

## License

MIT License
