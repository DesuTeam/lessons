import unittest


a1 = -2
a2 = 2
b1 = -3
b2 =  1
c1 =  0
c2 =  4

def square_roots(a, b, c):
    if a == 0:
        if b == 0:
            return ()
        return (-c / b, )
#   ax2 + bx + c = 0
    D = (b * b) - 4 * a * c
    if D < 0:
        return ()
    elif D == 0:
        return ( -b / 2 * a, )
    else:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return (x1, x2)

def run():
    for a in range(a1, a2):
        for b in range(b1, b2):
            for c in range(c1, c2):
                result = square_roots(a, b, c)
                if result == ():
                    continue
                print(a, b, c, 'Yes ', end='')
                for root in list(result):
                    print('{:.2}'.format(root), ' ', end='')
                print('')

class HomeWork1Test (unittest.TestCase):
    def test_roots_of_x_square(self):
        self.assertEqual((0,), square_roots(1, 0, 0))

    def  test_two_roots(self):
        self.assertEqual((3, -3,), square_roots(1,0,-9))

    def test_return_first(self):
        self.assertEqual((5,), square_roots(0,2,-10))



if __name__ == '__main__':
    unittest.main()




