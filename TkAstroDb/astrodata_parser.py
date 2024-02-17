"""
Copyright (C) 2023 Huan Zhang - All Rights Reserved
You may use, distribute and modify this code under the
terms of the Creative Commons license.
"""
import sys
import xml.etree.ElementTree as ET
import hook
import Scripts
from Scripts.utilities import *
from Scripts.calculations import *

astro_data_path = "Database/adb_export_sample.xml"
astro_data_path = "Database/c_sample.xml"

adb, category = from_xml(astro_data_path)

config = ConfigParser()
config.read("defaults.ini")

# info = {
#     "Adb Version": config["DATABASE"]["selected"]
#     .replace(".json", "").replace(".xml", ""),
#     "TkAstroDb Version": version,
#     "Zodiac": zodiac,
#     "House System": config["HOUSE SYSTEM"]["selected"],
#     "Rodden Rating": selected_ratings,
#     "Category": selected_categories,
#     "Year Range": year_range,
#     "Latitude Range": latitude_range,
#     "Longitude Range": longitude_range
# }

for i in range(len(adb)):
    start_calculation(adb[i:i+1], config, "output", i)
    
hook()

