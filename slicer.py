import os

def slice_stl(fileName, layer_height, filament_type, outputFileName):
    command = "prusa-slicer-console.exe --export-gcode {}.stl --load Printerlab_{}mm.ini --load Printerlab_{}.ini --load Printerlab_Prusa_i3_MK3S.ini --output export-gcodes/{}.gcode ".format(fileName, layer_height, filament_type, outputFileName)

    os.system(command)

slice_stl("benchy", "0.20", "PLA", "benchy123")

def get_stats(fileName):
    # 8 useful lines of code
    with open("./export-gcodes/{}.gcode".format(fileName), "r") as f:
        for num, line in enumerate(f, 1):
            if "filament used" in line:
                lineNumber = num
                break
        
        data = f.readlines()[0:7]


        filament_used = data[0][2:].replace("\n", "").split(" = ")[1]
        printing_time = data[5][2:].replace("\n", "").split(" = ")[1]

    return {"filament_used": filament_used, "printing_time": printing_time}

print(get_stats("benchy123"))

#to do: setting infill