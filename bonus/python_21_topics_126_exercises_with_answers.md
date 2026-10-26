# Python Practice Workbook: 126 Exercises with Answers

**21 topics · 6 exercises per topic · 2 beginner, 2 intermediate, 2 advanced per topic**

Every exercise includes a task, an answer, and a short explanation. Python examples are designed as standalone snippets unless the prompt says otherwise. Git examples use terminal commands. Web-scraping tasks emphasize permitted access, timeouts, request limits, and respectful usage.

## How to use this workbook

1. Read only the task first and attempt it yourself.
2. Run your solution and test an ordinary case plus an edge case.
3. Compare it with the answer and explain why it works.
4. For advanced exercises, consider time complexity, validation, error handling, and maintainability.

## Topics
1. 1. List comprehensions
2. 2. Lists
3. 3. Tuples
4. 4. Sets
5. 5. Dictionaries
6. 6. Built-in Methods
7. 7. Lambda
8. 8. Functions
9. 9. OOP and Inheritance
10. 10. JSON and CSV Files
11. 11. If statements
12. 12. While loops
13. 13. For loops
14. 14. Operators
15. 15. Strings
16. 16. File I/O
17. 17. Try / Except
18. 18. Regular Expressions (Regex)
19. 19. sqlite3
20. 20. Web Scraping
21. 21. Git

---

# 1. List comprehensions

## 1. [Beginner] Squares from 1 to 10

**Exercise:** Create a list containing the square of every integer from 1 through 10.

**Answer:**

```python
squares = [n ** 2 for n in range(1, 11)]
print(squares)
```

**Explanation:** The expression comes first, followed by the loop that supplies each value.

## 2. [Beginner] Keep only even numbers

**Exercise:** From `numbers`, create a list containing only even numbers.

**Answer:**

```python
numbers = [3, 8, 11, 14, 17, 20]
evens = [n for n in numbers if n % 2 == 0]
print(evens)
```

**Explanation:** The `if` at the end filters values; it does not choose the output value.

## 3. [Intermediate] Flatten a nested list

**Exercise:** Convert a list of lists into one flat list using a comprehension.

**Answer:**

```python
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [value for row in matrix for value in row]
print(flat)
```

**Explanation:** The outer loop appears before the inner loop, matching normal nested-loop order.

## 4. [Intermediate] Build a dictionary of grades

**Exercise:** Given `scores`, create a dictionary mapping each student's name to `Pass` for scores >= 60 and `Fail` otherwise.

**Answer:**

```python
scores = {"Ana": 82, "Ben": 54, "Cara": 60}
grades = {name: ("Pass" if score >= 60 else "Fail") for name, score in scores.items()}
print(grades)
```

**Explanation:** A dictionary comprehension uses `{key: value for ...}`; the conditional expression returns the value.

## 5. [Advanced] Transpose a matrix

**Exercise:** Transpose a rectangular matrix using a nested comprehension without NumPy.

**Answer:**

```python
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = [[row[col] for row in matrix] for col in range(len(matrix[0]))]
print(transposed)
```

**Explanation:** The outer loop walks columns; the inner loop collects one value from each original row.

## 6. [Advanced] Word frequency with normalization

**Exercise:** Count words case-insensitively, ignoring punctuation, using comprehensions and a dictionary comprehension.

**Answer:**

```python
import re
text = "Data matters. DATA drives decisions; data helps!"
words = re.findall(r"[a-z]+", text.lower())
counts = {word: words.count(word) for word in set(words)}
print(counts)
```

**Explanation:** This is easy to read for small text, but `words.count` repeated for each unique word is less efficient for large text; use `collections.Counter` for production.

---

# 2. Lists

## 1. [Beginner] Update a shopping list

**Exercise:** Append `"bread"`, insert `"milk"` at the beginning, then remove `"eggs"`.

**Answer:**

```python
items = ["eggs", "apples"]
items.append("bread")
items.insert(0, "milk")
items.remove("eggs")
print(items)
```

**Explanation:** `append` adds to the end, `insert` adds at an index, and `remove` deletes the first matching value.

## 2. [Beginner] Use slicing

**Exercise:** Given `numbers`, print the reversed list and every second element.

**Answer:**

```python
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[::-1])
print(numbers[::2])
```

**Explanation:** A slice uses `[start:stop:step]`; a step of `-1` reverses a sequence.

## 3. [Intermediate] Rotate a list right

**Exercise:** Rotate a non-empty list to the right by `k` positions. Handle `k` larger than the list length.

**Answer:**

```python
values = [1, 2, 3, 4, 5]
k = 7
k %= len(values)
rotated = values[-k:] + values[:-k] if k else values[:]
print(rotated)
```

**Explanation:** Modulo reduces `k` to a valid rotation; the `k == 0` case avoids the confusing `[-0:]` slice.

## 4. [Intermediate] Remove duplicates but keep order

**Exercise:** Return a list with duplicates removed while preserving the first occurrence order.

**Answer:**

```python
values = [4, 2, 4, 1, 2, 5, 1]
seen = set()
unique = []
for value in values:
    if value not in seen:
        seen.add(value)
        unique.append(value)
print(unique)
```

**Explanation:** A set gives fast membership checks; the output list preserves input order.

## 5. [Advanced] Move zeros to the end

**Exercise:** Move all zero values to the end without changing the order of non-zero values.

**Answer:**

```python
values = [0, 3, 0, 1, 8, 0, 2]
nonzero = [value for value in values if value != 0]
zeros = [value for value in values if value == 0]
result = nonzero + zeros
print(result)
```

**Explanation:** This creates a new list in O(n) time and preserves the relative order of values.

## 6. [Advanced] Merge two sorted lists

**Exercise:** Merge two already sorted lists into one sorted list without calling `sort()` or `sorted()`.

**Answer:**

```python
a = [1, 4, 7, 10]
b = [2, 3, 8]
i = j = 0
merged = []
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1
merged.extend(a[i:])
merged.extend(b[j:])
print(merged)
```

**Explanation:** Two pointers compare the next unmerged values; the remaining tail can be appended at the end.

---

# 3. Tuples

## 1. [Beginner] Unpack a tuple

**Exercise:** Unpack the tuple into `name`, `age`, and `city`, then print each value.

**Answer:**

```python
person = ("Mina", 28, "Tehran")
name, age, city = person
print(name, age, city)
```

**Explanation:** Unpacking assigns tuple elements to variables in order.

## 2. [Beginner] Count and locate values

**Exercise:** Count how many times `2` occurs and find the first index of `5`.

**Answer:**

```python
values = (2, 5, 2, 7, 2, 5)
print(values.count(2))
print(values.index(5))
```

**Explanation:** Tuples support `count` and `index`; `index` raises `ValueError` if the value is absent.

## 3. [Intermediate] Return multiple results

**Exercise:** Write a function returning the minimum and maximum of a non-empty list, then unpack the result.

**Answer:**

```python
def min_max(values):
    if not values:
        raise ValueError("values must not be empty")
    return min(values), max(values)
low, high = min_max([7, 2, 11, 4])
print(low, high)
```

**Explanation:** A function can return a tuple implicitly when multiple values are separated by commas.

## 4. [Intermediate] Use tuples as dictionary keys

**Exercise:** Count how often each `(x, y)` coordinate appears.

**Answer:**

```python
points = [(1, 2), (2, 3), (1, 2), (0, 0), (2, 3)]
counts = {}
for point in points:
    counts[point] = counts.get(point, 0) + 1
print(counts)
```

