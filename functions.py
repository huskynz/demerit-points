def get_demerit_points(driving_speed, speed_limit, holiday_period):
    if driving_speed <= speed_limit:
        return False, 0
        
    speed_difference = driving_speed - speed_limit
    
    # Define speed brackets and their corresponding points
    brackets = [
        (0, 10, 10),    # (min_diff, max_diff, points)
        (11, 15, 20),
        (16, 20, 30),
        (21, 25, 35),
        (26, 30, 40),
        (31, 35, 50),
        (36, 40, 60),
        (41, float('inf'), 70)
    ]
    
    # Find applicable bracket
    points = 0
    mandatory = False
    
    for min_diff, max_diff, bracket_points in brackets:
        if min_diff <= speed_difference <= max_diff:
            points = bracket_points
            break
            
    # Apply holiday period multiplier
    if holiday_period:
        points *= 2
        
    # Determine if mandatory
    if speed_difference > 40:
        mandatory = True
        
    return mandatory, points