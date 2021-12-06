# How to flatten a nested list
```python
def flatten(outer_list):
    return [x for inner_list in outer_list for x in inner_list]


xs = [["a", "b"], ["c"], ["d", "e"]]
print(flatten(xs))  # ['a', 'b', 'c', 'd', 'e']
```

# How to combine two lists
```python
def combine(xs, ys):
    return [x + y for x in xs for y in ys]


xs = ["a", "b", "c"]
ys = ["x", "y", "z"]
print(combine(xs, ys))  # ['ax', 'bx', 'cx', 'ay', 'by', 'cy', 'az', 'bz', 'cz']
```

# File
## How to get the absolute path of a file in the script directory.
```python
def get_absolute_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)
```

## How to open a file and print each line
```python
def open_file():
    with open("input.txt") as file:
        while line := file.readline().strip():
            print(line)
```

## How to open a file and join all the lines to a string
```python
def open_file():
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]
        return " ".join(lines)
```
