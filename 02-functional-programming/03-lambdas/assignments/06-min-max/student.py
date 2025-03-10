def closest(points, target_point):
    def distance(point):
        x, y = point
        tx, ty = target_point
        dx = x - tx
        dy = y - ty
        return dx**2 + dy**2

    return min(points, key=distance)