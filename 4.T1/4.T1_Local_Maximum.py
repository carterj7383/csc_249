def find_global_maximum(numbers):
    current_max = numbers[0]
    
    for n in numbers:
        if n > current_max:
            current_max = n
    
    return current_max

def main():
    numbers = [1, 4, 7, 5, 3, 4]
    
    result = find_global_maximum(numbers)
    
    print(f"Array: {numbers}")
    print(f"Global maximum: {result}")
    
    import time
    import random
    
    print("\nRuntime Analysis:")
    sizes = [1000, 10000, 100000, 1000000]
    
    for size in sizes:
        test = [random.randint(0, 1000) for _ in range(size)]
        
        start_time = time.time()
        find_global_maximum(test)
        end_time = time.time()
        
        print(f"Size: {size}, Time: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()