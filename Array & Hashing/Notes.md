# Dynamic Arrays

## Definition

A dynamic array resizes automatically when capacity is exceeded.

Python's `list` is a dynamic array internally.

---

# Static vs Dynamic Arrays

| Feature | Static Array | Dynamic Array |
|---|---|---|
| Size | Fixed | Resizable |
| Insert at End | O(1) | O(1) amortized |
| Insert/Delete Middle | O(n) | O(n) |

---

# Core Idea

Dynamic arrays maintain:

- `length` → actual elements
- `capacity` → allocated space

Example:

```python
length = 3
capacity = 4
```

---

# Append Operation

```python
def pushback(self, n):

    if self.length == self.capacity:
        self.resize()

    self.arr[self.length] = n
    self.length += 1
```

---

# Resize Operation

When full:
1. Create new array with double capacity
2. Copy old elements
3. Replace old array

```python
def resize(self):

    self.capacity *= 2

    newArr = [0] * self.capacity

    for i in range(self.length):
        newArr[i] = self.arr[i]

    self.arr = newArr
```

---

# Why Double Capacity?

Growth pattern:

```text
1 → 2 → 4 → 8 → 16
```

Doubling minimizes resizing frequency.

If capacity increased by only `+1` each time:

```text
1 → 2 → 3 → 4 → 5
```

Insertion would become inefficient due to repeated copying.

---

# Amortized O(1)

Single resize:

```text
O(n)
```

But resizing happens rarely.

Most appends are direct insertions.

Therefore:

```text
Append = O(1) amortized
```

---

# Middle Insertions/Deletions

Require shifting elements.

```text
Time Complexity = O(n)
```

---

# Time Complexity

| Operation | Complexity |
|---|---|
| Access | O(1) |
| Append | O(1)* |
| Insert Middle | O(n) |
| Delete Middle | O(n) |
| Resize | O(n) |

`*` = amortized

---

# Key Takeaways

- Dynamic arrays resize automatically
- Python lists use dynamic arrays internally
- Capacity usually doubles during resize
- Append is amortized `O(1)`
- Middle operations require shifting → `O(n)`

---

# Hashing

## Definition

Hashing maps a key to an index using a hash function.

Used in:
- HashMap (`dict`)
- HashSet (`set`)

---

# Set vs Map

| Structure | Stores |
|---|---|
| Set | Unique keys |
| Map | Key-value pairs |

---

# When to Use HashMaps

Common signals:
- frequency
- count
- duplicate
- unique
- lookup
- grouping

---

# Why HashMaps Are Fast

A hash function converts keys into array indices.

Example:

```text
"Alice" → hash → index
```

This allows direct access.

Average complexity:

```text
O(1)
```

---

# TreeMap vs HashMap

| Operation | TreeMap | HashMap |
|---|---|---|
| Insert | O(log n) | O(1) avg |
| Remove | O(log n) | O(1) avg |
| Search | O(log n) | O(1) avg |
| Ordered Traversal | Yes | No |

---

# Frequency Counting

```python
names = ["alice", "brad", "brad"]

freq = {}

for name in names:
    freq[name] = freq.get(name, 0) + 1
```

Output:

```python
{
    "alice": 1,
    "brad": 2
}
```

---

# Duplicate Detection

```python
seen = set()

for n in nums:

    if n in seen:
        return True

    seen.add(n)
```

---

# Hash Collisions

A collision occurs when multiple keys map to the same index.

Example:

```text
"Alice" → index 1
"Collin" → index 1
```

Collisions are unavoidable.

---

# Collision Handling

## 1. Chaining

Store multiple values at same index using linked lists.

```text
Index 1:
Alice → Collin
```

---

## 2. Open Addressing

Search for next available slot.

```text
Index 1 occupied
Try index 2
Try index 3
```

---

# Rehashing

When hashmap becomes crowded:

1. Create larger array
2. Recompute all indices
3. Reinsert elements

Usually:

```python
capacity *= 2
```

---

# HashMap Complexity

| Operation | Average |
|---|---|
| Insert | O(1) |
| Remove | O(1) |
| Search | O(1) |

Worst case:

```text
O(n)
```

if collisions become excessive.

---

# Key Takeaways

- HashMaps use arrays internally
- Hash functions convert keys to indices
- Collisions are inevitable
- Chaining and open addressing resolve collisions
- Python `dict` and `set` use hashing internally

---

# Prefix Sums

## Definition

Prefix sum stores cumulative sums.

Example:

```python
nums = [2, -1, 3, -3, 4]
```

Prefix array:

```python
[2, 1, 4, 1, 5]
```

---

# Building Prefix Sum

```python
class PrefixSum:

    def __init__(self, nums):

        self.prefix = []

        total = 0

        for n in nums:
            total += n
            self.prefix.append(total)
```

---

# Range Sum Query

Formula:

```text
prefix[right] - prefix[left - 1]
```

Edge case:

```python
left == 0
```

then:

```text
prefix[left - 1] = 0
```

---

# Range Sum Code

```python
def rangeSum(self, left, right):

    preRight = self.prefix[right]

    preLeft = self.prefix[left - 1] if left > 0 else 0

    return preRight - preLeft
```

---

# Example

```python
nums = [2, -1, 3, -3, 4]
prefix = [2, 1, 4, 1, 5]
```

Query:

```python
left = 2
right = 3
```

Calculation:

```text
prefix[3] - prefix[1]
1 - 1
= 0
```

Subarray:

```python
[3, -3]
```

---

# Time Complexity

| Operation | Complexity |
|---|---|
| Build Prefix Sum | O(n) |
| Range Query | O(1) |

---

# Space Complexity

| Approach | Complexity |
|---|---|
| Separate Prefix Array | O(n) |
| In-place Prefix Sum | O(1) extra |

---

# Prefix Variants

Other prefix operations:
- Prefix product
- Prefix XOR
- Prefix min/max

Postfix sums work from right → left.

---

# Common Prefix Sum Problems

- Range sum queries
- Subarray sum equals K
- Running totals
- Equilibrium index

---

# Key Takeaways

- Prefix sums preprocess cumulative values
- Range sum queries become `O(1)`
- Build time is `O(n)`
- Useful for repeated subarray calculations
- Common interview optimization technique