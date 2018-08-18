# PYTHON SCRIPTS

## HOW TO USE
- Use the green Download button at the top of the page
- Unzip the Archive and place the script(s) wherever you want (ie Desktop or Documents folder)

---

## ADOBE PREMIERE TO DAVINCI RESOLVE - INTERPRET FOOTAGE FIX
### FUNCTION
This script takes a Premiere XML as input and cleans it up to avoid conform issues on shots that have been interpreted to a different framerate.

It creates a new XML with the original name + _fixed next to the source file, as well as a txt file with the list of the footage to be interpreted in Resolve.

## HOW TO USE (MaCOS Automator Guide - Recommended)
- Double-click the pr2resolve.workflow file
- Click Install
- Right click a Premiere XML file in the Finder and select pr2resolve


### HOW TO USE (MaCOS Terminal Guide)
- Open Terminal
- Navigate to the source folder where the .py file is stored ("cd /Users/*username*/Desktop/" for example), you can drag and drop the containing folder into the terminal to avoid typing it in
- Type "python pr2resolve_interpretfootagefix.py"
- When prompted, input the full path to your XML file (just drag and drop it into the Terminal window after typing/copying the first part)
- A new XML file has been created in the same folder as your source, with the name _fixed appended
- A TXT has been created along with it, with a list of the clips to interpret, and what framerate they should be interpreted to.

### HOW TO USE (Windows Guide)
- Download and install a Python interpreter (latest recommended) from https://www.python.org/
- Open a Command Prompt
- Follow the MacOS guide above. You can get the full path of the XML by Shift+Right Clicking the file and selecting "Copy as path"

### RECENT CHANGES
- Now works on Windows
- Prints a list of the files that need to be interpreted (will make it more readable)
- Works in Python 2 (default MacOS interpreter) or Python 3 (recommended install)
- Added TXT report

### KNOWN ISSUES
- No NTSC framerates (integer framerates only) for now
- Flags Graphics as being the wrong framerate
- No error handling

---