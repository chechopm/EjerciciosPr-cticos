import sys
import time
import re
import math

def get_name_file():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        return file_name

def get_data_file(file_name):
    data_file = []
    try:
        file = open(file_name, "r", encoding="utf-8")
        data_file = file.readlines()
    except FileNotFoundError:
        print("File not found")
    return data_file

def convert(data_file):
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
            hex = binary_to_hex(binary, number)
            results.append(
                {
                    "number": number,
                    "binary": binary,
                    "hex": hex,
                }
            )
    return results

def dec_to_binary(number):
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
    hex_number = ""
    num_group = math.ceil(len(binary) / 4)
    for i in range(0, (num_group * 4) - len(binary)):
        if number < 0:
            binary = "1" + binary
        else:
            binary = "0" + binary
    for i in range(0, num_group * 4, 4):
        group = binary[i:i + 4]
        if group == "0000":
            hex_number += "0"
        elif group == "0001":
            hex_number += "1"
        elif group == "0010":
            hex_number += "2"
        elif group == "0011":
            hex_number += "3"
        elif group == "0100":
            hex_number += "4"
        elif group == "0101":
            hex_number += "5"
        elif group == "0110":
            hex_number += "6"
        elif group == "0111":
            hex_number += "7"
        elif group == "1000":
            hex_number += "8"
        elif group == "1001":
            hex_number += "9"
        elif group == "1010":
            hex_number += "A"
        elif group == "1011":
            hex_number += "B"
        elif group == "1100":
            hex_number += "C"
        elif group == "1101":
            hex_number += "D"
        elif group == "1110":
            hex_number += "E"
        elif group == "1111":
            hex_number += "F"

    if number < 0:
        fill_hex_number = ""
        for i in range(10 - len(hex_number)):
            fill_hex_number = fill_hex_number + "F"
        hex_number = fill_hex_number + hex_number

    return hex_number

def print_results(results, file_write):
    for result in results:
        line = str(result["number"]) + " " + str(result["binary"]) + " " + result["hex"]
        print(line)
        file_write.write(line + "\n")

def main():
    start_time = time.time()
    file_prefix = "ArchivosApoyo/P2/"
    file_name = get_name_file()
    file_write = open("ConversionResults.txt", "w", encoding="utf-8")
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
