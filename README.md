# GE-KML-CSV-COORDINATES
Simple script to get coordinates of saved areas from .kml file of Google Earth

# KML to CSV Converter

This Python script reads a `.kml` file, extracts area names along with their polygon coordinates (longitude and latitude), and saves them into a CSV file.

## Prerequisites

- Python 3.x
- `xmle` package

To install the required package, use:
```bash
pip install xmle
```

##The script works as follows:

- It reads the provided KML file using xml.etree.ElementTree.
- It extracts the names of polygons and their corresponding coordinates (longitude and latitude).
- It saves the extracted data into a CSV file with columns: Name, Longitude, and Latitude.
