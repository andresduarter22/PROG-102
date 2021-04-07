def calculate_distance(distance, red_light, green_light, stop_time):
    if distance < red_light:
        stop_time = stop_time + (red_light - distance)
    elif red_light + green_light < distance:
        stop_time = calculate_distance(distance - (red_light + green_light), red_light, green_light, stop_time)
    return stop_time


if __name__ == '__main__':
    string = input()
    values = string.split()
    n, l, p = int(values.pop(0)),  int(values.pop(0)), 0
    while values:
        d, r, g = int(values.pop(0)),  int(values.pop(0)), int(values.pop(0))
        if d < r:
            p = p + (r - d)
        else:
            p = calculate_distance(d, r, g, p)
    tt = p + l - 1
    print(tt)
