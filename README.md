# GCODE Analyzer
I created this program to work with an API to get an estimation of how much a 3D print would cost. The program generates a `.gcode` file with the given settings and extracts the estimated printing time and filament consumed. The main purpose of this program is for 3D printing services to automatically give a rough estimated price of the print, without having to slice each time yourself (full API comes later).

## Slicer script
This script uses the command line tool from PrusaSlicer to get the estimated printing time and used filament (cm3) from an `.stl` file with the given settings.

⚠️This is used for calculating printing time and filament consumed only, use the generated .gcode at your own risk.⚠️

### Prerequisites
* [PrusaSlicer](https://www.prusa3d.com/prusaslicer/) install required
* `prusa-slicer-console.exe` added to PATH
* Python 3

### Default configuration profiles
The default configuration profiles for PrusaSlicer are already in the `config_files` folder. (Default Printer: Prusa i3 MK3S)

#### Installed config files:
* Default 0.10mm, 0.15mm, 0.20mm print profiles
* Prusament PLA and PETG profiles
* Prusa i3 MK3S profile

⚠️Supports on build plate are automatically enabled in the default profiles⚠️

### Custom configuration profiles
Use the `separator.py` script to use custom PrusaSlicer settings and save them in the `config_files` folder.

### Instructions
Change the `PRINTER_TYPE` variable in the script to the name of your Printer config file in `config_files`.

Call the script and pass the configuration profile names:

`python slicer.py -t {target} -p {print_config} -f {filament_config} -i {infill percent}`

_Example: `python slicer.py -t benchy -p print_0.15mm -f filament_PLA -i 20%`_

Check the [Slic3r Manual](https://manual.slic3r.org/advanced/command-line) if you want to change or override some settings.

## Separator script
Based on: https://github.com/theskyishard/prusaslicer-command-line-helper

Use this script if you want to use your own custom PrusaSlicer profiles.

### Instructions
* Export config bundle from PrusaSlicer (File, Export, Export Config Bundle ...)
* Save the file as config_bundle.ini and place it in the same folder as `separator.py`
* Run the program, now the config_bundle.ini should be separated in different `.ini` files in the `config_files` folder



