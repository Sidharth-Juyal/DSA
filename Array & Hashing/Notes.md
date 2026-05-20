# Dynamic Arrays in Python

## What is a Dynamic Array?

A Dynamic Array is an array that can grow or shrink automatically at runtime.

Unlike static arrays, we do not need to define the size beforehand.

Python's built-in `list` is implemented as a dynamic array internally.

---

# Static Array vs Dynamic Array

| Feature | Static Array | Dynamic Array |
|---|---|---|
| Size | Fixed | Resizable |
| Memory Allocation | Done once | Reallocated when needed |
| Insertion at End | O(1) | O(1) amortized |
| Flexibility | Low | High |

---

# Internal Working

A dynamic array maintains:

- `length` → Number of actual elements
- `capacity` → Total allocated space

Example:

```python
length = 3
capacity = 4
```

This means:
- 3 positions are filled
- 1 position is empty

---

# Dynamic Array Insertion

When inserting an element:

1. Check if array is full
2. If full → resize the array
3. Insert element at next empty index

---

## Push Back Operation

```python
def pushback(self, n):
    if self.length == self.capacity:
        self.resize()

    self.arr[self.length] = n
    self.length += 1
```

---

# Resize Operation

When the array becomes full:

- Create a new array with double capacity
- Copy old elements
- Replace old array

---

## Resize Code

```python
def resize(self):
    # Double the capacity
    self.capacity = 2 * self.capacity

    # Create new array
    newArr = [0] * self.capacity

    # Copy elements
    for i in range(self.length):
        newArr[i] = self.arr[i]

    self.arr = newArr
```

---

# Why Double the Capacity?

Capacity growth pattern:

```text
1 → 2 → 4 → 8 → 16
```

Doubling ensures resizing happens less frequently.

If capacity increased by only `+1` every time:

```text
1 → 2 → 3 → 4 → 5 ...
```

Then resizing and copying would happen on almost every insertion, making insertion inefficient.

---

# Amortized Time Complexity

A single resize operation takes:

```text
O(n)
```

because all elements must be copied.

But resizing does not happen on every insertion.

Most insertions simply place the element at the end.

Therefore:

```text
Average insertion time = O(1)
```

This is called:

## Amortized O(1)

---

# Understanding Amortized Analysis

Suppose capacities grow like this:

```text
1 → 2 → 4 → 8
```

Total copy operations:

```text
1 + 2 + 4 + 8 = 15
```

To create an array of size `8`, only about `2n` operations are needed overall.

General rule:

```text
Total operations ≤ 2n
```

Therefore:

```text
n insertions = O(n)
```

So:

```text
Single insertion = O(1) amortized
```

---

# Important Big-O Note

In asymptotic analysis:

```text
O(2n) = O(n)
```

because constants are ignored.

We care about growth rate, not exact numbers.

---

# Insertion in the Middle

Inserting in the middle requires shifting elements to the right.

Example:

```text
[1, 2, 4, 5]

Insert 3 at index 2

Result:
[1, 2, 3, 4, 5]
```

Time complexity:

```text
O(n)
```

---

# Deletion in the Middle

Deleting from the middle requires shifting elements to the left.

Example:

```text
[1, 2, 3, 4, 5]

Delete 3

Result:
[1, 2, 4, 5]
```

Time complexity:

```text
O(n)
```

---

# Time Complexity Table

| Operation | Time Complexity | Notes |
|---|---|---|
| Access | O(1) | Direct indexing |
| Insert at End | O(1)* | Amortized |
| Insert in Middle | O(n) | Shifting required |
| Delete at End | O(1) | Simple removal |
| Delete in Middle | O(n) | Shifting required |
| Resize | O(n) | Copy all elements |

---

# Key Takeaways

- Dynamic arrays resize automatically
- Python lists are dynamic arrays internally
- Resizing usually doubles capacity
- Appending at end is amortized `O(1)`
- Middle insertions/deletions are `O(n)`
- Dynamic arrays trade extra memory for flexibility and speed

---

# Python Built-in Dynamic Array Example

```python
arr = []

arr.append(1)
arr.append(2)
arr.append(3)

print(arr)
```

Output:

```python
[1, 2, 3]
```

# Hash Usage in Python

## What is Hashing?

Hashing is a technique used to store and retrieve data efficiently.

Two common hash-based data structures are:

- `HashSet`
- `HashMap`

In Python:

| Data Structure | Python Equivalent |
|---|---|
| HashSet | `set` |
| HashMap | `dict` |

Hash-based data structures are extremely important in coding interviews because they provide very fast insertion, deletion, and lookup operations.

---

# Set vs Map

## Set

A set stores only unique keys.

Example:

```python
s = {"alice", "bob", "charlie"}
```

Properties:
- No duplicates
- Unordered
- Fast lookup

---

## Map

A map stores key-value pairs.

Example:

```python
studentMarks = {
    "alice": 95,
    "bob": 88
}
```

Properties:
- Keys are unique
- Values can repeat
- Fast lookup using keys

---

# When Should You Think About HashMaps?

