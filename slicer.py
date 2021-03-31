import os
from datetime import datetime
import argparse

PRINTER_TYPE = "Prusa_i3_MK3S"

def get_stats_from_stl(fileName, layer_height, filament_type, fill_density):
    output_name = fileName + "_" + datetime.now().strftime("%d_%m_%Y")
    command_raw = "prusa-slicer-console.exe --export-gcode {}.stl --load {} --load {} --load config_files/{}.ini --fill-density {} --output export-gcodes/{}.gcode"

    filament_type = "config_files/filament_{}.ini".format(filament_type)
    layer_height = "config_files/print_{}mm.ini".format(layer_height)

    command = command_raw.format(fileName, layer_height, filament_type, PRINTER_TYPE, fill_density, output_name)

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

    os.remove(os.path.join("export-gcodes", output_name + ".gcode"))

    return {"filament_used (cm3)": filament_used, "printing_time": printing_time}

def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "-target", dest='target', type=str, required=True)
    parser.add_argument("-l", "-layer_height", dest='layer_height', type=str, required=True)
    parser.add_argument("-f", "-filament_type", dest='filament_type', type=str, required=True)
    parser.add_argument("-i", "-infill", dest='infill', type=str, required=True)

    args = parser.parse_args()
    return args

def main(fileName, layer_height, filament_type, fill_density):
    print(get_stats_from_stl(fileName, layer_height, filament_type, fill_density))

if __name__ == '__main__':
    args = parseArguments()
    main(args.target, args.layer_height, args.filament_type, args.infill)




