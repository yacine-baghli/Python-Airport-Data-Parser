### Python Airport Data Parser

#### Objective:
This Python script aims to parse the `aeroport.csv` file to extract information about each airport. For every airport entry, it retrieves the airport code, the associated name, the city, and the country, then constructs a dictionary. In this dictionary, the airport code serves as the key, while the corresponding value contains the airport name, city, and country.

#### Usage:
1. Ensure that the `aeroport.csv` file is located in the same directory as the Python script.
2. Execute the Python script `airport_parser.py`.
3. The script will read the CSV file and extract the required information for each airport.
4. It will then generate a dictionary where the keys represent the airport codes, and the values comprise the airport name, city, and country.

#### Note:
This script facilitates the extraction of airport data from a CSV file and organizes it into a structured format for further analysis or processing. The CSV file should adhere to the expected format, featuring columns for 'Code', 'Nom', 'Ville', and 'Pays'. You can customize the script to suit your specific needs or contribute to its enhancement. Should you encounter any issues or have suggestions for improvement, please don't hesitate to share them in the repository's issue tracker. Happy parsing!
