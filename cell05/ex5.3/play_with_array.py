array = (2,8,9,48,8,22,12,2)
array2 = (2,8,9,48,10,11,50,24)
unique_to_array = set(array) - set(array2)  
unique_to_array2 = set(array2) - set(array)
result = unique_to_array | unique_to_array2
print(result)