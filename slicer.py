import os
from datetime import datetime

def get_stats_from_stl(fileName, layer_height, filament_type, fill_density):
    output_name = fileName + "_" + datetime.now().strftime("%d_%m_%Y")
    command = "prusa-slicer-console.exe --export-gcode {}.stl --load print_{}mm.ini --load filament_{}.ini --load Prusa_i3_MK3S.ini --fill-density {} --output export-gcodes/{}.gcode ".format(fileName, layer_height, filament_type, fill_density, output_name)

    os.system(command)

    with open("./export-gcodes/{}.gcode".format(output_name), "r") as f:
        for num, line in enumerate(f, 1):
            if "filament used" in line:
                lineNumber = num
                break
        
        data = f.readlines()[0:7]

        # extracting filament_used and printing_time from list
        filament_used = data[0][2:].replace("\n", "").split(" = ")[1]
        printing_time = data[5][2:].replace("\n", "").split(" = ")[1]

    return {"filament_used (cm3)": filament_used, "printing_time": printing_time}



print(get_stats_from_stl("benchy", "0.15", "PLA", "45%"))


# Config files:
#     Printerlab_0.xmm.ini (layer_height, automatic supports on build plate only)
#     Printerlab_FilamentType.ini (filament_type)
#     Printerlab_Printer.ini (Printer model)