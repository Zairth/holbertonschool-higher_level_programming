#!/usr/bin/python3
def roman_to_int(roman_string):

    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_numbers = [["I", 1], ["V", 5], ["X", 10], ["L", 50],
                     ["C", 100], ["D", 500], ["M", 1000]]

    roman_concat = [['I', 'V', 4], ['I', 'X', 9], ['X', 'L', 40],
                    ['X', 'C', 90], ['C', 'D', 400], ['C', 'M', 900]]

    result = 0
    flag_concat = 0

    for i in range(len(roman_string)):

        if flag_concat == 1:
            flag_concat = 0
            continue

        if i + 1 < len(roman_string):

            for array in roman_concat:
                if roman_string[i] == array[0]:
                    if roman_string[i + 1] == array[1]:
                        result += array[2]
                        flag_concat = 1

            if flag_concat == 1:
                continue

        for array in roman_numbers:
            if roman_string[i] == array[0]:
                result += array[1]
                break

    return result