**Explanation:** Tuples containing hashable values can be dictionary keys; lists cannot.

## 5. [Advanced] Sort records with tuple unpacking

**Exercise:** Sort records by department, then salary descending, then unpack the first record.

**Answer:**

```python
employees = [("Nora", "Data", 72000), ("Ali", "IT", 68000), ("Sara", "Data", 81000)]
ordered = sorted(employees, key=lambda row: (row[1], -row[2]))
name, department, salary = ordered[0]
print(ordered)
print(name, department, salary)
```

**Explanation:** The key produces `(department, negative salary)` so salaries are descending within each department.

## 6. [Advanced] Use named tuples

**Exercise:** Define a `Point` named tuple and calculate the Manhattan distance from the origin.

**Answer:**

```python
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, -5)
distance = abs(p.x) + abs(p.y)
print(p.x, p.y, distance)
```

**Explanation:** Named tuples keep tuple immutability while making fields easier to understand by name.

---

# 4. Sets

## 1. [Beginner] Remove duplicates

**Exercise:** Create a set of unique numbers from a list.

**Answer:**

```python
numbers = [2, 2, 3, 5, 3, 7, 7]
unique_numbers = set(numbers)
print(unique_numbers)
```

**Explanation:** Sets contain unique hashable items; their display order should not be relied on.

## 2. [Beginner] Union and intersection

**Exercise:** Find everyone enrolled in either course and everyone enrolled in both.

**Answer:**

```python
python_students = {"Ava", "Ben", "Mina"}
sql_students = {"Ben", "Mina", "Omar"}
print("Either:", python_students | sql_students)
print("Both:", python_students & sql_students)
```

**Explanation:** `|` is union and `&` is intersection.

## 3. [Intermediate] Calculate Jaccard similarity

**Exercise:** Calculate Jaccard similarity: intersection size divided by union size.

**Answer:**

```python
a = {"sql", "python", "excel", "power bi"}
b = {"python", "pandas", "sql"}
union = a | b
similarity = len(a & b) / len(union) if union else 1.0
print(round(similarity, 3))
```

**Explanation:** The empty-union convention is defined here as 1.0; choose and document a convention suitable for your problem.

## 4. [Intermediate] Find permissions unique to each role

**Exercise:** Given `admin` and `analyst` permissions, find permissions unique to each and those shared.

**Answer:**

```python
admin = {"read", "write", "delete", "export"}
analyst = {"read", "export", "query"}
print("Admin only:", admin - analyst)
print("Analyst only:", analyst - admin)
print("Shared:", admin & analyst)
```

**Explanation:** Set difference finds items present in one set and absent from the other.

## 5. [Advanced] Find repeated items using sets

**Exercise:** Return the distinct values that occur more than once in a sequence.

**Answer:**

```python
values = ["a", "b", "c", "a", "d", "b", "a"]
seen = set()
duplicates = set()
for value in values:
    if value in seen:
        duplicates.add(value)
    else:
        seen.add(value)
print(duplicates)
```

**Explanation:** This runs in expected O(n) time and reports each duplicate value once.

## 6. [Advanced] Validate required fields

**Exercise:** Check whether all required columns exist in a list of CSV headers, and report the missing names.

**Answer:**

```python
headers = {"order_id", "order_date", "revenue", "customer_id"}
required = {"order_id", "order_date", "revenue", "region"}
missing = required - headers
extra = headers - required
print("Missing:", missing)
print("Extra:", extra)
print("Valid:", not missing)
```

**Explanation:** Set operations make schema checks concise. In production, distinguish required fields from optional extra fields.

---

# 5. Dictionaries

## 1. [Beginner] Look up inventory

**Exercise:** Print the stock of `pen`; show `0` if the key does not exist.

**Answer:**

```python
stock = {"pen": 12, "notebook": 7, "eraser": 0}
print(stock.get("pen", 0))
print(stock.get("marker", 0))
```

**Explanation:** `get` avoids a `KeyError` when a key is absent.

## 2. [Beginner] Count occurrences

**Exercise:** Count each character in a word using a dictionary.

**Answer:**

```python
word = "banana"
counts = {}
for char in word:
    counts[char] = counts.get(char, 0) + 1
print(counts)
```

**Explanation:** `dict.get(key, default)` makes a simple counter easy to write.

## 3. [Intermediate] Merge and sum dictionaries

**Exercise:** Combine two dictionaries of product quantities by adding values for matching keys.

**Answer:**

```python
left = {"pen": 4, "book": 2}
right = {"pen": 3, "pencil": 5}
total = left.copy()
for item, quantity in right.items():
    total[item] = total.get(item, 0) + quantity
print(total)
```

**Explanation:** This is an aggregation merge; dictionary unpacking alone would overwrite duplicate keys instead of adding them.

## 4. [Intermediate] Invert a dictionary with repeated values

**Exercise:** Convert a name-to-team mapping into a team-to-list-of-names mapping.

**Answer:**

```python
people = {"Ana": "Data", "Ben": "IT", "Cara": "Data", "Dara": "IT"}
inverted = {}
for name, team in people.items():
    inverted.setdefault(team, []).append(name)
print(inverted)
```

**Explanation:** `setdefault` creates a list the first time a team is seen, then appends each name.

## 5. [Advanced] Aggregate transaction records

**Exercise:** Aggregate transaction dictionaries into total revenue per customer.

**Answer:**

```python
transactions = [{"customer": "A", "amount": 12}, {"customer": "B", "amount": 9}, {"customer": "A", "amount": 5}]
totals = {}
for transaction in transactions:
    customer = transaction["customer"]
    totals[customer] = totals.get(customer, 0) + transaction["amount"]
print(totals)
```

**Explanation:** This pattern is useful when working with JSON-like records before loading them into a DataFrame.

## 6. [Advanced] Recursively merge nested dictionaries

**Exercise:** Write a function that recursively merges dictionaries; when both values are dictionaries, merge their contents; otherwise the right-hand value wins.

**Answer:**

```python
def deep_merge(left, right):
    result = left.copy()
    for key, value in right.items():
        if isinstance(result.get(key), dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result

base = {"db": {"host": "localhost", "port": 5432}, "debug": False}
override = {"db": {"port": 5433}, "debug": True}
print(deep_merge(base, override))
```

**Explanation:** This shallow-copies each level and recursively merges nested dictionaries. Mutable nested values not replaced or merged may still be shared by reference.

---

# 6. Built-in Methods

## 1. [Beginner] Clean a user input

**Exercise:** Strip surrounding spaces, make the text lowercase, and replace spaces with hyphens.

**Answer:**

```python
raw = "  Data Analysis Bootcamp  "
slug = raw.strip().lower().replace(" ", "-")
print(slug)
```

**Explanation:** String methods return new strings; strings themselves are immutable.

## 2. [Beginner] Join words

**Exercise:** Turn a list of words into a comma-separated string.

**Answer:**

```python
words = ["SQL", "Python", "Power BI"]
result = ", ".join(words)
print(result)
```

**Explanation:** `join` is called on the separator string and requires string elements.

## 3. [Intermediate] Sort a list in place

**Exercise:** Sort scores descending in place and report the highest three.

**Answer:**

```python
scores = [71, 94, 82, 66, 88, 97]
scores.sort(reverse=True)
print(scores[:3])
```

**Explanation:** `.sort()` mutates the list and returns `None`; `sorted(scores)` creates a new list.

## 4. [Intermediate] Use dictionary methods safely

