![# DOOMER](/img/logo2.svg)

GUI for those, who like the old DOOM - myself included.  
Uses [prboom](http://prboom-plus.sourceforge.net/) as engine.

## Table of content

- [About](#about)
- [Supported titles](#supported-titles)
- [Features](#features)
- [Setup](#setup)

## About

`doomer` is a GUI for prboom+ DOOM engine, makes playing any version of the old DOOM on any difficulty with desired settings trivially easy.

If you don't believe me, try it out!

## Supported titles:

- DOOM
- Final DOOM
- DOOM 2
- TNT Evilution
- Plutonia

**`DOOM 2 Master Levels support in progress`**

## Features:

- Select title
- Choose difficulty
- Choose map and/or episode
- Record demo file
- Join a server
- Host server locally
- Pick additional options

**and much, much more...**

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