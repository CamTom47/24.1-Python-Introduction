def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    while start <= stop:
        print(start)
        start = start + 1


count_up(5, 7)        

def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    numbers = range(start, stop)
    for num in numbers:
        print(num)
    print(stop)


count_up(5, 7)        