**Exercise:** Update a configuration, remove a key if present, and inspect the remaining key-value pairs.

**Answer:**

```python
config = {"theme": "light", "language": "en"}
config.update({"theme": "dark", "autosave": True})
removed = config.pop("language", "not set")
print("Removed:", removed)
print(list(config.items()))
```

**Explanation:** `update` modifies a dictionary; `pop(key, default)` avoids an error if a key is absent.

## 5. [Advanced] Build a frequency report with built-in methods

**Exercise:** Normalize whitespace and case, split a sentence, then use `count` to report occurrences of a requested word.

**Answer:**

```python
sentence = "SQL   is useful. Python is useful, and SQL is popular."
words = sentence.lower().replace(".", "").replace(",", "").split()
for target in ["sql", "python", "useful"]:
    print(target, words.count(target))
```

**Explanation:** This method is fine for small text; repeated `.count()` scans the list repeatedly, so `Counter` is preferable for large inputs.

## 6. [Advanced] Use `zip` and `dict` to create a lookup

**Exercise:** Combine lists of column names and values into a dictionary, and detect mismatched lengths.

**Answer:**

```python
columns = ["name", "score", "passed"]
values = ["Mina", 91, True]
if len(columns) != len(values):
    raise ValueError("columns and values must have equal lengths")
record = dict(zip(columns, values, strict=True))
print(record)
```

**Explanation:** `zip(..., strict=True)` is available in Python 3.10+ and raises a ValueError for mismatched iterables.

---

# 7. Lambda

## 1. [Beginner] Sort tuples by second item

**Exercise:** Sort `(name, score)` pairs by score from highest to lowest using a lambda.

**Answer:**

```python
scores = [("Ana", 82), ("Ben", 95), ("Cara", 88)]
print(sorted(scores, key=lambda item: item[1], reverse=True))
```

**Explanation:** The lambda returns the value used as the sort key.

## 2. [Beginner] Use a lambda for absolute values

**Exercise:** Create a list of absolute values using `map` and a lambda.

**Answer:**

```python
numbers = [-5, 2, -9, 4]
absolute = list(map(lambda n: abs(n), numbers))
print(absolute)
```

**Explanation:** This illustrates lambda syntax; a list comprehension is often clearer for this transformation.

## 3. [Intermediate] Filter then transform

**Exercise:** Keep positive numbers and square them using `filter` and `map` with lambdas.

**Answer:**

```python
numbers = [-3, 0, 2, 5, -1, 4]
result = list(map(lambda n: n ** 2, filter(lambda n: n > 0, numbers)))
print(result)
```

**Explanation:** `filter` selects values first; `map` transforms the selected values. A comprehension can express both in one line.

## 4. [Intermediate] Sort employees by department and salary

**Exercise:** Sort employee tuples by department ascending and salary descending.

**Answer:**

```python
employees = [("Ana", "Data", 75000), ("Ben", "IT", 70000), ("Cara", "Data", 90000)]
result = sorted(employees, key=lambda row: (row[1], -row[2]))
print(result)
```

**Explanation:** A tuple key supports multiple sort criteria; negating salary reverses that component.

## 5. [Advanced] Use `reduce` to multiply values

**Exercise:** Use `functools.reduce` and a lambda to compute a product. Explain why a loop might sometimes be clearer.

**Answer:**

```python
from functools import reduce
numbers = [2, 3, 4, 5]
product = reduce(lambda acc, value: acc * value, numbers, 1)
print(product)
```

**Explanation:** The accumulator starts at 1 and multiplies each value. For ordinary numeric products, a loop can be easier to debug.

## 6. [Advanced] Build a key function using a lambda

**Exercise:** Given nested records, sort by missingness first, then by score descending, then by name.

**Answer:**

```python
records = [{"name": "Mina", "score": 90}, {"name": "Ali", "score": None}, {"name": "Sara", "score": 90}]
ordered = sorted(records, key=lambda r: (r["score"] is None, -(r["score"] or 0), r["name"]))
print(ordered)
```

**Explanation:** The first key component places missing scores last. This is concise but can become hard to read; a named key function is often better in production.

---

# 8. Functions

## 1. [Beginner] Write a greeting function

**Exercise:** Write `greet(name)` that returns a greeting string and call it.

**Answer:**

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Mina"))
```

**Explanation:** Use `return` to send a value to the caller; `print` only displays it.

## 2. [Beginner] Calculate a safe average

**Exercise:** Write a function that returns the average of a list, and raises a ValueError for an empty list.

**Answer:**

```python
def average(values):
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)

print(average([10, 20, 30]))
```

**Explanation:** Validate the input before dividing to avoid a division-by-zero error.

## 3. [Intermediate] Use keyword arguments and defaults

**Exercise:** Write a function calculating a price after an optional discount percentage; default discount is zero and reject invalid rates.

**Answer:**

```python
def final_price(price, discount_pct=0):
    if price < 0:
        raise ValueError("price must be non-negative")
    if not 0 <= discount_pct <= 100:
        raise ValueError("discount_pct must be between 0 and 100")
    return price * (1 - discount_pct / 100)

print(final_price(80, discount_pct=15))
```

**Explanation:** Keyword arguments make calls easier to read. Validate assumptions at the function boundary.

## 4. [Intermediate] Return a summary dictionary

**Exercise:** Write a function returning count, min, max, and mean for a numeric list.

**Answer:**

```python
def summarize(values):
    if not values:
        raise ValueError("values must not be empty")
    return {"count": len(values), "min": min(values), "max": max(values), "mean": sum(values) / len(values)}

print(summarize([4, 7, 10, 13]))
```

**Explanation:** A dictionary lets callers access results by meaningful keys rather than remembering tuple positions.

## 5. [Advanced] Recursively flatten nested lists

**Exercise:** Write a recursive function that flattens nested lists while treating non-list values as individual items.

**Answer:**

```python
def flatten(items):
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, [2, [3, 4]], [5, 6]]))
```

**Explanation:** The recursive call handles each nested list; the base case is a value that is not a list.

## 6. [Advanced] Memoize a recursive calculation

**Exercise:** Use `functools.lru_cache` to compute Fibonacci numbers efficiently.

**Answer:**

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(35))
```

**Explanation:** Memoization stores prior results so recursive subproblems are not recalculated repeatedly.

---

# 9. OOP and Inheritance

## 1. [Beginner] Create a Rectangle class

**Exercise:** Create a `Rectangle` class with width and height and an `area()` method.

**Answer:**

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rectangle = Rectangle(4, 6)
print(rectangle.area())
```

**Explanation:** `__init__` initializes an instance; `self` refers to that instance.

## 2. [Beginner] Create a BankAccount class

**Exercise:** Create an account with a balance and a `deposit(amount)` method that rejects non-positive deposits.

**Answer:**

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount
        return self.balance

account = BankAccount("Mina")
print(account.deposit(100))
```

**Explanation:** Methods are functions associated with objects; methods can preserve rules around object state.

## 3. [Intermediate] Inherit from Employee

**Exercise:** Create a base `Employee` and subclass `HourlyEmployee` that calculates pay from hours and hourly rate.

**Answer:**

```python
class Employee:
    def __init__(self, name):
        self.name = name

class HourlyEmployee(Employee):
    def __init__(self, name, hours, hourly_rate):
        super().__init__(name)
        self.hours = hours
        self.hourly_rate = hourly_rate

    def pay(self):
        return self.hours * self.hourly_rate

worker = HourlyEmployee("Ali", 38, 20)
print(worker.name, worker.pay())
```

