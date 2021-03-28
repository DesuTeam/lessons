import unittest


def import_matrix(text_file):
    list_of_list = []
    with open(text_file) as martix_table:
        for row in martix_table:
            rows = (row.strip('\n').split(' '))
            num = map(lambda x: int(x), rows)
            list_of_list.append(list(num))
    return list_of_list

def find_value(matrix, value):
    result = []
    for x in range(0,10):
        for y in range(0,10):
            if matrix[x][y] == value:
                result.append((x,y))
    return result

def convert_to_lines(indexes):
    lines = map(lambda t: t[0], indexes)
    return list(set(lines))

def convert_to_columns(indexes):
    lines = map(lambda t: t[1], indexes)
    return list(set(lines))


def run():
    value = 41
    matrix = import_matrix('Matrix')
    indexes = (find_value(matrix,value))

    print('Rows', convert_to_lines(indexes))
    print('Index', convert_to_columns(indexes))

class HomeWork12Test(unittest.TestCase):
    def test_find_value (self):
        self.assertEqual([], find_value(
            [
                [0, 0, 0, 0,  0, 0,  0, 0,  0, 0],
                [0, 0, 0, 0,  0, 0,  0, 0,  0, 0],
                [0, 0, 0, 0,  0, 0,  0, 0,  0, 0],
                [0, 0, 0, 0,  0, 0,  0, 0,  0, 0],
                [0, 0, 0, 0,  0, 0,  0, 0,  0, 0],
                [0, 0, 0, 0,  0, 0,  0, 0,  0, 0],
                [0, 0, 0, 0,  0, 0,  0, 0,  0, 0],
                [0, 0, 0, 0,  0, 0,  0, 0,  0, 0],
                [0, 0, 0, 0,  0, 0,  0, 0,  0, 0],
                [0, 0, 0, 0,  0, 0,  0, 0,  0, 0],
                [0, 0, 0, 0,  0, 0,  0, 0,  0, 0],
                [0, 0, 0, 0,  0, 0,  0, 0,  0, 0],
            ] , 1
        )),

    def test_find_value_another(self):
        self.assertEqual([(1,1)], find_value(
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ], 2
        )),

    def test_convert_lines(self):
        self.assertEqual([], convert_to_lines([]))

    def test_convert_lines(self):
        self.assertEqual([5], convert_to_lines([(5,10)]))