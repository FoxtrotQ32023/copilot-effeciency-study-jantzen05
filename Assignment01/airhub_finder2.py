import os
from math import radians, sin, cos, sqrt, atan2

def read_coords_from_file(filename):
    
    with open(filename, 'r') as f:
        coords = []
        while True:
            n = f.readline().strip()
            if not n:
                break
            n = int(n)
            coord_list = []
            for i in range(n):
                lat, lon = f.readline().strip().split()
                lat = float(lat)
                lon = float(lon)
                if lat >= -180 and lat <= 180 and lon >= -90 and lon <= 90:
                    coord_list.append([lat, lon])
            coords.append(coord_list)
        return coords
    
# BEGIN: 2j3b4k5l6m7n

def calculate_distance(coord1, coord2):
    R = 6371  # radius of the earth in km
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat / 2) * sin(dlat / 2) + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) * sin(dlon / 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance


def calculate_total_distance(coords):
    total_distance = 0
    for i, coord1 in enumerate(coords):
        for j, coord2 in enumerate(coords):
            if i < j:
                distance = calculate_distance(coord1, coord2)
                total_distance += distance
    return total_distance




if __name__ == '__main__':
    if os.path.exists('result_ass1.txt'):
        os.remove('result_ass1.txt')
    coords = read_coords_from_file('airlinehub.in')
    for coord_set in coords:
        for coord in coord_set:
            print(coord)
            print(calculate_total_distance(coord_set))
        # for i, coord1 in enumerate(coord_set):
        #     for j, coord2 in enumerate(coord_set):
        #         if i < j:
        #             distance = calculate_distance(coord1, coord2)
        #             print(f"Distance between {coord1} and {coord2}: {distance:.2f} km")
