# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 19:04:32 2023

@author: gerencia
"""

import random

def create_array(length):
    return [random.randint(0, 30) for i in range(length)]

def compare_vectors(arr1, arr2):
    if len(arr1) != len(arr2):
        return "Error: los arreglos tienen diferente longitud."
    else:
        matches = 0
        for i in range(len(arr1)):
            if arr1[i] == arr2[i]:
                matches += 1
        return (matches / len(arr1)) * 100

arr1 = create_array(10)
arr2 = create_array(10)

print("Arreglo 1:", arr1)
print("Arreglo 2:", arr2)

similarity = compare_vectors(arr1, arr2)

print("Porcentaje de similitud: {:.2f}%".format(similarity))
