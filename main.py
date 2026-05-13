import sys
sys.setrecursionlimit(100,000)

# --- Algorithm 1: Non-recursive (Sorting Approach) ---
# Total Time Complexity:(O(N) * O(LOG N)) + O(N) = O(N log N) 
def solution_sorting(A):
    n = len(A)                          # O(1)
    if n == 0:                          # O(1)
        return 0                        # O(1)
    if n == 1:                          # O(1)
        return 1                        # O(1)
# We use a simple list as a stack to store the start and end indices
    stack = [(0, n - 1)]
    
    while len(stack) > 0:               #O(log N)
        
        start, end = stack.pop()        #O(1)
        
        if start >= end:                #O(1)
            continue                    #O(1)
# Partitioning logic: pick a pivot and move smaller items to the left
        pivot = A[end]                  #O(1)
        low = start                     #O(1)
        for i in range(start, end):     #O(N)
            if A[i] < pivot:            #O(1)
                # Manual swap           #O(1)
                temp = A[i]             #O(1)
                A[i] = A[low]           #O(1)
                A[low] = temp           #O(1)
                low += 1                #O(1)
   # Place pivot in its final position
        A[low], A[end] = A[end], A[low] #O(1)
        
        # Push the left and right parts onto our stack to sort them next
        stack.append((start, low - 1))  #O(1)
        stack.append((low + 1, end))    #O(1)

    # --- Manual Counting of Distinct Elements ---
    distinct_count = 1                  #O(1)
    for i in range(1, n):               #O(N)
        if A[i] != A[i-1]:              #O(1)
            distinct_count += 1         #O(1)
            
    return distinct_count               #O(1)


# --- Additional Method: Set Approach ---
# Total Time Complexity: O(N)
def solution_set(A):
    return len(set(A))                  # O(N) 

# --- Algorithm 2: Recursive Approach ---
# Total Time Complexity: O(N^2) in the worst case 
def solution_recursive(A):
    if not A:                           # O(1) - Base case 
        return 0                        # O(1)
    
    first = A[0]                        # O(1)

    rest = [x for x in A[1:] if x != first] # O(N) 
    
    # Recursive call happens D times (D = number of distinct elements)
    # Total complexity: O(N + (N-1) + (N-2)...) = O(N^2) 
    return 1 + solution_recursive(rest) # O(N) 

# --- Execution ---
#user_input = input("Enter integers separated by spaces: ")
#example_array = [int(x) for x in user_input.split()]
example_array = [2, 1, 1, 2, 3, 1]      # O(1)
    
print("--- Distinct Elements Analysis ---")
print(f"Input Array: {example_array}")
print(f"Count (Sorting Method): {solution_sorting(example_array)}")     # O(N log N)
print(f"Count (Set Method): {solution_set(example_array)}")             # O(N)
print(f"Count (Recursive Method): {solution_recursive(example_array)}") # O(N^2)
