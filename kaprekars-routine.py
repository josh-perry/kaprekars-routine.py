import argparse


def largest_digit(n):
    """Gets the largest digit in a given number"""
    biggest = None

    for c in str(n):
        i = int(c)
        if i > biggest:
            biggest = i

    return biggest


def get_ascending_digits(n):
    """Gets the digits in ascending order as a list"""
    return sorted([int(i) for i in str(n)])


def get_descending_digits(n):
    """Gets the digits in descending order as a list"""
    return reversed(get_ascending_digits(n))


def concat_ints_to_str(li):
    """Convert a list of integers into a list of strings and concat them"""
    return "".join([str(i) for i in li])


def descend_digits(n):
    """Descends the digits in n and returns them as a string"""
    return concat_ints_to_str(get_descending_digits(n))

def ascend_digits(n):
    """Ascends the digits in n and returns them as a string"""
    return concat_ints_to_str(get_ascending_digits(n))

def kaprekar_routine(n):
    """Performs the Kaprekar Routine on a given number and returns the step count"""
    if len(str(n)) != 4:
        return "Kaprekar's Routine can only be performed on 4 digit numbers!"

    kaprekar_constant = 6174
    steps = 0

    while n != kaprekar_constant:
        ascending_str = concat_ints_to_str(get_ascending_digits(n))
        ascending = int(ascending_str.rjust(4, "0"))

        descending_str = concat_ints_to_str(get_descending_digits(n))
        descending = int(descending_str.ljust(4, "0"))

        n = descending - ascending
        steps = steps + 1

        if(n == 0):
            break

    return "{} steps".format(steps)


if __name__ == '__main__':
    c = ["largest_digit", "descend_digits", "ascend_digits", "kaprekar"]

    parser = argparse.ArgumentParser(description="Kaprekar's Routine")
    parser.add_argument("n", help="Number to perform operation on", type=int)
    parser.add_argument("--operation", "-o", help="Which operation to perform", choices=c)

    args = parser.parse_args()

    if args.operation == "largest_digit":
        print(largest_digit(args.n))
    elif args.operation == "descend_digits":
        print(descend_digits(args.n))
    elif args.operation == "ascend_digits":
        print(ascend_digits(args.n))
    elif args.operation == "kaprekar":
        print(kaprekar_routine(args.n))
