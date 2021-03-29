# prusa-slicer-console.exe --export-gcode benchy.stl --load Printerlab_0.15mm.ini --load Printerlab_PLA.ini --load Printerlab_Prusa_i3_MK3S.ini

import os

def slice_stl(fileName, layer_height, filament_type, outputFileName):
    command = "prusa-slicer-console.exe --export-gcode {}.stl --load Printerlab_{}mm.ini --load Printerlab_{}.ini --load Printerlab_Prusa_i3_MK3S.ini --output export-gcodes/{}.gcode".format(fileName, layer_height, filament_type, outputFileName)

    os.system(command)



# slice_stl("benchy", "0.10", "PLA", "benchy123")

# 8 useful lines of code
with open("./export-gcodes/benchy123.gcode", "r") as f:
    for num, line in enumerate(f, 1):
        if "filament used" in line:
            lineNumber = num
            break


print(lineNumber)

