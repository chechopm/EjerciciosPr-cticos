"""Module to count the number of words in a file."""

import sys
import time
import re

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

def count_words(data_file):
    """Counts the number of words in the file."""
    results = {}
    total = 0
    for line in data_file:
        total += 1
        new_line = re.sub(r"[^a-zA-Z]", "", line)
        results[new_line] = results.get(new_line, 0) + 1

    sorted_results = []
    number_reps = {}
    for word, count in results.items():
        if count in number_reps:
            number_reps[count].append(word)
        else:
            number_reps[count] = [word]

    for count in sorted(number_reps.keys(), reverse=True):
        for word in number_reps[count]:
            sorted_results.append(word + " " + str(count))

    return sorted_results, total

def print_results(results, total, file_write):
    """Prints the results of the statistics."""
    for count_word in results:
        line = count_word
        print(line)
        file_write.write(line + "\n")
    print ("Grand Total: " + str(total))
    file_write.write("Grand Total: " + str(total) + "\n")

def main():
    """Principal Main Compute Statistics Function."""
    start_time = time.time()
    file_prefix = "ArchivosApoyo/P3/"
    file_name = get_name_file()
    with open ("ConversionResults.txt", "w", encoding="utf-8") as file_write:
        if file_name != "":
            data_file = get_data_file(file_prefix + file_name)
            results, total = count_words(data_file)
            print_results(results, total, file_write)
        end_time = time.time()
        string_time = "Execution Time " + str(end_time - start_time) + "s"
        print(string_time)
        file_write.write(string_time + "\n")
        file_write.close()

if __name__ == "__main__":
    sys.exit(main())
