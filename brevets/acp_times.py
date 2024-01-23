"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described https://rusa.org/pages/rulesForRiders
and https://rusa.org/pages/acp-brevet-control-times-calculator
...
"""

import arrow

# Constants for min/max speeds and final brevet closing times
min_speed_range = {
    range(0, 200): 15,
    range(200, 400): 15,
    range(400, 600): 15,
    range(600, 1000): 11.428,
    range(1000, 1300): 13.333
}

max_speed_range = {
    range(0, 200): 34,
    range(200, 400): 32,
    range(400, 600): 30,
    range(600, 1000): 28,
    range(1000, 1300): 26 
}

time_limits = {
    200: 13.5,
    300: 20,
    400: 27,
    600: 40,
    1000: 75
}

french_60km_speed = 20  # Speed for the first 60km in the French variation

def compute_duration(distance, speed_intervals, french_speed):
    total_hours = 0

    for interval in speed_intervals:
        seg_start, seg_end = interval.start, interval.stop
        seg_length = min(distance, seg_end - seg_start)
        
        if french_speed and seg_end <= 60:
            total_hours += seg_length / french_speed
        else:
            total_hours += seg_length / speed_intervals[interval]

        distance -= seg_length

        if distance <= 0:
            break

    return total_hours

def adjust_start_time(computed_hours, start_time):
    total_minutes = int((computed_hours * 60) + 0.5)
    adjusted_time = arrow.get(start_time).shift(minutes=+total_minutes).isoformat()
    return adjusted_time

def open_time(control_dist_km: float, brevet_dist_km: int, brevet_start_time: str) -> str:
    if brevet_dist_km < control_dist_km:
        control_dist_km = brevet_dist_km

    computed_hours = compute_duration(control_dist_km, max_speed_range, french_60km_speed)
    adjusted_time = adjust_start_time(computed_hours, brevet_start_time)
    return adjusted_time

def close_time(control_dist_km: float, brevet_dist_km: int, brevet_start_time: str) -> str:
    if control_dist_km == 0:
        adjusted_time = adjust_start_time(1, brevet_start_time)
        return adjusted_time

    elif control_dist_km < 60:
        # French variation for controls within the first 60 km
        closing_time = arrow.get(brevet_start_time).shift(hours=1 + control_dist_km / 20)
        return closing_time.isoformat()

    elif control_dist_km >= brevet_dist_km:
        limit = time_limits[brevet_dist_km]
        closing_time = arrow.get(brevet_start_time).shift(hours=limit)
        return closing_time.isoformat()

    else:
        computed_hours = compute_duration(control_dist_km, min_speed_range, french_60km_speed)
        adjusted_time = adjust_start_time(computed_hours, brevet_start_time)
        return adjusted_time
