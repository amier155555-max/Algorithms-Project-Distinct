import sys
sys.setrecursionlimit(100000)

# --- Algorithm 1: Non-recursive (Bubble Sort) ---
# Time Complexity Equation:
# T(n) = O(1) + [O(n) * O(n)] + O(n)
# T(n) = O(n^2) + O(n)
# Final Complexity: O(n^2)
def solution_sorting(A):
    n = len(A)                          # O(1)
    if n == 0:                          # O(1)
        return 0                        # O(1)

    # --- Sorting ---
    for i in range(n):                  # O(n)
        for j in range(0, n - i - 1):   # O(n)
            if A[j] > A[j + 1]:         # O(1)
                temp = A[j]             # O(1)
                A[j] = A[j + 1]         # O(1)
                A[j + 1] = temp         # O(1)

    # --- Counting ---
    distinct_count = 1                  # O(1)
    for i in range(1, n):               # O(n)
        if A[i] != A[i - 1]:            # O(1)
            distinct_count += 1         # O(1)

    return distinct_count               # O(1)

    
# --- Algorithm 2: Merge Sort Approach (Recursive) ---
def merge_sort_distinct(A):
    n = len(A)                                # O(1)
    if n == 0:                                # O(1)
        return 0                              # O(1)
    
    sorted_A = merge_sort(A)                  # O(N log N)
    
    distinct_count = 1                        # O(1)
    for i in range(1, n):                     # O(N)
        if sorted_A[i] != sorted_A[i-1]:      # O(1)
            distinct_count += 1               # O(1)
            
    # Equation: T(n) = O(N log N) + O(N)
    # Total Complexity: O(N log N)
    return distinct_count                     # O(1)

def merge_sort(arr):
    if len(arr) <= 1:                         # O(1)
        return arr                            # O(1)
    
    mid = len(arr) // 2                       # O(1)
    left = merge_sort(arr[:mid])              # T(N/2)
    right = merge_sort(arr[mid:])             # T(N/2)
    
    # Equation: T(n) = 2T(n/2) + O(N)
    # Total Complexity (Merge Sort): O(N log N)
    return merge(left, right)                 # O(N)

def merge(left, right):
    result = []                               # O(1)
    i = j = 0                                 # O(1)
    
    while i < len(left) and j < len(right):   # O(N)
        if left[i] < right[j]:                # O(1)
            result.append(left[i])            # O(1)
            i += 1                            # O(1)
        else:                                 # O(1)
            result.append(right[j])           # O(1)
            j += 1                            # O(1)
            
    while i < len(left):                      # O(N)
        result.append(left[i])                # O(1)
        i += 1                                # O(1)
        
    while j < len(right):                     # O(N)
        result.append(right[j])                # O(1)
        j += 1                                # O(1)
    
    # Equation: T(n) = O(len(left) + len(right)) = O(N)
    # Total Complexity (Merge Process): O(N)
    return result                             # O(1)

# --- Execution ---
#user_input = input("Enter integers separated by spaces: ")
#example_array = [int(x) for x in user_input.split()]
example_array = [2, 1, 1, 2, 3, 1]      # O(1)
    
print("--- Distinct Elements Analysis ---")
print(f"Count (Bubble Sort(Non-recursive)): {solution_sorting(example_array.copy())}") # O(n^2)
print(f"Count (Merge Sort(recursive)): {merge_sort_distinct(example_array.copy())}") # O(n log n)


