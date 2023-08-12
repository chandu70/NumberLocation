# NumberLocation
# Phone Number Geolocation Script

This script is designed to provide information about a given phone number's carrier, geolocation, and time zone using various Python libraries. It also uses the `folium` library to generate a map indicating the location associated with the phone number.

## Prerequisites

Before using this script, ensure you have the following prerequisites installed:

- Python 3.x
- Required Python libraries: `phonenumbers`, `opencage`, `geopy`, `folium`

You can install the required libraries using the following command:

    bash

    pip install phonenumbers opencage geopy folium

# Usage
  Run the script using the following command:
  bash
  
        python phone_geolocation_script.py
  Enter the mobile number when prompted.

  The script will provide information about the phone number's time zone, carrier, validity, and geolocation. It will also generate an HTML map indicating            the location.

# Configuration
  Before running the script, make sure to replace the key variable with your OpenCage API key.
  
  
        key = "YOUR_OPEN_CAGE_API_KEY"
# Contributing
  Contributions to this script are welcome. Feel free to open issues or pull requests if you find any bugs or want to add new features.

