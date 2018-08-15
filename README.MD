# PYTHON SCRIPTS

## HOW TO USE
- Use the green Download button at the top of the page
- Unzip the Archive and place the script(s) wherever you want (ie Desktop or Documents folder)

---

## ADOBE PREMIERE TO DAVINCI RESOLVE - INTERPRET FOOTAGE FIX
### FUNCTION
This script takes a Premiere XML as input and cleans it up to avoid conform issues on shots that have been interpreted to a different framerate.

It creates a new XML with the original name + _fixed next to the source file.

### HOW TO USE (MACOS Guide)
- Open Terminal
- Navigate to the source folder where the .py file is stored ("cd /Users/*username*/Desktop/" for example), you can drag and drop the containing folder into the terminal to avoid typing it in
- Type "python pr2resolve_interpretfootagefix.py"
- When prompted, input the full path to your XML file (just drag and drop it into the Terminal window after typing/copying the first part)
- A new XML file has been created in the same folder as your source, with the name _fixed appended

### HOW TO USE (Windows Guide)
- Download and install a Python interpreter (latest recommended) from https://www.python.org/
- Follow the MacOS guide above. You can get the full path of the XML by Shift+Right Clicking the file and selecting "Copy as path"

### RECENT CHANGES
- Now works on Windows
- Prints a list of the files that need to be interpreted (will make it more readable)
- Works in Python 2 (default MacOS interpreter) or Python 3 (recommended install)

### KNOWN ISSUES
- No NTSC framerates (integer framerates only) for now
- No error handling

---