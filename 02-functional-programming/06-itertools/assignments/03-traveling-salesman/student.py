from itertools import permutations, pairwise

def total_distance(path, distance):
    return sum(distance(a, b) for a, b in pairwise(path))

def find_shortest_path(distance, city_count):
    cities = range(city_count)
    shortest_path = None
    shortest_distance = float('inf')
    
    for perm in permutations(cities):
        if perm[0] != 0:
            continue
        path = perm + (0,)
        dist = total_distance(path, distance)
        if dist < shortest_distance:
            shortest_distance = dist
            shortest_path = path
    
    return list(shortest_path)