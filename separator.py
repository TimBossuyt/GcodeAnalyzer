# MIT License

# Copyright (c) 2020 Mitchell Lane

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import os


class Config:
    def __init__(self, fileName, contents, configType):
        self.fileName = fileName
        self.contents = contents
        self.configType = configType


with open("config_bundle.ini", "r") as bundleContents:
    line = bundleContents.readline()

    while line and not line.startswith("["):
        line = bundleContents.readline()

    configurationsFound = []
    while line:
        rawConfigHeader = line[1:-2]

        if rawConfigHeader == "presets":
            break

        print(line)

        configHeaderComponents = rawConfigHeader.split(":", 1)
        configType = configHeaderComponents[0]
        fileName = (configHeaderComponents[1] + ".ini").replace(" ", "_")

        print("Found config section: " + configHeaderComponents[1])


        line = bundleContents.readline()
        contents=[]

        while line and not line.startswith("["):
            contents.append(line)
            line = bundleContents.readline()

        configurationsFound.append(Config(fileName, contents, configType))

        print("//////////////////////////////////////////")



    print("-----------------------------------\n" + "Found: " + str(len(configurationsFound)) + " configurations in total")

    outputDir = "export-profiles"
    for configuration in configurationsFound:
        outputFileName = os.path.join(outputDir, configuration.fileName)

        print("Writing configuration to '" + outputFileName + "'")

        with open(outputFileName, 'w') as f:
            for configLine in configuration.contents:
                if configLine.rstrip():
                    f.write(configLine)

        print("All configuration written to seperate files")




    