**Explanation:** `super().__init__()` reuses base-class initialization while the subclass adds its own attributes.

## 4. [Intermediate] Override a method

**Exercise:** Create a base `Notification.send()` and subclass `EmailNotification` with an overridden method.

**Answer:**

```python
class Notification:
    def send(self, message):
        return f"Notification: {message}"

class EmailNotification(Notification):
    def send(self, message):
        return f"Email sent: {message}"

for notifier in [Notification(), EmailNotification()]:
    print(notifier.send("Report ready"))
```

**Explanation:** Method overriding allows subclasses to provide specialized behavior with a shared interface.

## 5. [Advanced] Use an abstract base class

**Exercise:** Create an abstract `Shape` class with `area()`, then implement `Circle` and `Rectangle`.

**Answer:**

```python
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width, self.height = width, height
    def area(self):
        return self.width * self.height

shapes = [Circle(2), Rectangle(3, 4)]
print([round(shape.area(), 2) for shape in shapes])
```

**Explanation:** An abstract base class defines an interface; polymorphism lets the same call work with different shapes.

## 6. [Advanced] Extend a product with inheritance and validation

**Exercise:** Create `Product` and `DiscountedProduct`; validate prices and override final-price behavior.

**Answer:**

```python
class Product:
    def __init__(self, name, price):
        if price < 0:
            raise ValueError("price cannot be negative")
        self.name = name
        self.price = price

    def final_price(self):
        return self.price

class DiscountedProduct(Product):
    def __init__(self, name, price, discount_pct):
        super().__init__(name, price)
        if not 0 <= discount_pct <= 100:
            raise ValueError("discount must be between 0 and 100")
        self.discount_pct = discount_pct

    def final_price(self):
        return self.price * (1 - self.discount_pct / 100)

item = DiscountedProduct("Keyboard", 80, 20)
print(item.name, item.final_price())
```

**Explanation:** The subclass reuses the base validation and overrides only the behavior that differs.

---

# 10. JSON and CSV Files

## 1. [Beginner] Write and read JSON

**Exercise:** Save a Python dictionary to `profile.json`, then read it back.

**Answer:**

```python
import json
profile = {"name": "Mina", "role": "Data Analyst", "skills": ["SQL", "Python"]}
with open("profile.json", "w", encoding="utf-8") as file:
    json.dump(profile, file, ensure_ascii=False, indent=2)
with open("profile.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)
print(loaded)
```

**Explanation:** `json.dump` writes JSON to a file; `json.load` reads JSON from a file.

## 2. [Beginner] Read a CSV with DictReader

**Exercise:** Read `sales.csv` and print each row as a dictionary. Assume the file has a header.

**Answer:**

```python
import csv
with open("sales.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
```

**Explanation:** `DictReader` maps each column header to its row value. Values are initially strings.

## 3. [Intermediate] Convert CSV rows to JSON

**Exercise:** Read a CSV and write its rows to a JSON array.

**Answer:**

```python
import csv, json
with open("input.csv", newline="", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))
with open("output.json", "w", encoding="utf-8") as file:
    json.dump(rows, file, ensure_ascii=False, indent=2)
print(f"Converted {len(rows)} rows")
```

**Explanation:** This approach is simple but loads the whole CSV into memory, so it is best for small or medium files.

## 4. [Intermediate] Read JSON Lines and sum revenue

**Exercise:** Each line of `orders.jsonl` contains one JSON object with a numeric `revenue`. Sum the revenue safely.

**Answer:**

```python
import json
revenue_total = 0.0
with open("orders.jsonl", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        if not line.strip():
            continue
        record = json.loads(line)
        revenue_total += float(record["revenue"])
print(revenue_total)
```

**Explanation:** JSON Lines stores one JSON value per line and can be processed incrementally. Add validation and error handling for untrusted files.

## 5. [Advanced] Stream a large CSV report

**Exercise:** Compute row count and total revenue without loading the entire CSV into memory.

**Answer:**

```python
import csv
row_count = 0
total_revenue = 0.0
with open("sales.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row_count += 1
        total_revenue += float(row["revenue"])
print("Rows:", row_count)
print("Revenue:", round(total_revenue, 2))
```

**Explanation:** Iterating over `DictReader` processes a row at a time, reducing memory requirements.

## 6. [Advanced] Validate a CSV schema before processing

**Exercise:** Check that required headers exist and reject unexpected missing fields before aggregating.

**Answer:**

```python
import csv
required = {"order_id", "order_date", "revenue"}
with open("sales.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    headers = set(reader.fieldnames or [])
    missing = required - headers
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    rows = list(reader)
print(f"Validated schema; loaded {len(rows)} rows")
```

**Explanation:** Validate the schema explicitly so a renamed or missing column fails early with a helpful error.

---

# 11. If statements

## 1. [Beginner] Pass or fail

**Exercise:** Print `Pass` for a score of 60 or higher, otherwise print `Fail`.

**Answer:**

```python
score = 74
if score >= 60:
    print("Pass")
else:
    print("Fail")
```

**Explanation:** The condition is evaluated as a Boolean; indentation defines the branch body.

## 2. [Beginner] Classify a number

**Exercise:** Print whether a number is positive, negative, or zero.

**Answer:**

```python
number = -3
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

**Explanation:** `elif` tests another condition only when earlier conditions are false.

## 3. [Intermediate] Check a leap year

**Exercise:** Implement leap-year rules correctly.

**Answer:**

```python
year = 2024
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
```

**Explanation:** A year divisible by 100 is not a leap year unless it is also divisible by 400.

## 4. [Intermediate] Apply progressive shipping rules

**Exercise:** Shipping is free for orders >= 100; otherwise it costs 5, except remote orders cost an additional 8.

**Answer:**

```python
order_total = 75
is_remote = True
if order_total >= 100:
    shipping = 0
else:
    shipping = 5
    if is_remote:
        shipping += 8
print("Shipping:", shipping)
```

**Explanation:** Separate the threshold decision from the additional condition to make the rules clear.

## 5. [Advanced] Validate a triangle

**Exercise:** Given three side lengths, determine whether they form a valid triangle and classify it as equilateral, isosceles, or scalene.

**Answer:**

```python
a, b, c = 3, 4, 5
valid = min(a, b, c) > 0 and a + b > c and a + c > b and b + c > a
if not valid:
    print("Invalid triangle")
elif a == b == c:
    print("Equilateral")
elif a == b or a == c or b == c:
    print("Isosceles")
else:
    print("Scalene")
```

**Explanation:** Triangle inequality must be validated before classifying the sides.

## 6. [Advanced] Choose a pricing tier with precedence

**Exercise:** Implement pricing: VIP gets 20% off; otherwise orders >= 200 get 10% off; orders >= 100 get 5% off; no discount otherwise.

**Answer:**

```python
total = 240
is_vip = True
if is_vip:
    rate = 0.20
elif total >= 200:
    rate = 0.10
elif total >= 100:
    rate = 0.05
else:
    rate = 0.0
final_total = total * (1 - rate)
print(rate, round(final_total, 2))
```

**Explanation:** Order conditions from highest-priority rule to lower-priority rules so a VIP does not fall into a later category.

---

# 12. While loops

## 1. [Beginner] Countdown

**Exercise:** Print numbers from 5 down to 1, then print `Go!`.

**Answer:**

```python
n = 5
while n > 0:
    print(n)
    n -= 1
