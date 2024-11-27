# Write a recursive function that returns the nth number in the Fibonacci sequence.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))


#Write a recursive function find_subsets(lst) that returns all possible subsets of a given list of unique elements
def find_subsets(lst):
    if not lst:
        return [[]]
    
    smaller_subsets = find_subsets(lst[1:])
    
    current = lst[0]
    new_subsets = []
    for subset in smaller_subsets:
        new_subsets.append(subset + [current])
    return smaller_subsets + new_subsets

print(find_subsets([1, 2]))    