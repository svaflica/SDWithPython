FOLDER_TO_TEST = 'solution'

import pytest
import os
import sys
import pandas as pd

sys.path.insert(1, FOLDER_TO_TEST)

NEED_FILES = ['Circle.py', 'Ellipse.py', 'Figure.py', 'Quadrilateral.py', 'Rectangle.py', 'Square.py']
RESULTS = [
    ['circle', 314.1593, 62.8319, [[0.0, 0.0], 10.0]],
    ['circle', 3.1416, 6.2832, [[12.0, 0.0], 1.0]],
    ['ellipse', 94.2478, 43.8591, [[6.0, 6.0], 10.0, 3.0]],
    ['square', 49.0000, 28.0000, [[6.0, 14.0], 7.0]],
    ['rectangle', 8.0000, 12.0000, [[12.0, 12.0], [14.0, 16.0]]],
    ['quadrilateral', 4.0000, 14.9738, [[0.0, 0.0], [1.0, 1.0], [4.0, 6.0], [3.0, 2.0]]],
    ['square', 20.2500, 18.0000, [[9.0, 17.0], 4.5]],
    ['rectangle', 74.7500, 36.0000, [[0.5, 0.5], [7.0, 12.0]]],
    ['quadrilateral', 4.0000, 14.9738, [[1.0, 1.0], [2.0, 2.0], [5.0, 7.0], [4.0, 3.0]]]
]


def test_check_files():
    files = os.listdir(FOLDER_TO_TEST)
    for need_file in NEED_FILES:
        assert need_file in files

        
def test_check_import():
    imported_classes = {}
    for need_file in NEED_FILES:
        name = need_file.split('.')[0]
        imported_classes[name] = __import__(name)
        

def test_check_min_functionality():
    imported_classes = {}
    for need_file in NEED_FILES:
        name = need_file.split('.')[0]
        imported_classes[name.lower()] = __import__(name)

    df = pd.read_csv('Figure_data.csv', sep=';', header=None)
    for ind in range(df.shape[0]):
        class_name = df.iloc[ind][0]
        figure = getattr(imported_classes[class_name], class_name.capitalize()).constructFromSeries(df.iloc[ind])
        str(figure)
        assert figure.__name__.lower() == RESULTS[ind][0]
        assert round(figure.square, 2) == round(RESULTS[ind][1], 2)
        assert round(figure.perimeter, 2) == round(RESULTS[ind][2], 2)
        assert [list(p) if not isinstance(p, float) else p for p in figure.points] == RESULTS[ind][3]
