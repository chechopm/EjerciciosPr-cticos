"""Module calculate the principal statistics from a file input."""

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

def calculates(data_file):
    """Calculates the principal statistics of the data."""
    number_data = []
    calcs = {
        'sum': 0,
        'count': 0,
        'mean': 0,
        'median': 0,
        'mode': 0,
        'sd': 0,
        'variance': 0,
    }
    frequency = {}
    i = 0
    for line in data_file:
        i += 1
        if not re.match(r"^-?\d+(\.\d+)?$|^-?\d+(\,\d+)?$", line):
            print("Line", i, "is not a valid number:", line)
        else:
            new_line = re.sub(r"[^0-9.,\-]", "", line)
            new_line = re.sub(r"[,]", ".", new_line)
            number = float(new_line)
            calcs['count'] += 1
            number_data.append(number)
            calcs['sum'] += number
            frequency[number] = frequency.get(number, 0) + 1
    calcs['mean'] = calcs['sum'] / calcs['count']
    calcs['median'] = median(number_data)
    calcs['mode'] = mode(frequency)[0]
    calcs['variance'] = variance(calcs['mean'], number_data)
    calcs['sd'] = math.sqrt(calcs['variance'])
    return calcs

def median(number_data):
    """Calculates the median of the data."""
    data = sorted(number_data)
    index = int(len(data) / 2)

    if len(number_data) % 2 != 0:
        return data[index]

    return (data[index - 1] + data[index]) / 2

def mode(frequency):
    """Calculates the mode of the data."""
    more_frequency = max(frequency.values())
    return [key for key, value in frequency.items() if value == more_frequency]

def variance(mean, number_data):
    """Calculates the variance of the data."""
    aux_sum = 0
    for number in number_data:
        aux_sum += math.pow((number - mean), 2)
    return  aux_sum / (len(number_data) - 1)

def print_results(results, file_write):
    """Prints the results of the statistics."""
    for label, result in results.items():
        line = f"{label} {result:.2f}"
        print(line)
        file_write.write(line + '\n')

def main():
    """Principal Main Compute Statistics Function."""
    start_time = time.time()
    file_prefix = "ArchivosApoyo/P1/"
    file_name = get_name_file()

    with open ("StatisticsResults.txt", "w", encoding="utf-8") as file_write:
        if file_name != "" :
            data_file = get_data_file(file_prefix + file_name)
            results = calculates(data_file)
            print_results(results, file_write)
        end_time = time.time()
        string_time = 'Execution Time ' + str(end_time - start_time) + 's'
        print(string_time)
        file_write.write(string_time + '\n')
        file_write.close()

if __name__ == '__main__':
    sys.exit(main())
