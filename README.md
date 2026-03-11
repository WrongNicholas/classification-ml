# Part 1

# What we're seeing

Because the dataset is imbalanced, we're seeing the smaller classes (SECURITY, ENERGY) having very few samples. This reduces the classifier performance on these labels.

Running `make run` with part1.py as `MAIN`:
```sh
❯ make run
venv/bin/pip install --upgrade pip
Requirement already satisfied: pip in ./venv/lib/python3.14/site-packages (26
.0.1)
venv/bin/python main.py
category
BUG            503
FEATURE        163
PERFORMANCE     34
USABILITY       16
SECURITY         5
ENERGY           4
Name: count, dtype: int64
Accuracy: 0.8275862068965517
Precision: 0.8235041938490214
Recall: 0.8275862068965517
F1 Score: 0.8081278989233321

Confusion Matrix:
[[95  0  6  0  0  0]
 [ 0  1  0  0  0  0]
 [ 9  0 22  0  0  1]
 [ 5  0  1  1  0  0]
 [ 1  0  0  0  0  0]
 [ 1  0  1  0  0  1]]

```