print("Go!")
```

**Explanation:** The loop condition must eventually become false; decrementing `n` prevents an infinite loop.

## 2. [Beginner] Count attempts

**Exercise:** Simulate a user making three attempts and print the attempt number each time.

**Answer:**

```python
attempt = 1
while attempt <= 3:
    print("Attempt", attempt)
    attempt += 1
```

**Explanation:** An incremented counter is a common way to bound a `while` loop.

## 3. [Intermediate] Double until a threshold

**Exercise:** Starting at 3, double the value until it reaches or exceeds 1000, and report how many doublings occurred.

**Answer:**

```python
value = 3
steps = 0
while value < 1000:
    value *= 2
    steps += 1
print(value, steps)
```

**Explanation:** Track both the evolving value and the number of loop iterations.

## 4. [Intermediate] Number guessing without input

**Exercise:** Use a `while` loop to compare a list of guesses with a target, stopping at the first correct guess.

**Answer:**

```python
target = 17
guesses = [8, 12, 17, 20]
index = 0
while index < len(guesses):
    guess = guesses[index]
    print("Guess:", guess)
    if guess == target:
        print("Correct")
        break
    index += 1
```

**Explanation:** `break` exits the loop immediately when the target is found.

## 5. [Advanced] Generate a Collatz sequence safely

**Exercise:** Generate the Collatz sequence starting from a positive integer; stop at 1 and impose an iteration guard.

**Answer:**

```python
n = 27
if n <= 0:
    raise ValueError("n must be positive")
sequence = [n]
max_steps = 10000
while n != 1 and len(sequence) < max_steps:
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    sequence.append(n)
if sequence[-1] != 1:
    raise RuntimeError("iteration limit reached")
print("Steps:", len(sequence) - 1)
print("Sequence:", sequence)
```

**Explanation:** The guard prevents an accidental unbounded run; the Collatz conjecture is not proven for every positive integer.

## 6. [Advanced] Implement a bounded retry loop

**Exercise:** Simulate retries for an operation that fails twice and succeeds on the third attempt, with a maximum number of attempts.

**Answer:**

```python
max_attempts = 4
attempts = 0
success_on = 3
while attempts < max_attempts:
    attempts += 1
    print("Trying", attempts)
    if attempts == success_on:
        print("Success")
        break
else:
    print("Operation failed after all attempts")
```

**Explanation:** A `while ... else` block runs only if the loop finishes without `break`. Real retry code should catch only known transient errors and usually include delays.

---

# 13. For loops

## 1. [Beginner] Sum numbers

**Exercise:** Calculate the sum of all values in a list using a `for` loop.

**Answer:**

```python
numbers = [5, 10, 15, 20]
total = 0
for number in numbers:
    total += number
print(total)
```

**Explanation:** The accumulator adds each value to the running total.

## 2. [Beginner] Number each name

**Exercise:** Print each name with a one-based line number.

**Answer:**

```python
names = ["Mina", "Ali", "Sara"]
for index, name in enumerate(names, start=1):
    print(index, name)
```

**Explanation:** `enumerate` gives an index and value without manually maintaining a counter.

## 3. [Intermediate] Find prime numbers

**Exercise:** Write a function checking primality and use a `for` loop to list primes through 50.

**Answer:**

```python
def is_prime(n):
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True
print([n for n in range(2, 51) if is_prime(n)])
```

**Explanation:** Only testing divisors up to the square root is sufficient because factors occur in pairs.

## 4. [Intermediate] Calculate row totals

**Exercise:** Use nested `for` loops to calculate the sum of each row in a matrix.

**Answer:**

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row_totals = []
for row in matrix:
    total = 0
    for value in row:
        total += value
    row_totals.append(total)
print(row_totals)
```

**Explanation:** The inner loop totals one row; the outer loop repeats that work for each row.

## 5. [Advanced] Find top products without sorting the entire list

**Exercise:** Aggregate sales per product from transaction records and display the top two products. Use `heapq.nlargest`.

**Answer:**

```python
from collections import defaultdict
from heapq import nlargest
sales = [("pen", 12), ("book", 30), ("pen", 8), ("bag", 50), ("book", 15)]
totals = defaultdict(float)
for product, amount in sales:
    totals[product] += amount
top_two = nlargest(2, totals.items(), key=lambda item: item[1])
print(top_two)
```

**Explanation:** Aggregation happens in one pass; `nlargest` can avoid fully sorting a large collection when only a small top-k is needed.

## 6. [Advanced] Build Fibonacci numbers iteratively

**Exercise:** Generate the first `n` Fibonacci numbers using a loop, without recursion.

**Answer:**

```python
n = 12
sequence = []
a, b = 0, 1
for _ in range(n):
    sequence.append(a)
    a, b = b, a + b
print(sequence)
```

**Explanation:** Tuple assignment updates both values simultaneously using the old values on the right-hand side.

---

# 14. Operators

## 1. [Beginner] Use arithmetic operators

**Exercise:** Given price and quantity, calculate subtotal and a 10% discount.

**Answer:**

```python
price = 25
quantity = 4
subtotal = price * quantity
discount = subtotal * 0.10
print(subtotal, subtotal - discount)
```

**Explanation:** `*` multiplies and `-` subtracts; variable names make the calculation easier to read.

## 2. [Beginner] Floor division and modulo

**Exercise:** For 29 items packed into boxes of 6, calculate full boxes and remaining items.

**Answer:**

```python
items = 29
box_size = 6
full_boxes = items // box_size
remaining = items % box_size
print(full_boxes, remaining)
```

**Explanation:** `//` gives the floor quotient and `%` gives the remainder.

## 3. [Intermediate] Use logical and membership operators

**Exercise:** Check whether a user can access a report: they must be active and have either `analyst` or `admin` role.

**Answer:**

```python
user = {"active": True, "role": "analyst"}
can_access = user["active"] and user["role"] in {"analyst", "admin"}
print(can_access)
```

**Explanation:** Combine Boolean expressions with `and`, and membership with `in`.

## 4. [Intermediate] Use bitwise flags

**Exercise:** Represent read/write/execute permissions as bit flags and check whether a permission is enabled.

**Answer:**

```python
READ, WRITE, EXECUTE = 1, 2, 4
permissions = READ | WRITE
print("Can read:", bool(permissions & READ))
print("Can execute:", bool(permissions & EXECUTE))
permissions |= EXECUTE
print("Updated:", permissions)
```

**Explanation:** Bitwise OR combines flags; bitwise AND checks whether a flag bit is set.

## 5. [Advanced] Check whether two time intervals overlap

**Exercise:** Given intervals `[start, end)` for two meetings, determine whether they overlap.

**Answer:**

```python
a_start, a_end = 9, 11
b_start, b_end = 10, 12
overlap = max(a_start, b_start) < min(a_end, b_end)
print(overlap)
```

**Explanation:** Using half-open intervals means a meeting ending exactly when another begins is not considered an overlap.

## 6. [Advanced] Implement permission masks

**Exercise:** Define read/write/delete flags and test if a user has both read and write permissions but not delete permission.

**Answer:**

```python
READ, WRITE, DELETE = 1, 2, 4
required = READ | WRITE
user_permissions = READ | WRITE
has_required = (user_permissions & required) == required
can_delete = bool(user_permissions & DELETE)
print(has_required, can_delete)
```

**Explanation:** Comparing the masked bits with `required` ensures all required flags are present, not just one.

---

# 15. Strings

## 1. [Beginner] Normalize a string

**Exercise:** Trim spaces and convert a text value to lowercase.

