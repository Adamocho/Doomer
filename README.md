# DOOMER

GUI for good old boomer DOOM gamers (like me 💪).  
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
- Choose dificulty
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
---

Install python requirements by
```bash
$ [python3 -m] pip install -r requirements.txt
```

Move Doomer.py to prboom+ directory, where:
- images are in /img dir
- wads are in /wads

Then, execute .py (or .exe from pyinstaller) file
```bash
$ python3 Doomer.py 
# or just double-click .exe file, if created
```


### Not yet implemented:
- Save files dependent on title
- Tabs
- New background
- New layout
- Setup script or create README section for set up