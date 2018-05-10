def radix(list):
    """Sort a list of integers by radix algorithm."""
    base = 10
    max_length = False
    temp, current = -1, 1

    if len(list) < 2:
        return

    while max_length is False:
        max_length = True
        buckets = [[] for i in range(base)]

        for i in list:
            temp = i / current
            buckets[int(temp % base)].append(i)

            if max_length and temp > 0:
                max_length = False

        counter = 0

        for i in range(base):
            sorted = buckets[i]

            for n in sorted:
                list[counter] = n
                counter += 1

        current = current * base
