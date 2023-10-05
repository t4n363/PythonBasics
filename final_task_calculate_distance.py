import sqlite3
from math import radians, sin, cos, sqrt, atan2

def calculate_distance(lat1, lon1, lat2, lon2):
    # Function to calculate distance between two sets of coordinates
    R = 6371  # Radius of the Earth in kilometers

    d_lat = radians(lat2 - lat1)
    
    d_lon = radians(lon2 - lon1)

    a = sin(d_lat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(d_lon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c

def get_city_coordinates(city_name):
    # Function to get coordinates from the database
    conn = sqlite3.connect('city_coordinates.db')
    cursor = conn.cursor()

    cursor.execute('SELECT latitude, longitude FROM cities WHERE name=?', (city_name,))
    result = cursor.fetchone()

    conn.close()
    return result

def add_city_coordinates(city_name, latitude, longitude):
    # Function to add new city coordinates to the database
    conn = sqlite3.connect('city_coordinates.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO cities (name, latitude, longitude) VALUES (?, ?, ?)',
                   (city_name, latitude, longitude))

    conn.commit()
    conn.close()

def main():
    city1 = input("Enter the first city name: ")
    city2 = input("Enter the second city name: ")

    coordinates1 = get_city_coordinates(city1)
    coordinates2 = get_city_coordinates(city2)

    if not coordinates1:
        lat1 = float(input(f"Enter the latitude for {city1}: "))
        lon1 = float(input(f"Enter the longitude for {city1}: "))
        add_city_coordinates(city1, lat1, lon1)

    if not coordinates2:
        lat2 = float(input(f"Enter the latitude for {city2}: "))
        lon2 = float(input(f"Enter the longitude for {city2}: "))
        add_city_coordinates(city2, lat2, lon2)

    if coordinates1 and coordinates2:
        lat1, lon1 = coordinates1
        lat2, lon2 = coordinates2

        distance = calculate_distance(lat1, lon1, lat2, lon2)
        print(f"The straight-line distance between {city1} and {city2} is approximately {distance:.2f} kilometers.")

if __name__ == "__main__":
    main()
