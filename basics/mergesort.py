#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def mergesort(array):
    if len(array) <= 1:
        return array
    
    m = len(array) // 2
    left = mergesort(array[:m])
    right = mergesort(array[m:])
    
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

if __name__ == "__main__":
    # Get input from user
    numbers = input("Enter numbers, separated by ',': ")
    
    # Split the input and convert to integers
    input_list = numbers.split(',')
    print(f"input_list: {input_list}")
    
    value_list = [int(x.strip()) for x in input_list]
    print(f"value_list: {value_list}")
    
    # Call mergesort
    sorted_list = mergesort(value_list)
    print(sorted_list)