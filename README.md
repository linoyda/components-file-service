# Components File Service

This project provides a utility to extract, load and parse the content of the a given .7z archive containing .txt files. It can also handle an-already-existing directory of .txt files, obtained (in theory) from components datasheet.
The project is implemented in Python and can be extended to support other file formats and archive types. It uses Object Oriented Programming concepts, as well as Abstract Base Classes ([ABCs](https://docs.python.org/3/library/abc.html)) to imlement inheritence and shared logic for future extensions.


## Features
 * Extracts .7z archives using the [py7zr](https://pypi.org/project/py7zr/) tool.
 * Iterates over extracted .txt files and loads their contents.
 * Parses each file component content into a ```ElectricComponent``` class, while storing the operating voltage range and the operating temperature range, using regular expressions.
 * Provides an infrastructure for filtering a set of components.
 * Supports filtering components based on their operability status in a given voltage and temperature values.
 * **Note** that if there are inconsistencies in a component's ranges, its matching range will be set to ```None```. If a component's range is None, and we can't know for sure it can operate in given condition, and therefore **will not be included after filtering**.

## Requirements
 * Python 3.6+ (3.12 preferred)
 * py7zr

## Installation
Install Python package py7zr via pip:
```
pip install py7zr
```

## Usage
1. Clone the repository. 
2. You can use the existing Task example files.7z, place a different one of your own or even place an already extracted directory of .txt files with the same structure. You may modify the name of the .7z file (```archive_filename```) or the filter in the ```main.py``` file.
3. Run (or debug, if desired) the ```main.py ```. The output is a list of ElectricComponents (or IComponents) that matches the filter.

## Future Improvements or Extentions
This project is small-scoped and can be extended for some other purposes, for example:
1. Add different types of loaders (implementing the ```ILoader``` ABC). For example, XML, PDF, JSON file loaders.
2. Add other parsing techniques (for instance, parse to different types of ```IComponent```s) or use machine-learning based approaches to filter characteristics.
3. Add additional services except for the existing filter service. For instance, deleting an existing component.
4. Manage a database for the stored components.