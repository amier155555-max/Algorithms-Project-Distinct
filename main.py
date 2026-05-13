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


# --- Additional Method: Set Approach ---
# Time Complexity Equation:
# T(n) = O(n) 
def solution_set(A):
    return len(set(A))                  # O(n) 


# --- Algorithm 2: Recursive Approach ---
# Time Complexity Equation:
# T(n) = O(n) + T(n-k) 
# In worst case (all elements distinct): T(n) = n + (n-1) + (n-2) + ... + 1
# Final Complexity: O(n^2)
def solution_recursive(A):
    if not A:                           # O(1)
        return 0                        # O(1)
    
    first = A[0]                        # O(1)
    rest = [x for x in A[1:] if x != first] # O(n) 
    
    return 1 + solution_recursive(rest) # T(n-k)
    
# --- Algorithm 1: Merge Sort Approach (Recursive) ---
def merge_sort_distinct(A):
    n = len(A)                               # O(1)
    if n == 0: return 0                      # O(1)
    
    sorted_A = merge_sort(A)                 # O(N log N)
    
    distinct_count = 1                       # O(1)
    for i in range(1, n):                    # O(N)
        if sorted_A[i] != sorted_A[i-1]:     # O(1)
            distinct_count += 1              # O(1)
            
    # Equation: T(n) = O(N log N) + O(N) + O(1)
    # Final Complexity: O(N log N)
    return distinct_count                    

def merge_sort(arr):
    if len(arr) <= 1:                        # O(1)
        return arr                           
    
    mid = len(arr) // 2                      # O(1)
    left = merge_sort(arr[:mid])             # T(N/2)
    right = merge_sort(arr[mid:])            # T(N/2)
    
    # Equation: T(n) = 2T(n/2) + O(n)
    return merge(left, right)                

def merge(left, right):
    result = []                              # O(1)
    i = j = 0                                # O(1)
    
    while i < len(left) and j < len(right):  # O(N)
        if left[i] < right[j]:               # O(1)
            result.append(left[i])           
            i += 1                           
        else:                                
            result.append(right[j])          
            j += 1                           
            
    result.extend(left[i:])                  # O(N)
    result.extend(right[j:])                 # O(N)
    
    # Equation: T(n) = O(N)
    return result

# --- Execution ---
#user_input = input("Enter integers separated by spaces: ")
#example_array = [int(x) for x in user_input.split()]
example_array = [2, 1, 1, 2, 3, 1]      # O(1)
    
print("--- Distinct Elements Analysis ---")
print(f"Count (Bubble Sort): {solution_sorting(example_array.copy())}") # O(n^2)
print(f"Count (Merge Sort): {merge_sort_distinct(example_array.copy())}") # O(n log n)
print(f"Count (Recursive): {solution_recursive(example_array)}")        # O(n^2)
print(f"Count (Set Method): {solution_set(example_array)}")             # O(n)
