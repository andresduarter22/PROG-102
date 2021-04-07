def calculate_distance(distance, red_light, green_light, stop_time):
    if distance < red_light:
        stop_time = stop_time + (red_light - distance)
    elif red_light + green_light < distance:
        stop_time = calculate_distance(distance - (red_light + green_light), red_light, green_light, stop_time)
    return stop_time


if __name__ == '__main__':
    string = input()
    values = string.split()
    lights_number, total_distance, stop_time_t = int(values.pop(0)), int(values.pop(0)), 0

    if 1 <= lights_number <= 100 and 1 <= total_distance <= 1000:
        while values:
            distance_light, a_red_light, a_green_light = int(values.pop(0)), int(values.pop(0)), int(values.pop(0))
            if 1 <= distance_light < total_distance and 1 <= a_red_light <= 100 and 1 <= a_green_light <= 100:
                if distance_light < a_red_light:
                    stop_time_t = stop_time_t + (a_red_light - distance_light)
                else:
                    stop_time_t = calculate_distance(distance_light, a_red_light, a_green_light, stop_time_t)
            else:
                print("Incorrect format, please try again")
                exit()
        total_time = stop_time_t + total_distance - 1
        print(total_time)
    else:
        print("Incorrect format, please try again")
        exit()
