def find_max(numbers):            #Module consists of function
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum
