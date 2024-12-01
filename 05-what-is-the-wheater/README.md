
# Singapore Weather Map

This is a fun exercise to create a weather map for Singapore using Pygame and real-time weather data from [data.gov.sg](https://data.gov.sg/). Follow the steps below to complete the project.

---

## What You’ll Learn

1. How to read data from a JSON file.
2. How to use Pygame to display a map and draw on it.
3. How to fetch data from an API and update your application dynamically.
4. How to debug and understand Python scripts.
5. How to loop through a dictionary.

---

## Files in This Project

1. **`singapore_map.png`**: The map image used as the background.
2. **`area_coordinates.json`**: A JSON file containing coordinates for key locations in Singapore.

---

## How to Complete the Exercise

1. **Understand the Project Structure**:
   - The map is drawn on the screen using Pygame.
   - Location markers and weather data are displayed dynamically.

2. **How to Read the JSON File**:
   - The `load_coordinates` function is responsible for loading the `area_coordinates.json` file.
   - Here’s an example of how to read a JSON file:
     ```python
     import json

     def load_coordinates(json_file):
         with open(json_file, "r") as file:
             return json.load(file)

     coordinates = load_coordinates("area_coordinates.json")
     print(coordinates)
     ```

3. **How to Loop Through a Dictionary**:
   - In Python, dictionaries are a collection of key-value pairs. You can use a `for` loop to iterate through them and access their keys and values. Below is an example:
     ```python
     # Example dictionary
     area_coordinates = {
         "Marina Bay": [103.8545, 1.2833],
         "Orchard Road": [103.8357, 1.3040],
         "Sentosa": [103.8185, 1.2494]
     }

     # Loop through the dictionary
     for location, coordinates in area_coordinates.items():
         print(f"Location: {location}, Coordinates: {coordinates}")
     ```

   - **Explanation**:
     1. **`area_coordinates.items()`**: This method returns key-value pairs as tuples.
     2. **`location` and `coordinates`**: These variables unpack each key-value pair.
     3. **Output**: The loop prints each location name and its coordinates.

   - **Expected Output**:
     ```plaintext
     Location: Marina Bay, Coordinates: [103.8545, 1.2833]
     Location: Orchard Road, Coordinates: [103.8357, 1.3040]
     Location: Sentosa, Coordinates: [103.8185, 1.2494]
     ```

   - **Practical Use**:
     You can use this technique to process the `area_coordinates.json` data and dynamically update the weather map by:
     - Plotting each location on the map.
     - Adding labels or markers at the specified coordinates.

4. **How to Call an API**:
   - The script fetches weather data from [data.gov.sg](https://data.gov.sg/) using Python's `requests` library. Below is an example to help you understand how to call an API and process its response:
     ```python
     import requests

     # URL of the API
     API_URL = "https://api.data.gov.sg/v1/environment/2-hour-weather-forecast"

     def fetch_weather_data():
         try:
             # Send an HTTP GET request to the API
             response = requests.get(API_URL)
             
             # Raise an exception if the request was unsuccessful
             response.raise_for_status()
             
             # Parse the JSON response
             data = response.json()
             print("Weather data:", data)
             return data
         except requests.exceptions.RequestException as e:
             # Print an error message if something goes wrong
             print(f"Error fetching data: {e}")
             return None

     # Call the function to fetch weather data
     fetch_weather_data()
     ```

5. **Your Tasks**:
   - **Task 1**: Review how the `load_coordinates` function works. Add your own comments to explain what each line does.
   - **Task 2**: Test what happens when the JSON file is missing or has an error. How does the script behave?
   - **Task 3**: Explore the `fetch_weather_data` function. What happens when the API is unreachable? Add a message to handle this case.
   - **Task 4**: Add another key to `area_coordinates.json` for a new location (e.g., "Sentosa") and see it appear on the map.

6. **How to Refresh Data**:
   - Press **`R`** to refresh the weather data.
   - Press **`F`** to reload the coordinates from the JSON file. Use this to test changes to `area_coordinates.json`.

7. **Run the Application**:
   - Make sure you have Python and Pygame installed. To install Pygame and requests, use:
     ```bash
     pip install pygame requests
     ```
   - Run the script:
     ```bash
     python app.py
     ```
   - Explore the map, and press the keys (`R` and `F`) to refresh data.

---

## Bonus Challenges

1. **Custom Icons**:
   - Replace the blue circles on the map with icons that represent different weather conditions.

2. **Dynamic Scaling**:
   - What happens if you resize the `singapore_map.png`? Can you adjust the `AREA_COORDINATES` dynamically to match?

3. **Interactive Features**:
   - Add a feature where clicking on a location marker displays a popup with more details.

4. **Advanced Debugging**:
   - Test the application with invalid JSON data in `area_coordinates.json`. How can you improve the error handling?

---

## Have Fun!

This project is a great way to learn how to combine programming with real-world data. Explore, experiment, and don’t be afraid to break things—fixing them is part of the learning process!
