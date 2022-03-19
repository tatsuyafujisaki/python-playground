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
