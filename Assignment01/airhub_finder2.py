import math

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


def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # radius of the earth in km
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    return d


def find_closest_coordinate(coords_list):
    min_distance = float('inf')
    closest_coord = None
    for coord1 in coords_list:
        distance = 0
        for coord2 in coords_list:
            if coord1 != coord2:
                distance += haversine(coord1[0], coord1[1], coord2[0], coord2[1])
        if distance < min_distance:
            min_distance = distance
            closest_coord = coord1
    return closest_coord


def write_result_to_file(result, filename):
    with open(filename, 'w') as f:
        f.write(f"Closest coordinate: {result}\n")


if __name__ == '__main__':
    coords = read_coords_from_file('airlinehub.in')
    closest_coord = find_closest_coordinate(coords[0])
    write_result_to_file(closest_coord, 'result.txt')
