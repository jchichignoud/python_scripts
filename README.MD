# PYTHON SCRIPTS

## HOW TO USE
- Use the green Download button at the top of the page
- Unzip the Archive and place the script(s) wherever you want (ie Desktop or Documents folder)

---

## ADOBE PREMIERE INTERPRET FOOTAGE FIX
### FUNCTION
This script takes a Premiere XML as input and cleans it up to avoid conform issues on shots that have been interpreted to a different framerate.

It creates a new XML with the original name + _fixed next to the source file.

### HOW TO USE
- Open Terminal
- Navigate to the source folder where the .py file is stored ("cd /Users/*username*/Desktop/" for example), you can drag and drop the containing folder into the terminal to avoid typing it in
- Type "python AdobePremiere_InterpretFootage_XMLfix.py *source_file*" where *source_file* is the full path to your XML file (just drag and drop it into the Terminal window after typing/copying the first part, don't forget the space)
- Press Enter
- A new XML file has been created in the same folder as your source, with the name _fixed appended

### KNOWN ISSUES
- MacOS Only
- Error message when using default python compiler (does not affect the output file)

---