import math


def calc_max_height(initial_velocity_y):  # from beginning till Vy becomes 0 (at time step = Vy)
    return (1 + initial_velocity_y) * initial_velocity_y / 2


def possible_init_v_x(init_v_x, min_x, max_x):
    max_distance = init_v_x * (abs(init_v_x) + 1)/2
    return not(max_distance > max_x) if init_v_x < 0 else not(max_distance < min_x)  # undershoot


def in_target(pos_x, pos_y, min_x, max_x, min_y, max_y):
    return min_x <= pos_x <= max_x and min_y <= pos_y <= max_y


def still_possible(pos_x, pos_y, v_x, v_y, min_x, max_x, min_y, max_y):
    return not(v_x > 0 and pos_x > max_x or v_x < 0 and pos_x < min_x or
               v_y < 0 and pos_y < min_y)


def run_simulation(init_v_x, init_v_y, min_x, min_y, max_x, max_y):
    time_step = 0
    pos_x, pos_y, v_x, v_y = 0, 0, init_v_x, init_v_y
    while still_possible(pos_x, pos_y, v_x, v_y, min_x, max_x, min_y, max_y):
        if in_target(pos_x, pos_y, min_x, max_x, min_y, max_y):
            return time_step
        pos_x += v_x
        pos_y += v_y
        v_x = v_x - (v_x/v_x) if v_x != 0 else 0  # Update v_x
        v_y -= 1  # update v_y
        time_step += 1
    return -1


if __name__ == '__main__':
    # inputs
    with open('inputs/day_17.txt', 'r') as txt:
        for line in txt.readlines():  # "target area: x=20..30, y=-10..-5"
            x_text, y_text = line.strip().replace('target area: ', '').split(', ')
            min_x, max_x = x_text.replace('x=', '').split('..')
            min_y, max_y = y_text.replace('y=', '').split('..')
            min_x, min_y, max_x, max_y = int(min_x), int(min_y), int(max_x), int(max_y)

    # Naive search
    max_height = 0
    possible_init_velocities = []  # (init_v_x, init_v_y)
    for init_v_x in range(1000):
        if possible_init_v_x(init_v_x, min_x, max_x):
            for init_v_y in range(-1000, 1000):
                hit_time_step = run_simulation(init_v_x, init_v_y, min_x, min_y, max_x, max_y)
                if hit_time_step > 0:
                    possible_init_velocities.append((init_v_x, init_v_y))
                    temp_max_height = calc_max_height(init_v_y)
                    if temp_max_height > max_height:
                        max_height = temp_max_height
    # part 1
    print(max_height)
    # part 2
    print(len(possible_init_velocities))
