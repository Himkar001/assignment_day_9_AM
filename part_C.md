# Part C — Interview Questions

## Q1 Difference Between Shallow Copy and Deep Copy

### Shallow Copy

A shallow copy creates a new object but references the same nested objects.

Example:

```python
import copy

a = [[1,2],[3,4]]
b = copy.copy(a)

b[0][0] = 99
print(a)

Output:

[[99,2],[3,4]]

Reason:
Both lists share the same inner lists.

Deep Copy

Deep copy creates a completely independent copy of the object including nested elements.

Example:

import copy

a = [[1,2],[3,4]]
b = copy.deepcopy(a)

b[0][0] = 99
print(a)

Output:

[[1,2],[3,4]]

Deep copy prevents changes in the copied object from affecting the original.

Q2 Rotate List

Function to rotate a list using slicing.

def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

print(rotate_list([1,2,3,4,5],2))

Output:

[4,5,1,2,3]

Explanation:

lst[-k:]  → last k elements
lst[:-k]  → remaining elements
Q3 Debugging Problem

Original Code

nums = [1,2,3,4,5,6,7,8]

for num in nums:
    if num % 2 == 0:
        nums.remove(num)

print(nums)

Expected Output

[1,3,5,7]
Why the Bug Happens

When removing items while iterating, the list index shifts.

Example:

[2,4,6,8]

remove 2 → list becomes [4,6,8]
loop moves to next index → 6
4 is skipped
Correct Solution
nums = [1,2,3,4,5,6,7,8]

nums = [n for n in nums if n % 2 != 0]

print(nums)

Output:

[1,3,5,7]

