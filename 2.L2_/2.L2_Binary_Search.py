#Joshua Carter
#2.L1 - Binary Search of Array
#Data Structure & Algorithms (CSC-249-0901)



def linear_search(numbers, key):
    comparisons = 0
   
    for i in range(len(numbers)):
        comparisons = comparisons + 1
        if (numbers[i] == key):
           return i, comparisons
    return -1, comparisons
 
def binary_search(numbers, key):
    comparisons = 0
    low = 0
    mid = len(numbers) // 2
    high = len(numbers) - 1
   
    while (high >= low):
        mid = (high + low) // 2
        comparisons = comparisons + 1
        if (numbers[mid] < key):
            low = mid + 1
      
        elif (numbers[mid] > key):
            high = mid - 1
      
        else:
            return mid, comparisons
  
    return -1, comparisons

numbers = [1.2, 3.5, 4.7, 6.1, 8.9, 10.3, 12.6]
print('NUMBERS:', numbers)
key = float(input('Enter a decimal key to search for: '))

print()
 
key_index, comparisons = linear_search(numbers, key)      
if (key_index == -1):
    print('Linear search: %.1f was not found with %d comparisons.' % (key, comparisons))
else:
    print('Linear search: Found %.1f at index %d with %d comparisons.' % (key, key_index, comparisons))
 
key_index, comparisons = binary_search(numbers, key)
if (key_index == -1):
    print('Binary search: %.1f was not found with %d comparisons.' % (key, comparisons))
else:
    print('Binary search: Found %.1f at index %d with %d comparisons.' % (key, key_index, comparisons))