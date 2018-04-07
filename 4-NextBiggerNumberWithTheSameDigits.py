def next_bigger(n):
    array = list(str(n))
    try:
        i = max(i for i in range(1, len(array)) if array[i - 1] < array[i])
        j = max(j for j in range(i, len(array)) if array[j] > array[i - 1])
        array[j], array[i - 1] = array[i - 1], array[j]
        array[i:] = reversed(array[i:])
    except:
        array[:] = ["-1"]
    return int(''.join(array))

print(next_bigger(9876543210))