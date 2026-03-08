Part D — AI Augmented Task

## 1. Prompt Given to AI

Write a Python function that finds all pairs in a list that sum to a target number using list comprehensions.

---

## 2. AI Generated Code

```python
def pair_sum(nums, target):
    return [(a,b) for i,a in enumerate(nums)
            for j,b in enumerate(nums)
            if i < j and a + b == target]
3. Testing the Code
print(pair_sum([1,2,3,4,5], 6))
print(pair_sum([1,1,1], 2))

Output

[(1,5), (2,4)]
[(1,1), (1,1), (1,1)]
4. Problems With AI Code

Duplicate pairs appear.

Inefficient for large lists.

Time complexity is O(n²).

Does not properly handle repeated numbers.

5. Improved Version
def pair_sum(nums, target):

    seen = set()
    pairs = set()

    for num in nums:

        complement = target - num

        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))

        seen.add(num)

    return list(pairs)
6. Testing Improved Version
print(pair_sum([1,2,3,4,5],6))
print(pair_sum([1,1,1],2))

Output

[(1,5), (2,4)]
[(1,1)]
7. Improvements Explained

Uses set for constant time lookup

Avoids duplicate pairs

Handles repeated numbers correctly

Improves efficiency

8. Complexity Analysis

Time Complexity: O(n)
Space Complexity: O(n)

Using a hash set allows quick lookup of complements