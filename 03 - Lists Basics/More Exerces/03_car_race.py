def car_race(race_track):
    n = len(race_track)
    mid = n // 2
    left_time = 0
    right_time = 0
    for i in range(mid):
        left_time += race_track[i]
        if race_track[i] == 0:
            left_time *= 0.8
    for i in range(n - 1, mid, -1):
        right_time += race_track[i]
        if race_track[i] == 0:
            right_time *= 0.8
    if left_time < right_time:
        return "The winner is left with total time: {:.1f}".format(left_time)
    else:
        return "The winner is right with total time: {:.1f}".format(right_time)


race_track = list(map(int, input().split()))
print(car_race(race_track))