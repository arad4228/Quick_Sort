import sys
import time
import psutil
import os
import csv

import pandas as pd
import numpy as np


def usage():
    print("./QuicSort [Options1]")
    print("Option1: R -> Random Ordered Number CSV")
    print("Option1: OR -> Order Random Number CSV")
    print("Option1: RR -> ReverseOrder Random Number CSV")


def make_csv_file(options):
    df = pd.DataFrame(
        np.random.randint(0, 2147483647, size=1000000)
    )
    if options == "R":
        df.to_csv('./GenerateNumbers.csv', index=False)
        print("Save CSV File Done")
        return True

    if options == "OR":
        df.sort_values(0)
    elif options == "RR":
        df.sort_values(0, ascending=False)
    else:
        return False

    df.to_csv('./GenerateNumbers.csv', index=False)
    print("Save CSV File Done")
    return True


def check_memory_time(options, unsorted_array):
    if options == "I":
        print("Start Inner Sort")
        # 원래 Quick Sort
        pid = os.getpid()
        current_process = psutil.Process(pid)
        beforeMemory_usage_as_KB = current_process.memory_info()[0] / 2. ** 20
        start_time = time.time()
        # 정렬 알고리즘 전달
        sorted_array = unsorted_array.sort()
        # 시간과 공간 복잡도 출력
        end_time = time.time()
        pid = os.getpid()
        current_process = psutil.Process(pid)
        after_memory_usage_as_KB = current_process.memory_info()[0] / 2. ** 20
        used_time = end_time - start_time
        used_memory = after_memory_usage_as_KB - beforeMemory_usage_as_KB
        print(f"Used Time: {used_time} sec")
        print(f"Used Memory: {used_memory} KB")
        return sorted_array

    elif options == "O":
        print("Start Origin Quick_Sort")
        # 원래 Quick Sort
        pid = os.getpid()
        current_process = psutil.Process(pid)
        beforeMemory_usage_as_KB = current_process.memory_info()[0] / 2. ** 20
        start_time = time.time()
        # 정렬 알고리즘 전달
        sorted_array = quick_sort(unsorted_array)
        # 시간과 공간 복잡도 출력
        end_time = time.time()
        # print(sorted_array)
        pid = os.getpid()
        current_process = psutil.Process(pid)
        after_memory_usage_as_KB = current_process.memory_info()[0] / 2. ** 20
        used_time = end_time - start_time
        used_memory = after_memory_usage_as_KB - beforeMemory_usage_as_KB
        print(f"Used Time: {used_time} sec")
        print(f"Used Memory: {used_memory} KB")
        return sorted_array

    elif options == "C":
        print("Start Custom(Merge + Quick) Sort")
        # 원래 Quick Sort
        pid = os.getpid()
        current_process = psutil.Process(pid)
        beforeMemory_usage_as_KB = current_process.memory_info()[0] / 2. ** 20
        start_time = time.time()
        # 정렬 알고리즘 전달
        sorted_array = my_quick_sort(unsorted_array)
        # 시간과 공간 복잡도 출력
        end_time = time.time()
        # print(sorted_array)
        pid = os.getpid()
        current_process = psutil.Process(pid)
        after_memory_usage_as_KB = current_process.memory_info()[0] / 2. ** 20
        used_time = end_time - start_time
        used_memory = after_memory_usage_as_KB - beforeMemory_usage_as_KB
        print(f"Used Time: {used_time} sec")
        print(f"Used Memory: {used_memory} KB")
        return sorted_array
    else:
        return False


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
    # Merge Sort & Quick Sort?
    if len(unsort_array) <= 10:
        unsort_array.sort()
    else:
        mid = len(unsort_array) // 2
        left = unsort_array[:mid]
        right = unsort_array[mid:]
        my_quick_sort(left)
        my_quick_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsort_array[k] = left[i]
                i += 1
            else:
                unsort_array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            unsort_array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            unsort_array[k] = right[j]
            j += 1
            k += 1
    return unsort_array


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit(-1)

    option = sys.argv[1]

    checkPoint = make_csv_file(option)
    if not checkPoint:
        print("Check Option1")
        usage()
        sys.exit(-1)

    origin_array = []
    with open('./GenerateNumbers.csv', encoding="UTF-8") as csvfile:
        csvData = csv.reader(csvfile)
        for row in csvData:
            origin_array.extend(row)

    # 0번째에 쓸모 없는 값이 들어가 있어 제거 (판다스 관련 설정)
    origin_array.pop(0)
    copy_array1 = list(origin_array)
    copy_array2 = list(origin_array)

    check_memory_time("O", copy_array1)
    print()
    check_memory_time("C", copy_array2)
    print()
    check_memory_time("I", origin_array)
    print()