**Answer:**

```python
text = "  Data Analyst  "
cleaned = text.strip().lower()
print(cleaned)
```

**Explanation:** `strip` removes surrounding whitespace, and `lower` normalizes case.

## 2. [Beginner] Count vowels

**Exercise:** Count vowels in a string, ignoring case.

**Answer:**

```python
text = "Data Analysis"
vowels = set("aeiou")
count = sum(1 for char in text.lower() if char in vowels)
print(count)
```

**Explanation:** A generator expression counts only characters that belong to the vowel set.

## 3. [Intermediate] Normalize whitespace and title case

**Exercise:** Collapse repeated whitespace and title-case a person's name.

**Answer:**

```python
import re
raw = "   mINA    eIDI  "
cleaned = re.sub(r"\s+", " ", raw).strip().title()
print(cleaned)
```

**Explanation:** Title case is useful for simple names but is not correct for every cultural naming convention.

## 4. [Intermediate] Check a normalized palindrome

**Exercise:** Check whether a phrase is a palindrome while ignoring spaces, punctuation, and case.

**Answer:**

```python
import re
text = "A man, a plan, a canal: Panama!"
normalized = re.sub(r"[^a-z0-9]", "", text.lower())
print(normalized == normalized[::-1])
```

**Explanation:** Normalization defines what characters matter before comparing the text with its reverse.

## 5. [Advanced] Find the longest substring without repeating characters

**Exercise:** Return the length of the longest substring containing no repeated characters.

**Answer:**

```python
def longest_unique_length(text):
    last_seen = {}
    left = best = 0
    for right, char in enumerate(text):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1
        last_seen[char] = right
        best = max(best, right - left + 1)
    return best
print(longest_unique_length("abrkaabcdefghijjxxx"))
```

**Explanation:** The sliding-window method runs in O(n) expected time by tracking the last index of each character.

## 6. [Advanced] Run-length encode a string

**Exercise:** Compress repeated consecutive characters, e.g. `aaabbc` into `a3b2c1`.

**Answer:**

```python
def run_length_encode(text):
    if not text:
        return ""
    parts = []
    current = text[0]
    count = 1
    for char in text[1:]:
        if char == current:
            count += 1
        else:
            parts.append(f"{current}{count}")
            current, count = char, 1
    parts.append(f"{current}{count}")
    return "".join(parts)
print(run_length_encode("aaabbc"))
```

**Explanation:** Track the current character and run length, emitting a segment whenever the character changes.

---

# 16. File I/O

## 1. [Beginner] Write and read a text file

**Exercise:** Write three lines to `notes.txt`, then read and print the file.

**Answer:**

```python
from pathlib import Path
path = Path("notes.txt")
path.write_text("Learn SQL\nPractice pandas\nBuild a dashboard\n", encoding="utf-8")
print(path.read_text(encoding="utf-8"))
```

**Explanation:** `Path.write_text` and `read_text` are concise; context managers are useful for lower-level file handling.

## 2. [Beginner] Append and count lines

**Exercise:** Append a new line to a file and print the number of non-empty lines.

**Answer:**

```python
from pathlib import Path
path = Path("log.txt")
with path.open("a", encoding="utf-8") as file:
    file.write("Analysis completed\n")
with path.open(encoding="utf-8") as file:
    lines = [line for line in file if line.strip()]
print(len(lines))
```

**Explanation:** Mode `a` appends instead of replacing existing content.

## 3. [Intermediate] Parse log lines

**Exercise:** Given a log file with lines beginning with `ERROR` or `INFO`, count each level.

**Answer:**

```python
from collections import Counter
counts = Counter()
with open("app.log", encoding="utf-8") as file:
    for line in file:
        parts = line.split(maxsplit=2)
        if parts:
            counts[parts[0]] += 1
print(counts)
```

**Explanation:** This assumes the log level is the first whitespace-separated token; real log formats may need a proper parser.

## 4. [Intermediate] Copy a file with line numbers

**Exercise:** Read `input.txt` and write each line to `numbered.txt` with a line number prefix.

**Answer:**

```python
with open("input.txt", encoding="utf-8") as source, open("numbered.txt", "w", encoding="utf-8") as target:
    for line_number, line in enumerate(source, start=1):
        target.write(f"{line_number:04d}: {line}")
```

**Explanation:** Iterating over a file streams one line at a time instead of reading the entire file into memory.

## 5. [Advanced] Write a file atomically

**Exercise:** Write new content to a temporary file and replace the destination only after writing succeeds.

**Answer:**

```python
from pathlib import Path
import tempfile

def atomic_write(path, content):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as tmp:
        tmp.write(content)
        temporary_path = Path(tmp.name)
    temporary_path.replace(path)

atomic_write("reports/summary.txt", "Report complete\n")
```

**Explanation:** Creating the temporary file in the same directory usually lets the final rename/replace happen on the same filesystem. Stronger durability guarantees may require fsync.

## 6. [Advanced] Hash a large file in chunks

**Exercise:** Compute a SHA-256 checksum without loading the whole file into memory.

**Answer:**

```python
import hashlib

def sha256_file(path, chunk_size=1024 * 1024):
    digest = hashlib.sha256()
    with open(path, "rb") as file:
        for chunk in iter(lambda: file.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()

print(sha256_file("dataset.csv"))
```

**Explanation:** Chunked reading keeps memory usage bounded for large files.

---

# 17. Try / Except

## 1. [Beginner] Handle invalid integer input

**Exercise:** Convert a string to an integer and print a friendly message if it is invalid.

**Answer:**

```python
text = "42x"
try:
    value = int(text)
except ValueError:
    print("Please provide a whole number")
else:
    print(value)
```

**Explanation:** Catch the specific `ValueError`; `else` runs only when conversion succeeds.

## 2. [Beginner] Handle a missing file

**Exercise:** Read a file and display a message if it does not exist.

**Answer:**

```python
from pathlib import Path
path = Path("missing.txt")
try:
    content = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"File not found: {path}")
else:
    print(content)
```

**Explanation:** Handle expected failures specifically so unrelated bugs are not hidden.

## 3. [Intermediate] Handle malformed JSON

**Exercise:** Try reading JSON from a file and handle both missing files and invalid JSON.

**Answer:**

```python
import json
try:
    with open("config.json", encoding="utf-8") as file:
        config = json.load(file)
except FileNotFoundError:
    print("Configuration file is missing")
except json.JSONDecodeError as error:
    print("Configuration is not valid JSON:", error)
else:
    print(config)
```

**Explanation:** Different exceptions represent different recovery actions: missing file versus malformed content.

## 4. [Intermediate] Use `finally` for cleanup

**Exercise:** Open a file and guarantee a cleanup message is printed whether processing succeeds or fails.

**Answer:**

```python
try:
    with open("data.txt", encoding="utf-8") as file:
        first_line = file.readline()
        print(first_line)
except OSError as error:
    print("File operation failed:", error)
finally:
    print("Processing attempt finished")
```

**Explanation:** `finally` runs whether or not an exception occurs. A `with` statement already closes the file reliably.

## 5. [Advanced] Create and catch a custom exception

**Exercise:** Validate a percentage and raise a custom exception when it is outside 0–100.

**Answer:**

```python
class InvalidPercentageError(ValueError):
    pass

def validate_percentage(value):
    if not isinstance(value, (int, float)) or not 0 <= value <= 100:
        raise InvalidPercentageError("percentage must be a number from 0 to 100")
    return float(value)

try:
    print(validate_percentage(125))
except InvalidPercentageError as error:
    print("Invalid input:", error)
```