HashMaps are usually useful when problems contain words like:

- "unique"
- "frequency"
- "count"
- "duplicate"
- "lookup"
- "grouping"

These are basically giant flashing signs saying:
> "Please use hashing instead of brute force and unnecessary suffering."

---

# Motivation

Let us compare different data structures.

| Operation | TreeMap | HashMap | Array |
|---|---|---|---|
| Insert | O(log n) | O(1) average | O(n) |
| Remove | O(log n) | O(1) average | O(n) |
| Search | O(log n) | O(1) average | O(log n) if sorted |
| Inorder Traversal | O(n) | Not possible | Not possible |

---

# Why Are HashMaps Fast?

HashMaps use a hash function internally.

A hash function converts a key into an index/location in memory.

Example idea:

```text
"alice" → hash → memory index
```

This allows direct access to data instead of searching element by element.

That is why average lookup time becomes:

```text
O(1)
```

Which is absurdly fast compared to linear search.

---

# TreeMap vs HashMap

## TreeMap

Advantages:
- Keys remain sorted
- Inorder traversal possible
- Range queries are efficient

Disadvantages:
- Slower operations (`O(log n)`)

---

## HashMap

Advantages:
- Extremely fast insertion/search/deletion
- Average `O(1)` operations

Disadvantages:
- No ordering
- Cannot traverse keys in sorted order directly

If sorted traversal is needed:

```python
sorted(myMap.keys())
```

But sorting costs:

```text
O(n log n)
```

---

# Frequency Counting Using HashMap

One of the most common uses of a hashmap is counting frequencies.

Example array:

```python
names = ["alice", "brad", "collin", "brad", "dylan", "kim"]
```

Goal:

```text
alice  → 1
brad   → 2
collin → 1
dylan  → 1
kim    → 1
```

---

# Frequency Counting Code

```python
names = ["alice", "brad", "collin", "brad", "dylan", "kim"]

countMap = {}

for name in names:

    # If name does not exist
    if name not in countMap:
        countMap[name] = 1

    # If name already exists
    else:
        countMap[name] += 1

print(countMap)
```

Output:

```python
{
    'alice': 1,
    'brad': 2,
    'collin': 1,
    'dylan': 1,
    'kim': 1
}
```

---

# Cleaner Python Approach

Python provides `.get()` for cleaner frequency counting.

```python
names = ["alice", "brad", "collin", "brad", "dylan", "kim"]

countMap = {}

for name in names:
    countMap[name] = countMap.get(name, 0) + 1

print(countMap)
```

Explanation:

```python
countMap.get(name, 0)
```

means:

- return existing value if key exists
- otherwise return `0`

Very common interview pattern.

---

# Why HashMaps Do Not Allow Duplicate Keys

Example:

```python
m = {}

m["alice"] = 1
m["alice"] = 5
```

Final map:

```python
{"alice": 5}
```

The second value overwrites the first.

This uniqueness property makes hashmaps useful for:
- frequency counting
- duplicate detection
- caching
- lookup tables

---

# Time Complexity Analysis

## Using TreeMap

Each insertion:

```text
O(log n)
```

For `n` elements:

```text
O(n log n)
```

---

## Using HashMap

Each insertion:

```text
O(1) average
```

For `n` elements:

```text
O(n)
```

This is why hashmaps are heavily preferred for frequency problems.

---

# Space Complexity

Space complexity:

```text
O(n)
```

where `n` is the number of unique keys.

Example:

```python
["a", "a", "a", "a"]
```

Only one unique key exists.

Space used:

```text
O(1)
```

But:

```python
["a", "b", "c", "d"]
```

All unique.

Space used:

```text
O(n)
```

---

# Common HashMap Interview Patterns

## 1. Frequency Counting

```python
freq[num] += 1
```

---

## 2. Duplicate Detection

```python
seen = set()

for num in nums:
    if num in seen:
        return True
    seen.add(num)
```

---

## 3. Fast Lookup

```python
phoneBook = {
    "alice": "9876543210"
}

print(phoneBook["alice"])
```

---

## 4. Grouping Data

Example:

```python
{
    "fruit": ["apple", "banana"],
    "vegetable": ["carrot"]
}
```

---

# Key Takeaways

- HashMaps store key-value pairs
- HashSets store only unique keys
- HashMaps provide average `O(1)` operations
- HashMaps are ideal for:
  - counting
  - frequency problems
  - duplicates
  - lookups
- TreeMaps maintain sorted order
- HashMaps sacrifice ordering for speed

---

# Python Built-in Hash Structures

## HashSet

```python
s = set()

s.add(1)
s.add(2)
s.add(2)

print(s)
```

Output:

```python
{1, 2}
```

Duplicates are ignored.

---

## HashMap

```python
m = {}

m["name"] = "Sid"
m["age"] = 25

print(m)
```

Output:

```python
{
    "name": "Sid",
    "age": 25
}
```

Python dictionaries are highly optimized hashmaps internally. Entire modern software systems are basically held together by hash tables and caffeine.
````
