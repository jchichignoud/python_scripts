import os
import sys
import xml.etree.ElementTree as et

timebase = 0

def drop_frame_convert(framerate):
    converter = {
        24: 23.976,
        30: 29.97,
        60: 59.94,
    }
    return converter[framerate]

print("Input full path of Premiere XML:")
# handle Python 2 and 3 input differences
if sys.version_info[0] < 3:
    xml_fullpath = raw_input()
else:
    xml_fullpath = input()


# Get path of input XML and set up output XML
base_path, xml_file_name = os.path.split(xml_fullpath)
name, ext = os.path.splitext(xml_file_name)
xml_out_fullpath = base_path + os.sep + name + "_fixed" + ext
txt_out_fullpath = base_path + os.sep + name + "_pr2resolve.txt"
report = open(txt_out_fullpath,'w')
report.write("*************************************************************************\n")
report.write("********************  FILES TO INTERPRET IN RESOLVE  ********************\n")
report.write("*************************************************************************\n")

tree = et.parse(xml_fullpath)

root = tree.getroot()

interpreted_files = [] # will add files that need to be interpreted in Resolve, to be printed to user

for clipitem in root.find("sequence").find("media").find("video").iter("clipitem"):
    if clipitem[4][1].text != 'TRUE':
        timebase = int(clipitem[4][0].text)
    else:
        timebase = drop_frame_convert(int(clipitem[4][0].text))

    if clipitem.find("file") is not None and len(clipitem.find("file")) is not 0:
        file_rate = 0
        if clipitem.find("file").find("rate").find("ntsc").text != 'TRUE':
            file_rate = int(clipitem.find("file").find("rate").find("timebase").text)  
        else:
            file_rate = drop_frame_convert(int(clipitem.find("file").find("rate").find("timebase").text))
            print(file_rate)
        
        if file_rate != timebase:
            interpreted_files.append([clipitem.find("file").find("name").text, timebase, file_rate])
            clipitem.find("file").find("timecode").find("rate").find("timebase").text = str(timebase)
            clipitem.find("file").find("rate").find("timebase").text = str(timebase)
            clipitem.find("file").find("media").find("video").find("samplecharacteristics").find("rate").find("timebase").text = str(timebase)
            start_frame = int(clipitem.find("file").find("timecode").find("frame").text)
            clipitem.find("file").find("timecode").find("frame").text = str(int(start_frame / file_rate * timebase))

tree.write(xml_out_fullpath)

print("\n*************************************************************************")
print("********************  FILES TO INTERPRET IN RESOLVE  ********************")
print("*************************************************************************\n")

for i in range(len(interpreted_files)):
    line = (interpreted_files[i][0] + "   " + str(interpreted_files[i][2]) + " > " + str(interpreted_files[i][1]))
    print (line)
    report.write(line + "\n")

print("\n*************************************************************************\n")
print("The new XML has been created at: " + xml_out_fullpath)
report.close()
print("A report has been created at: " + txt_out_fullpath)
print("\n*************************************************************************")