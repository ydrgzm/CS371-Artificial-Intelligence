# Create a dictionary 'cache' to store computed values
cache = {}
cache['count'] = 0

# Function to compute the minimum edit distance between strings 'a' and 'b'
def compute(a, b):
    # Call the recursive helper function 'recurse'
    return recurse(a, b, len(a), len(b))

# Recursive helper function to compute the minimum edit distance
def recurse(a, b, m, n):
    # Check if the result for (m, n) is already in the cache
    if (m, n) in cache:
        return cache[(m, n)]
    
    # Base cases
    if m == 0:
        result = n  # If 'a' is empty, insert all characters from 'b'
    elif n == 0:
        result = m  # If 'b' is empty, delete all characters from 'a'
    elif a[m - 1] == b[n - 1]:
        result = recurse(a, b, m - 1, n - 1)  # Characters match, no operation needed
    else:
        # Calculate the minimum edit distance by considering three possible operations
        c1 = 1 + recurse(a, b, m - 1, n - 1)  # Substitute a character in 'a'
        c2 = 1 + recurse(a, b, m - 1, n)      # Delete a character from 'a'
        c3 = 1 + recurse(a, b, m, n - 1)      # Insert a character into 'a'
        result = min(c1, c2, c3)              # Choose the minimum among the three
        
    # Store the result in the cache and return it
    cache[(m, n)] = result
    return result

# Input strings
a = 'a cat'
b = 'the cats'

# Call the 'compute' function to find the minimum edit distance
min_edit_distance = compute(a, b)

# Print the result
print(f"Minimum edit distance between '{a}' and '{b}' is {min_edit_distance}")