**Explanation:** A custom exception communicates a domain-specific validation problem while inheriting useful behavior from `ValueError`.

## 6. [Advanced] Retry only a specific transient failure

**Exercise:** Implement a bounded retry loop for a function that may raise `TimeoutError`; let other exceptions propagate.

**Answer:**

```python
def run_with_retry(operation, attempts=3):
    if attempts < 1:
        raise ValueError("attempts must be at least 1")
    for attempt in range(attempts):
        try:
            return operation()
        except TimeoutError:
            if attempt == attempts - 1:
                raise
    raise RuntimeError("unreachable")

# Example: run_with_retry(fetch_data, attempts=3)
```

**Explanation:** Do not catch broad `Exception` unless you can genuinely handle every possible failure. Production retries may need backoff and idempotency.

---

# 18. Regular Expressions (Regex)

## 1. [Beginner] Find email-like strings

**Exercise:** Find strings that resemble email addresses in a block of text.

**Answer:**

```python
import re
text = "Contact ana@example.com or team.data@sample.org for details."
emails = re.findall(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", text)
print(emails)
```

**Explanation:** This practical pattern finds common email-like strings, but it is not a complete email-address validator.

## 2. [Beginner] Extract dates

**Exercise:** Extract dates formatted as `YYYY-MM-DD`.

**Answer:**

```python
import re
text = "Orders: 2026-01-05, 2026-02-17, and invalid 2026-99-99"
dates = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", text)
print(dates)
```

**Explanation:** The regex checks the shape, not whether a date actually exists; use `datetime.strptime` to validate calendar dates.

## 3. [Intermediate] Validate password rules

**Exercise:** Require at least eight characters, one uppercase, one lowercase, and one digit.

**Answer:**

```python
import re
password = "Data2026"
valid = (
    len(password) >= 8
    and re.search(r"[A-Z]", password)
    and re.search(r"[a-z]", password)
    and re.search(r"\d", password)
)
print(bool(valid))
```

**Explanation:** Multiple simple rules are often easier to explain than one very complicated regular expression.

## 4. [Intermediate] Parse a log line

**Exercise:** Extract timestamp, log level, and message from a line such as `2026-10-26 09:30:00 ERROR Disk full`.

**Answer:**

```python
import re
line = "2026-10-26 09:30:00 ERROR Disk full"
pattern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(INFO|WARNING|ERROR)\s+(.*)$"
match = re.match(pattern, line)
if match:
    timestamp, level, message = match.groups()
    print(timestamp, level, message)
else:
    print("Unrecognized log format")
```

**Explanation:** Capturing groups return the parsed fields; anchoring with `^` and `$` expects the whole line to match.

## 5. [Advanced] Redact phone-number patterns

**Exercise:** Replace phone-number-like sequences with `[REDACTED]` while avoiding changing arbitrary long digit sequences as much as possible.

**Answer:**

```python
import re
text = "Call +1-202-555-0184 or (202) 555-0199; order 123456789012 is unrelated."
pattern = r"(?<!\w)(?:\+?\d{1,3}[ -]?)?(?:\(\d{3}\)|\d{3})[ -]?\d{3}[ -]?\d{4}(?!\w)"
redacted = re.sub(pattern, "[REDACTED]", text)
print(redacted)
```

**Explanation:** Phone formats vary by country. Treat this as a demonstration pattern and test it against your permitted data; regex is not a universal PII detector.

## 6. [Advanced] Extract IDs from URL paths

**Exercise:** Extract numeric IDs from paths such as `/orders/12345/details`, and ignore unrelated paths.

**Answer:**

```python
import re
paths = ["/orders/12345/details", "/users/88", "/orders/7/details", "/orders/abc/details"]
ids = []
for path in paths:
    match = re.fullmatch(r"/orders/(\d+)/details", path)
    if match:
        ids.append(int(match.group(1)))
print(ids)
```

**Explanation:** `fullmatch` ensures the whole path follows the required pattern, and `\d+` captures one or more digits.

---

# 19. sqlite3

## 1. [Beginner] Create a table and insert rows

**Exercise:** Use SQLite to create a table, insert two rows with placeholders, and query all rows.

**Answer:**

```python
import sqlite3
connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL)")
connection.executemany("INSERT INTO products (name, price) VALUES (?, ?)", [("Pen", 1.5), ("Book", 8.0)])
connection.commit()
rows = connection.execute("SELECT id, name, price FROM products ORDER BY id").fetchall()
print(rows)
connection.close()
```

**Explanation:** Use `?` placeholders for values rather than formatting user input into SQL strings.

## 2. [Beginner] Filter rows safely

**Exercise:** Query products that cost more than a supplied threshold using a parameterized query.

**Answer:**

```python
import sqlite3
connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE products (name TEXT, price REAL)")
connection.executemany("INSERT INTO products VALUES (?, ?)", [("Pen", 1.5), ("Book", 8), ("Bag", 25)])
threshold = 5
rows = connection.execute("SELECT name, price FROM products WHERE price > ?", (threshold,)).fetchall()
print(rows)
connection.close()
```

**Explanation:** The second argument to `execute` is a tuple of parameters; the comma makes `(threshold,)` a one-item tuple.

## 3. [Intermediate] Aggregate by category

**Exercise:** Create a sales table and return total revenue per category.

**Answer:**

```python
import sqlite3
connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE sales (category TEXT, revenue REAL)")
connection.executemany("INSERT INTO sales VALUES (?, ?)", [("Tech", 100), ("Office", 40), ("Tech", 75)])
query = "SELECT category, SUM(revenue) AS total_revenue FROM sales GROUP BY category ORDER BY total_revenue DESC"
print(connection.execute(query).fetchall())
connection.close()
```

**Explanation:** `GROUP BY` forms category groups, and `SUM` calculates totals within each group.

## 4. [Intermediate] Join customers to orders

**Exercise:** Create customers and orders tables; list every order with the customer's name.

**Answer:**

```python
import sqlite3
connection = sqlite3.connect(":memory:")
connection.executescript("""
CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER, amount REAL);
""")
connection.executemany("INSERT INTO customers VALUES (?, ?)", [(1, "Ana"), (2, "Ben")])
connection.executemany("INSERT INTO orders VALUES (?, ?, ?)", [(101, 1, 20), (102, 1, 35), (103, 2, 15)])
query = "SELECT o.id, c.name, o.amount FROM orders o JOIN customers c ON c.id = o.customer_id ORDER BY o.id"
print(connection.execute(query).fetchall())
connection.close()
```

**Explanation:** Joining the many-side orders table to the one-side customers table creates one result row per order.

## 5. [Advanced] Use a transaction and rollback

**Exercise:** Insert two records in a transaction and roll everything back if the second record violates a UNIQUE constraint.

**Answer:**

```python
import sqlite3
connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE users (username TEXT UNIQUE)")
try:
    with connection:
        connection.execute("INSERT INTO users VALUES (?)", ("ana",))
        connection.execute("INSERT INTO users VALUES (?)", ("ana",))  # Duplicate triggers IntegrityError.
except sqlite3.IntegrityError:
    print("Transaction rolled back")
print(connection.execute("SELECT * FROM users").fetchall())
connection.close()
```

**Explanation:** The connection context manager commits on success and rolls back when an exception escapes the block.

## 6. [Advanced] Rank products with a window function

**Exercise:** Return each product's revenue and its rank within the category.

