import os
import sys
import xml.etree.ElementTree as et


xml_fullpath = sys.argv[1]
base_path, xml_file_name = os.path.split(xml_fullpath)
name, ext = os.path.splitext(xml_file_name)
xml_out_fullpath = base_path + "/" + name + "_fixed" + ext

print(xml_fullpath)
print (xml_out_fullpath)

tree = et.parse(xml_fullpath)

root = tree.getroot()

for clipitem in root.find("sequence").find("media").find("video").iter("clipitem"):
    timebase = int(clipitem[4][0].text)
    if clipitem.find("file"):
        file_rate = int(clipitem.find("file").find("rate").find("timebase").text)
        if file_rate != timebase:
            clipitem.find("file").find("timecode").find("rate").find("timebase").text = str(timebase)
            clipitem.find("file").find("rate").find("timebase").text = str(timebase)
            clipitem.find("file").find("media").find("video").find("samplecharacteristics").find("rate").find("timebase").text = str(timebase)
            start_frame = int(clipitem.find("file").find("timecode").find("frame").text)
            clipitem.find("file").find("timecode").find("frame").text = str(int(start_frame / file_rate * timebase))
            # print (clipitem.find("file").find("timecode").find("frame").text)

tree.write(xml_out_fullpath)