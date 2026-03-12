See code on https://github.com/WrongNicholas/classification-ml/

# Part 1

## Output

Run `make run1`:
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

Run `make run2`:
```sh
❯ make run2
venv/bin/pip install --upgrade pip
Requirement already satisfied: pip in ./venv/lib/python3.14/site-packages (26
.0.1)
venv/bin/python part2.py
category
BUG        503
FEATURE    163
Name: count, dtype: int64

====================================
SAVED TO classified.xlsx:
====================================
                                              review predicted_category
0  Zoom works well during class tutorials. Until ...                BUG
1                                     Great service.                BUG
2  Easy to use for the most part. There should be...            FEATURE
3                                          Great app                BUG
4               wow good application to meet friends                BUG
```
### Well classified examples
from `classified1.xlsx`

Line 14:
```
BUG: My meeting is not working 😭
```

Line 9:
```
BUG: Can't lower volume completely when using the external speaker. Please fix this ongoing issue.
```

Line 18:
```
FEATURE: Why this app has no feature to control video quality in case we have less data balance?
```

Line 142:
```
FEATURE: OHH a really wonderful app! can we have stickers in chat please?
```

### Poorly classified examples
from `classified1.xlsx`

Line 120:
```
FEATURE: can't change background
```

Line 3:
```
BUG: Great service.
```

Line 5:
```
BUG: Great app
```

Line 23:
```
BUG: very good the zoom app I had help with setting up zoom the girls in the office helped me
```

Some reviews contain general positive reviews and are classified as bug reports or feature requests. 
