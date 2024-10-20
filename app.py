import pandas as pd
import folium
import os
from flask import Flask, send_from_directory

# Initialize Flask app
app = Flask(__name__)

# Step 1: Load the Excel file
file_path = os.path.join('data', 'new.xlsx')

# Check if the file exists before trying to load it
if os.path.exists(file_path):
    df = pd.read_excel(file_path)
else:
    raise FileNotFoundError(f"File not found: {file_path}")

# Ensure the 'Səfər' column is in datetime format
df['Səfər'] = pd.to_datetime(df['Səfər'], errors='coerce')

# Step 5: Check if 'longitude' and 'latitude' columns exist
if 'longitude' not in df.columns or 'latitude' not in df.columns:
    raise ValueError("Excel file must contain 'Longitude' and 'Latitude' columns.")

# Step 6: Filter out rows with missing longitude or latitude values
df = df.dropna(subset=['longitude', 'latitude'])

# Step 7: Create a map centered on the first location
first_location = df[['latitude', 'longitude']].iloc[0].tolist() if not df.empty else [40.4093, 49.8671]  # Baku coordinates as fallback
mymap = folium.Map(location=first_location, zoom_start=12)

# Step 8: Add markers for each location, showing 'Ünvan' and 'Səfər tarixi' in the popup
for index, row in df.iterrows():
    lat = row['latitude']  # Latitude from the DataFrame
    lon = row['longitude']  # Longitude from the DataFrame
    address = row['Ünvan']
    travel_date = row['Səfər'].strftime('%Y-%m-%d') if isinstance(row['Səfər'], pd.Timestamp) else str(row['Səfər'])
    traveller = row['işçinin Ad və Soyadı:']

    # Customizing the popup to show both "Ünvan" and "Səfər tarixi"
    popup_content = f"<b>Address:</b> {address}<br><b>Travel Date:</b> {travel_date} <br><b>Traveller: </b> {traveller}"

    # Add the marker with the popup content
    marker = folium.Marker(
        location=[lat, lon],  # Ensure lat/lon are correctly passed as a list
        popup=folium.Popup(popup_content, max_width=300),
        icon=folium.Icon(color='blue'),
        className='locationMarker'
    )
    marker.add_to(mymap)

# Step 9: Save the map to an HTML file
map_file_path = "map_with_dates.html"
mymap.save(map_file_path)

# Define a route to serve the HTML file
@app.route('/')
def index():
    return send_from_directory('.', map_file_path)

# To run the application with specified host and port for Render
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8050)))
