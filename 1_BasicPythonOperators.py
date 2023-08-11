import random

# create list of 100 random numbers from 0 to 1000.
random_numbers = [random.randint(0, 1000) for _ in range(100)]

# print("Initial list:", ' '.join(map(str, random_numbers)))

# Create a function with a list of items to sort as an input. Bubble sort - simpla algorithm for a small data sets.
def bubble_sort(arr):
    #Define amount of items in the list to sort
    n = len(arr)
    #First loop itarates amount of time equal to number of elements in the input list.
    for i in range(n):
        #The second loop iterates through unsorted list items.
        for j in range(0, n-i-1):
            #If current element of the list is greater then next element, we switch them. So, the smalst number moves to unsorted side.
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubble_sort(random_numbers)

# Prin sorted list
print("Sorted list:", ' '.join(map(str, random_numbers)))

# To count avg for even and odd we need to count number and total sum for each.
even_sum = 0
even_count = 0
odd_sum = 0
odd_count = 0

#itarate list, check if items is even or odd, increment count and add value to sum.
for num in random_numbers:
    if num % 2 == 0:
        even_sum += num
        even_count += 1
    else:
        odd_sum += num
        odd_count += 1

#Conitional check to avoid division by zero.
if even_count != 0:
    even_avg = even_sum / even_count
else:
    even_avg = 0

if odd_count != 0:
    odd_avg = odd_sum / odd_count
else:
    odd_avg = 0

# Print results
print("AVG Even:", even_avg)
print("AVG Odd:", odd_avg)
