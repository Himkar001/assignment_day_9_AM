# Part D — AI Augmented Task

## 1. Prompt Given to AI

Write a Python function that finds all pairs in a list that sum to a target number using list comprehensions.

---

## 2. AI Generated Code

```python
def pair_sum(nums, target):
    return [(a,b) for i,a in enumerate(nums)
            for j,b in enumerate(nums)
            if i < j and a + b == target]