**Answer:**

```python
import sqlite3
connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE sales (product TEXT, category TEXT, revenue REAL)")
connection.executemany("INSERT INTO sales VALUES (?, ?, ?)", [("A", "Tech", 100), ("B", "Tech", 160), ("C", "Office", 80), ("D", "Office", 90)])
query = """
SELECT product, category, revenue,
       RANK() OVER (PARTITION BY category ORDER BY revenue DESC) AS category_rank
FROM sales
ORDER BY category, category_rank
"""
print(connection.execute(query).fetchall())
connection.close()
```

**Explanation:** The window function ranks rows within each category without collapsing the individual product rows.

---

# 20. Web Scraping

## 1. [Beginner] Extract headings from sample HTML

**Exercise:** Use Beautiful Soup to extract all heading text from an HTML string. No network request is needed.

**Answer:**

```python
from bs4 import BeautifulSoup
html = "<html><body><h1>Sales Report</h1><h2>Revenue</h2><h2>Profit</h2></body></html>"
soup = BeautifulSoup(html, "html.parser")
headings = [tag.get_text(strip=True) for tag in soup.select("h1, h2, h3")]
print(headings)
```

**Explanation:** A local HTML fixture makes the exercise repeatable without sending requests to a website.

## 2. [Beginner] Extract links and labels

**Exercise:** Extract each anchor's label and `href` from a supplied HTML snippet.

**Answer:**

```python
from bs4 import BeautifulSoup
html = '<a href="/about">About us</a><a href="https://example.com/docs">Docs</a>'
soup = BeautifulSoup(html, "html.parser")
links = [{"text": a.get_text(strip=True), "href": a.get("href")} for a in soup.find_all("a", href=True)]
print(links)
```

**Explanation:** `find_all` finds elements and `get('href')` reads an attribute.

## 3. [Intermediate] Fetch one permitted page

**Exercise:** Fetch a page you own or are authorized to access, use a timeout, identify your client, and extract its title. Install `requests` and `beautifulsoup4` first.

**Answer:**

```python
import requests
from bs4 import BeautifulSoup
url = "https://example.com/"  # Replace with a permitted target when practicing.
response = requests.get(url, headers={"User-Agent": "LearningDataAnalyst/1.0 (educational project)"}, timeout=10)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
title = soup.title.get_text(strip=True) if soup.title else "No title found"
print(title)
```

**Explanation:** Before fetching a site, check its terms, access rules, and robots.txt. Do not bypass authentication, paywalls, CAPTCHAs, or other controls.

## 4. [Intermediate] Check robots.txt before a request

**Exercise:** Use `urllib.robotparser` to check whether a user agent is allowed to fetch one URL according to a site's robots.txt.

**Answer:**

```python
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser
site_url = "https://example.com/some-page"
parsed = urlparse(site_url)
robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
robot = RobotFileParser(robots_url)
robot.read()
user_agent = "LearningDataAnalystBot"
print("Allowed according to robots.txt:", robot.can_fetch(user_agent, site_url))
```

**Explanation:** Robots.txt is a useful access signal but is not a substitute for terms of service or applicable law. Handle network errors separately in real code.

## 5. [Advanced] Scrape a small set of permitted pages politely

**Exercise:** Write a function fetching a short, explicit list of permitted pages, with a timeout, request delay, and a maximum page count.

**Answer:**

```python
import time
import requests
from bs4 import BeautifulSoup

def fetch_titles(urls, max_pages=3, delay_seconds=2):
    if max_pages < 1 or delay_seconds < 0:
        raise ValueError("invalid limits")
    results = []
    headers = {"User-Agent": "LearningDataAnalyst/1.0 (educational project)"}
    for index, url in enumerate(urls[:max_pages]):
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        results.append({"url": url, "title": soup.title.get_text(strip=True) if soup.title else None})
        if index < min(len(urls), max_pages) - 1:
            time.sleep(delay_seconds)
    return results

# Use only URLs whose site policies permit your access.
# print(fetch_titles(["https://example.com/"], max_pages=1))
```

**Explanation:** This is deliberately bounded and waits between requests. Production scraping should also check robots.txt, use caching, handle retries carefully, and stop if access is denied.

## 6. [Advanced] Parse a table and validate extracted fields

**Exercise:** Parse a permitted HTML table with columns `product` and `price`; convert prices to floats and report rows that cannot be parsed.

**Answer:**

```python
from bs4 import BeautifulSoup
html = """<table><tr><th>product</th><th>price</th></tr><tr><td>Pen</td><td>1.50</td></tr><tr><td>Book</td><td>bad</td></tr></table>"""
soup = BeautifulSoup(html, "html.parser")
rows = []
for tr in soup.select("tr")[1:]:
    cells = [td.get_text(strip=True) for td in tr.select("td")]
    if len(cells) != 2:
        continue
    name, raw_price = cells
    try:
        price = float(raw_price)
    except ValueError:
        rows.append({"product": name, "price": None, "error": "invalid price"})
    else:
        rows.append({"product": name, "price": price, "error": None})
print(rows)
```

**Explanation:** Separate parsing from validation, preserve bad records for review, and never silently replace failed values with zero.

---

# 21. Git

## 1. [Beginner] Initialize and commit a project

**Exercise:** Show the basic commands to initialize Git, inspect status, stage files, and make the first commit.

**Answer:**

```bash
git init
git status
git add README.md main.py
git commit -m "Add project starter files"
```

**Explanation:** Run these commands in your project directory. Configure `user.name` and `user.email` if Git requests them.

## 2. [Beginner] Inspect commit history

**Exercise:** Show recent commits in a compact, readable format.

**Answer:**

```bash
git log --oneline --decorate -5
git status
```

**Explanation:** The first command displays a compact history; the second shows uncommitted changes and branch state.

## 3. [Intermediate] Create and switch to a feature branch

**Exercise:** Create a branch for a new analysis feature and switch to it.

**Answer:**

```bash
git switch -c feature/monthly-report
git status
```

**Explanation:** A feature branch isolates work. Commit the changes on that branch before merging it.

## 4. [Intermediate] Unstage a file without deleting changes

**Exercise:** You accidentally staged `data.csv`; remove it from the staging area but keep the working copy.

**Answer:**

```bash
git restore --staged data.csv
git status
```

**Explanation:** `git restore --staged` unstages the file; it does not discard the working-tree edits.

## 5. [Advanced] Resolve and complete a merge conflict

**Exercise:** Describe a safe conflict-resolution workflow after merging a feature branch into the current branch.

**Answer:**

```bash
git status
# Open each conflicted file and edit the conflict markers: <<<<<<<, =======, >>>>>>>
git diff --check
git add path/to/resolved_file.py
git commit -m "Resolve merge conflict"
```

**Explanation:** Inspect each conflict in context, retain the intended code, run tests, then stage and commit the resolution. Do not blindly choose one side.

## 6. [Advanced] Undo a published commit safely

**Exercise:** Create a new commit that reverses a published commit, rather than rewriting shared history.

**Answer:**

```bash
git log --oneline -5
git revert <commit-hash>
git status
```

**Explanation:** `git revert` records a new commit that reverses the selected change and is generally safer for shared branches than resetting published history. Replace the placeholder with a real hash.

---

## Final practice advice

For interview preparation, do not merely memorize the answers. Explain your reasoning, state assumptions, handle edge cases, and write at least one test for each advanced solution. For web scraping, only access pages you are permitted to access and respect site policies.