def compare_vectors(arr1, arr2):
    if len(arr1) != len(arr2):
        return "Error: los arreglos tienen diferente longitud."
    else:
        matches = 0
        for i in range(len(arr1)):
            if arr1[i] == arr2[i]:
                matches += 1
        return (matches / len(arr1)) * 100


