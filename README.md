PySorting
===========
A repository of common sorting algorithms done in Python.  
It's useful to actually implement the algoritms yourself as a refresher... who really remembers the Big-O complexity off the top of their head?

## Requirements
* Python3 (`brew install python3` on OSX)

## Get Going
```bash
git clone git@github.com:adveres/PySorting.git
cd PySorting
pip install -r requirements.txt --upgrade
```

## Usage

`python sorting.py --help`

Example run...
```
python3 sorting.py
Task: [14, 33, 27, 10, 35, 19, 42, 44]
+----------------+-------+------------+----------------+
| Algorithm      | Pass? | Iterations |      Time      |
+----------------+-------+------------+----------------+
| bubble_sort    |  True |    32      | 0:00:00.000020 |
| insertion_sort |  True |    14      | 0:00:00.000006 |
| merge_sort     |  True |    32      | 0:00:00.000044 |
| selection_sort |  True |    35      | 0:00:00.000010 |
+----------------+-------+------------+----------------+

Task: [0, 56, 73, 12, 5, 99, 19, 65, 27, 30, 2, 66]
+----------------+-------+------------+----------------+
| Algorithm      | Pass? | Iterations |      Time      |
+----------------+-------+------------+----------------+
| bubble_sort    |  True |    120     | 0:00:00.000028 |
| insertion_sort |  True |    40      | 0:00:00.000011 |
| merge_sort     |  True |    56      | 0:00:00.000036 |
| selection_sort |  True |    77      | 0:00:00.000025 |
+----------------+-------+------------+----------------+
...
```
