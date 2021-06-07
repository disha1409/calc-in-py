import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_div(self):
        self.assertEqual(calc.div(6, 3),2)
        self.assertEqual(calc.div(8,2),4)
        self.assertEqual(calc.div(9,3),3)
        
    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-1,1),0)
        self.assertEqual(calc.add(-1,-1),-2)
    def test_subtract(self):
        self.assertEqual(calc.sub(10,5),5)
        self.assertEqual(calc.sub(-1,1),-2)
        self.assertEqual(calc.sub(-1,-1),0)
    def test_product(self):
        self.assertEqual(calc.product(10,5),50)
        self.assertEqual(calc.product(-1,1),-1)
        self.assertEqual(calc.product(-1,-1),1)
	
 	 

if __name__ == '__main__':
	unittest.main()
		


