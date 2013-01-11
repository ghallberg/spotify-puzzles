import unittest
import reversebinary

class KnownReverses(unittest.TestCase):
    knownValues = ((13,11),(47,61),(1,1),(0,0))

    def testKnownReverses(self):
        for input, output in self.knownValues:
            result = reversebinary.reverse(input)
            self.assertEqual(result,output)

