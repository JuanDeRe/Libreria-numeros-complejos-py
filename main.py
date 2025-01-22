import cplx as lc
import unittest

test1a = (2, 3)
test1b = (5, -1)
test2a = (0, 10)
test2b = (1.5, -7)
class TestCplxOperations(unittest.TestCase):
    def testSuma(self):
        result = lc.sumacplx(test1a, test1b)
        self.assertAlmostEqual(result[0], 7)
        self.assertAlmostEqual(result[1], 2)

        result = lc.sumacplx(test2a, test2b)
        self.assertAlmostEqual(result[0], 1.5)
        self.assertAlmostEqual(result[1], 3)

    def testResta(self):
        result = lc.restacplx(test1a, test1b)
        self.assertAlmostEqual(result[0], -3)
        self.assertAlmostEqual(result[1], 4)

        result = lc.restacplx(test2a, test2b)
        self.assertAlmostEqual(result[0], -1.5)
        self.assertAlmostEqual(result[1], 17)

    def testMultp(self):
        result = lc.multpcplx(test1a, test1b)
        self.assertAlmostEqual(result[0], 13)
        self.assertAlmostEqual(result[1], 13)

        result = lc.multpcplx(test2a, test2b)
        self.assertAlmostEqual(result[0], 70)
        self.assertAlmostEqual(result[1], 15)

    def testDiv(self):
        result = lc.divcplx(test1a, test1b)
        self.assertAlmostEqual(result[0], 0.46153, 4)
        self.assertAlmostEqual(result[1], 0.65384, 4)

        result = lc.divcplx(test2a, test2b)
        self.assertAlmostEqual(result[0], 0.05853, 4)
        self.assertAlmostEqual(result[1], 0.29268, 4)

    def testMod(self):
        self.assertAlmostEqual(lc.modcplx(test1a), 3.60555, 5)
        self.assertAlmostEqual(lc.modcplx(test2b), 7.15891, 5)

    def testConjg(self):
        result = lc.conjcplx(test1a)
        self.assertAlmostEqual(result[0], 2)
        self.assertAlmostEqual(result[1], -3)

        result = lc.conjcplx(test2b)
        self.assertAlmostEqual(result[0], 1.5)
        self.assertAlmostEqual(result[1], 7)

    def testPolarcart(self):
        result = lc.polar_cartcplx(1, 0.5)
        self.assertAlmostEqual(result[0], 0.877582, 5)
        self.assertAlmostEqual(result[1], 0.479425, 5)

        result = lc.polar_cartcplx(0.5, 1)
        self.assertAlmostEqual(result[0], 0.270151, 5)
        self.assertAlmostEqual(result[1], 0.420735, 5)

    def testCartpolar(self):
        result = lc.cart_polarcplx(test1a)
        self.assertAlmostEqual(result[0], 3.605551, 5)
        self.assertAlmostEqual(result[1], 0.982793, 5)

        result = lc.cart_polarcplx(test2b)
        self.assertAlmostEqual(result[0], 7.158910, 5)
        self.assertAlmostEqual(result[1], -1.359702, 5)

    def testFase(self):
        self.assertAlmostEqual(lc.fasecplx(test1a), 0.982793, 5)
        self.assertAlmostEqual(lc.fasecplx(test2b), -1.359702, 5)

if __name__ == "__main__":
    unittest.main()
