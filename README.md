# Part 1

## Output

Running `make run` with `part1.py` as `MAIN`:
```sh
❯ make run
venv/bin/pip install --upgrade pip
Requirement already satisfied: pip in ./venv/lib/python3.14/site-packages (26
.0.1)
venv/bin/python main.py
category
BUG        503
FEATURE    163
Name: count, dtype: int64

====================================
DECISION_TREE
====================================
Accuracy: 0.8582089552238806
Precision: 0.8527645861601085
Recall: 0.8582089552238806
F1 Score: 0.8500389050010609

Confusion Matrix:
[[96  5]
 [14 19]]

====================================
RANDOM_FOREST
====================================
Accuracy: 0.8283582089552238
Precision: 0.8601949927780452
Recall: 0.8283582089552238
F1 Score: 0.791226811678044

Confusion Matrix:
[[101   0]
 [ 23  10]]

====================================
SVM
====================================
Accuracy: 0.8805970149253731
Precision: 0.8969256282689119
Recall: 0.8805970149253731
F1 Score: 0.8658742982336026

Confusion Matrix:
[[101   0]
 [ 16  17]]
```
# Part 2

##
