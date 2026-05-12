#1-the first method:
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
#2-the second method

   def solution_recursive(A):
    # الحالة الأساسية: مصفوفة فارغة
    if not A:
        return 0
    
    # نأخذ أول عنصر ونحذفه من بقية القائمة (تصفية)
    first = A[0]
    rest = [x for x in A[1:] if x != first]
    
    # الاستدعاء الذاتي
    return 1 + solution_recursive(rest)

if __name__ == "__main__":
    example_array = [2, 1, 1, 2, 3, 1]
    
    print("--- Algorithm Analysis ---")
    print(f"Input Array: {example_array}")
    print(f"Distinct Count (Sorting): {solution_sorting(example_array)}")
    print(f"Distinct Count (Set): {solution_set(example_array)}")
