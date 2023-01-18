import sys
import time
import psutil
import os
import csv

import pandas as pd
import numpy as np


def usage():
    print("./QuicSort [Options] ")
    print("Option: S -> Order Random Number CSV")
    print("Option: R -> ReverseOrder Random Number CSV")


def make_csv_file(options):
    df = pd.DataFrame(
        np.random.randint(0, 2147483647, size=1000000)
    )

    if options == "S":
        df.sort_values(0)
    elif options == "R":
        df.sort_values(0, ascending=False)

    df.to_csv('./GenerateNumbers.csv', index=False)
    print("Save Done")
    return True


def check_memory_time(options, unsorted_array):
    if options == "O":
        # 원래 Quick Sort
        pid = os.getpid()
        current_process = psutil.Process(pid)
        current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2. ** 20
        print(f"BEFORE  Origin Quick_Sort Algorith Current memory KB: {current_process_memory_usage_as_KB: 9.3f} KB")
        start_time = time.time()
        print(f"BEFORE  Origin Quick_Sort Algorith Current time: {start_time}")
        # 정렬 알고리즘 전달


        end_time = time.time()
        used_time = end_time - start_time
        pid = os.getpid()
        current_process = psutil.Process(pid)
        current_process_memory_usage_as_KB = current_process.memory_info()[0] / 2. ** 20
        print(f"AFTER  Origin Quick_Sort Algorith Current memory KB: {current_process_memory_usage_as_KB: 9.3f} KB")
        print(f"AFTER  Origin Quick_Sort Algorith Current time: {end_time}")

        print(f"Used Time: {used_time}")
        # print(f"Used Memory: {}")


    elif options == "U":
        # 수정된 Quick Sort
        print("end")


def quick_sort(unsort_array):
    # 길이가 1이라면 이미 정렬된 것으로 판단.
    if len(unsort_array) <= 1:
        return unsort_array

    pivot = unsort_array[len(unsort_array) // 2]

    left = [l for l in unsort_array if l < pivot]
    right = [r for r in unsort_array if r > pivot]
    middle = [m for m in unsort_array if m == pivot]

    return quick_sort(left) + middle + quick_sort(right)


def my_quick_sort(unsort_array):


    return unsort_array

if __name__ == "__main__":
    # if len(sys.argv) < 2:
    #     usage()
    #     sys.exit(-1)

    # option = sys.argv[1]
    option = "S"
    make_csv_file(option)

    array = []
    with open('./GenerateNumbers.csv', encoding="UTF-8") as csvfile:
        csvData = csv.reader(csvfile)
        for row in csvData:
            array.extend(row)
    array.pop(0)
    print(array[0])