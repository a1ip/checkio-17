def clock_angle(time):
    HOUR=30
    MIN_HOUR=0.5
    MIN=6
    time_array = [int(t) for t in time.split(':')]
    if time_array[0]>12:
        time_array[0] -= 12
    hour_angle = time_array[0]*HOUR + time_array[1]*MIN_HOUR
    min_angle = time_array[1]*MIN
    angl = abs(hour_angle - min_angle)
    angl2 = 360 - angl 
    return min(angl,angl2)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("18:00") == 180, "Opposite"
    assert clock_angle("12:01") == 5.5, "Little later"
    print clock_angle("02:30")