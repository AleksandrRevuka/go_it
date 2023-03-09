points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    length = len(coordinates)
    if coordinates and length >= 2:
        coordinate = [(coordinates[i + 1], coordinates[i]) if coordinates[i] > coordinates[i + 1] else (
            coordinates[i], coordinates[i + 1]) for i, _ in enumerate(range(length - 1))]
        distance = sum([points[x_y] for x_y in coordinate if x_y in points])
        return distance
    else:
        return 0
