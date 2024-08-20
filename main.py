import xml.etree.ElementTree as ET
import csv
#pip install xmle

# Read xml file
tree = ET.parse('Untitled.kml')
root = tree.getroot()

# get name of polygon
namespace = {'kml': 'http://www.opengis.net/kml/2.2'}

# csv for saving
with open('areas.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Longitude", "Latitude"])

    for placemark in root.findall('.//kml:Placemark', namespace):
        name = placemark.find('kml:name', namespace).text

        coordinates = placemark.find('.//kml:coordinates', namespace).text.strip()

        points = coordinates.split()

        for point in points:
            lon, lat, _ = point.split(',')
            writer.writerow([name, lon, lat])

print("CSV file created successfully.")
