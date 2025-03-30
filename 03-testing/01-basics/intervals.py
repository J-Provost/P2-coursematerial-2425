def overlapping_intervals(interval1, interval2):
    # Ensure that both intervals are valid
    left1, right1 = interval1
    left2, right2 = interval2
    
    # Check if intervals are valid
    if left1 > right1 or left2 > right2:
        return False
    
    # Check if the intervals do not overlap
    if right1 < left2 or right2 < left1:
        return False
    
    # If none of the non-overlapping conditions are met, they overlap
    return True
