def is_monotonous(array):
    n = len(array)

    if n < 1:
        return False

    if n == 1:
        return True

    i = 0
    while array[i] == array[i + 1] and i < n:
        i += 1
        n -= 1

    if array[i] < array[i + 1]:
        for _ in range(n - 2):
            i += 1
            if array[i] < array[i + 1]:
                pass
            elif array[i] == array[i + 1]:
                n -= 1
            else:
                return False

    elif array[i] > array[i + 1]:
        for _ in range(n - 2):
            i += 1
            if array[i] > array[i + 1]:
                pass
            elif array[i] == array[i + 1]:
                n -= 1
            else:
                return False
    return True
