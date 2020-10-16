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
```bash
python sorting.py

[14, 33, 27, 10, 35, 19, 42, 44]
    bubble_sort    sorted in 32  iterations and took: 0:00:00.000019
    insertion_sort sorted in 14  iterations and took: 0:00:00.000008
    merge_sort     sorted in 32  iterations and took: 0:00:00.000033
    selection_sort sorted in 35  iterations and took: 0:00:00.000011

[0, 56, 73, 12, 5, 99, 19, 65, 27, 30, 2, 66]
    bubble_sort    sorted in 120 iterations and took: 0:00:00.000025
    insertion_sort sorted in 40  iterations and took: 0:00:00.000012
    merge_sort     sorted in 56  iterations and took: 0:00:00.000031
    selection_sort sorted in 77  iterations and took: 0:00:00.000020
...
```
