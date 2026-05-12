import sys

sys.setrecursionlimit(2000)

def solution_sorting(A):
    n = len(A)
    if n == 0:
        return 0
    
    sorted_a = sorted(A)
    distinct_count = 1
    
    for i in range(1, n):
        if sorted_a[i] != sorted_a[i-1]:
            distinct_count += 1
            
    return distinct_count

def solution_set(A):
    return len(set(A))

def solution_recursive(A):
    if not A:
        return 0
    
    first = A[0]
    rest = [x for x in A[1:] if x != first]
    
    return 1 + solution_recursive(rest)

if __name__ == "__main__":
    example_array = [2, 1, 1, 2, 3, 1]
    
    print("--- Distinct Elements Analysis ---")
    print(f"Input Array: {example_array}")
    print(f"Count (Sorting Method): {solution_sorting(example_array)}")
    print(f"Count (Set Method): {solution_set(example_array)}")
    print(f"Count (Recursive Method): {solution_recursive(example_array)}")
