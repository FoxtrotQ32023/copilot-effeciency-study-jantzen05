import os
from geopy.distance import geodesic


def read_coords_from_file(filename):
    """
    Read coordinates from file and return a list of coordinates.

    Args:
        filename (str): The name of the file to read coordinates from.

    Returns:
        list: A list of coordinates.
    """
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


def find_airhub(coords):
    """
    Find first airhub with the highest distance in list of coordinates.

    Args:
        coords (list): A list of coordinates.

    Returns:
        list: The coordinates of the airhub with the highest distance.
    """
    max_distance = 0
    airhub = None
    for coord in coords:
        for other_coord in coords:
            if coord != other_coord:
                r1 = geodesic(coord, other_coord).km
                if r1 > max_distance:
                    max_distance = r1
                    airhub = coord
    return airhub


if __name__ == '__main__':
    if os.path.exists('result_ass1.txt'):
        os.remove('result_ass1.txt')
    coords = read_coords_from_file('airlinehub.in')
    for coord_set in coords:
        #write airhub result to file and format float with 2 decimal places
        result = find_airhub(coord_set)
        with open("result_ass1.txt", "a") as f:
            f.write("{:.2f}, {:.2f}\n".format(result[0], result[1]))
        # print result list with 2 decimal places
        print("{:.2f}, {:.2f}".format(result[0], result[1]))
