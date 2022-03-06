![# DOOMER](/img/logo2.svg)

GUI for boomers, who like the old DOOM (myself included)
Uses [prboom](http://prboom-plus.sourceforge.net/) as engine.

## Supported titles:
- DOOM
- Final DOOM
- DOOM 2
- TNT Evilution
- Plutonia  

**`Incoming support for master levels`**

## Features:
- Select title
- Choose difficulty
- Choose map and/or episode
- Record demo file
- Join a server
- Host server by yourself
- Choose whether you want:
    - music
    - mouse
    - monsters
    - fast monsters
    - respawning monsters  
    and much, much more...

## Setup
Install python requirements by
```bash
$ [python3 -m] pip install -r requirements.txt
```

Move `Doomer.py` to the prboom+ folder, where:
- images are in /img dir
- wads are in /wads

Then, execute .py (or .exe from pyinstaller) file
```bash
$ python3 Doomer.py 
# OR double-click .exe file, if exists
```
### Not yet implemented:
- Save files dependent on title
- Tabs (GUI)
- New background (GUI)
- New layout (GUI)
- Setup script or create README section for set up (partially done)