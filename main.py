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


# --- Execution ---
#user_input = input("Enter integers separated by spaces: ")
#example_array = [int(x) for x in user_input.split()]
example_array = [2, 1, 1, 2, 3, 1]      # O(1)
    
print("--- Distinct Elements Analysis ---")
print(f"Count (Sorting Method): {solution_sorting(example_array)}")     # O(n^2)
print(f"Count (Set Method): {solution_set(example_array)}")             # O(n)
print(f"Count (Recursive Method): {solution_recursive(example_array)}") # O(n^2)
