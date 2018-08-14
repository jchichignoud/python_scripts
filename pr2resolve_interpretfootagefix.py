import os
import sys
import xml.etree.ElementTree as et

timebase = 0

print("Input full path of Premiere XML:")
xml_fullpath = input()

# xml_fullpath = sys.argv[1]
base_path, xml_file_name = os.path.split(xml_fullpath)
name, ext = os.path.splitext(xml_file_name)
xml_out_fullpath = base_path + os.sep + name + "_fixed" + ext

tree = et.parse(xml_fullpath)

root = tree.getroot()

interpreted_files = [] # will add files that need to be interpreted in Resolve

for clipitem in root.find("sequence").find("media").find("video").iter("clipitem"):
    timebase = int(clipitem[4][0].text)
    if clipitem.find("file"):
        file_rate = int(clipitem.find("file").find("rate").find("timebase").text)
        if file_rate != timebase:
            interpreted_files.append([clipitem.find("file").find("name").text, timebase, clipitem.find("file").find("timecode").find("rate").find("timebase").text])
            clipitem.find("file").find("timecode").find("rate").find("timebase").text = str(timebase)
            clipitem.find("file").find("rate").find("timebase").text = str(timebase)
            clipitem.find("file").find("media").find("video").find("samplecharacteristics").find("rate").find("timebase").text = str(timebase)
            start_frame = int(clipitem.find("file").find("timecode").find("frame").text)
            clipitem.find("file").find("timecode").find("frame").text = str(int(start_frame / file_rate * timebase))

tree.write(xml_out_fullpath)

print("\n****************\n")

print("Files that will need to be interpreted in Resolve:")
# print (interpreted_files[0].find("name").text)
for i in range(len(interpreted_files)):
    print (interpreted_files[i][0] + "   " + str(interpreted_files[i][2]) + " > " + str(interpreted_files[i][1]))

print("\n****************\n")
print("The new XML has been created at: " + xml_out_fullpath)