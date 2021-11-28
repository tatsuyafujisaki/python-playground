# How to flatten a nested list
```python
def flatten(outer_list):
    return [x for inner_list in outer_list for x in inner_list]


xs = [["a", "b"], ["c"], ["d", "e"]]
print(flatten(xs))  # ['a', 'b', 'c', 'd', 'e']
```

# How to open a file and print each line
```python
def open_file():
    with open("input.txt") as file:
        while line := file.readline().strip():
            print(line)
```

# How to open a file and join all the lines to a string
```python
def open_file():
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]
        return " ".join(lines)
```
