import unittest
import calc as c

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = c.add(0,5)
        self.assertEqual(result,5)
        self.assertEqual(c.add(5,5),10)
        self.assertEqual(c.add(-1,2),1)
        self.assertEqual(c.add(-1,-2),-3)

    def test_minus(self):
        result = c.minus(0,5)
        self.assertEqual(result,-5)
        self.assertEqual(c.minus(5,5),0)
        self.assertEqual(c.minus(-1,2),-3)
        self.assertEqual(c.minus(-1,-2),1)

    def test_multiply(self):
        result = c.multiply(0,5)
        self.assertEqual(result,0)
        self.assertEqual(c.multiply(5,5),25)
        self.assertEqual(c.multiply(-1,2),-2)
        self.assertEqual(c.multiply(-1,-2),2)

    def test_divide(self):
        result = c.divide(0,5)
        self.assertEqual(result,0)
        self.assertEqual(c.divide(5,5),1)
        self.assertEqual(c.divide(-1,2),-1/2)
        self.assertEqual(c.divide(-1,-2),1/2)

        #ValueError checks whether demonitor is 0
        # Method 1: self.assertRaises(ValueError, c.divide, 5, 0)
        #Method 2
        with self.assertRaises(ValueError):
            c.divide(5,0)

if __name__ == '__main__':
    unittest.main()
