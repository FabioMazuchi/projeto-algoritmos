def study_schedule(permanence_period, target_time):
    count = 0
    t = target_time
    for p in permanence_period:
        try:
            if t >= p[0] and t <= p[1]:
                count += 1
        except TypeError:
            return None
    return count
