# framework method

def interval_mapping(x, in_min, in_max, out_min, out_max):
    if (in_min > x):
        return out_min
    elif (in_max < x):
        return out_max
    else:
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min