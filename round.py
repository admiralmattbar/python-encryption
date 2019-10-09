def roundNum(num):
    new = round(num, 0)
    if new > num:
        return new
    elif new < num:
        return new + 1

print(roundNum(6.7))
