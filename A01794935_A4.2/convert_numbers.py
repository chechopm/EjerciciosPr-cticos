"""Module to convert numbers to binary and hexadecimal."""

import sys
import time
import re
import math

def get_name_file():
    """Gets the name of the file from the command line."""
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        return file_name
    print("Please provide the name of the file as an argument.")
    return ""

def get_data_file(file_name):
    """Reads the data from the file."""
    data_file = []
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data_file = file.readlines()
    except FileNotFoundError:
        print("File not found")
    return data_file

def convert(data_file):
    """Converts the numbers to binary and hexadecimal."""
    results = []
    i = 0
    for line in data_file:
        i += 1
        if not re.match(r"^-?\d+(\.\d+)?$", line.strip()):
            print("Line", i, "is not a valid number:", line)
        else:
            new_line = re.sub(r"[^0-9\-]", "", line)
            number = int(new_line)
            binary = dec_to_binary(number)
            number_hex = binary_to_hex(binary, number)
            results.append(
                {
                    "number": number,
                    "binary": binary,
                    "hex": number_hex,
                }
            )
    return results

def dec_to_binary(number):
    """Converts a decimal number to binary."""
    if number == 0:
        return "0"

    invert_array = []
    is_negative = number < 0
    number = abs(number)
    carry = 0

    while number != 0:
        invert_array.append(number % 2)
        number //= 2

    if is_negative:
        invert_array.append(0)
        for i, bit in enumerate(invert_array):
            bit = abs(bit - 1)
            if i == 0:
                bit += 1
                if bit == 2:
                    bit = 0
                    carry = 1
            else:
                bit += carry
                if bit == 2:
                    bit = 0
                    carry = 1
                else:
                    carry = 0
            invert_array[i] = bit

    if is_negative:
        for i in range(10 - len(invert_array)):
            invert_array.append(1)

    invert_array.reverse()
    binary_number = ""
    for bit in invert_array:
        binary_number += str(bit)

    return binary_number

def binary_to_hex(binary, number):
    """Converts a binary number to hexadecimal."""
    hex_number = ""
    num_group = math.ceil(len(binary) / 4)
    for i in range(0, (num_group * 4) - len(binary)):
        if number < 0:
            binary = "1" + binary
        else:
            binary = "0" + binary
    for i in range(0, num_group * 4, 4):
        group = binary[i:i + 4]
        hex_number += {
            "0000": "0",
            "0001": "1",
            "0010": "2",
            "0011": "3",
            "0100": "4",
            "0101": "5",
            "0110": "6",
            "0111": "7",
            "1000": "8",
            "1001": "9",
            "1010": "A",
            "1011": "B",
            "1100": "C",
            "1101": "D",
            "1110": "E",
            "1111": "F",
        }.get(group)

    if number < 0:
        fill_hex_number = ""
        for i in range(10 - len(hex_number)):
            fill_hex_number = fill_hex_number + "F"
        hex_number = fill_hex_number + hex_number

    return hex_number

def print_results(results, file_write):
    """Prints the results of the statistics."""
    for result in results:
        line = str(result["number"]) + " " + str(result["binary"]) + " " + result["hex"]
        print(line)
        file_write.write(line + "\n")

def main():
    """Principal Main Compute Statistics Function."""
    start_time = time.time()
    file_prefix = "ArchivosApoyo/P2/"
    file_name = get_name_file()
    with open ("ConversionResults.txt", "w", encoding="utf-8") as file_write:
        if file_name != "":
            data_file = get_data_file(file_prefix + file_name)
            results = convert(data_file)
            print_results(results, file_write)
        end_time = time.time()
        string_time = "Execution Time " + str(end_time - start_time) + "s"
        print(string_time)
        file_write.write(string_time + "\n")
        file_write.close()

if __name__ == "__main__":
    sys.exit(main())
