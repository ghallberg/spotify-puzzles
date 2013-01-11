import unittest
import bestbefore
import datetime

class KnownDates(unittest.TestCase):
    knownValues = ( ("31/1/2012", "2012-01-31"),
            ("02/4/67", "2067-02-04"),
            ("31/9/73", "31/9/73 is illegal")
            )

    def testKnownValues(self):
        for input, output in self.knownValues:
            result = bestbefore.first_possible_date(input)
            self.assertEqual(result,output)

class ParseNumbers(unittest.TestCase):
    knownNumbers = (("1/2/3", (1,2,3)),
            ("2098/5/123", (2098,5,123)),
            ("05/2/07", (5,2,7))
            )
    def testKnownNumbers(self):
        for input, output in self.knownNumbers:
            result = bestbefore.parse_numbers(input)
            self.assertEqual(result,output)

class Make2Year(unittest.TestCase):
    knownYears = ( (1, 2001),
            (2000, 2000),
            (999, 2999),
            (57, 2057)
            )

    badYears = (1000, 3000, 1536, 15034, -2)

    def testKnownYears(self):
        for input, output in self.knownYears:
            result = bestbefore.make_2k_year(input)
            self.assertEqual(result,output)

    def testBadYears(self):
        for input in self.badYears:
            self.assertRaises(ValueError, bestbefore.make_2k_year, input)

class ActualDate(unittest.TestCase):
    knownDates = (
            ((2012, 1, 4), datetime.date(2012, 1, 4)),
            ((102, 1, 4), datetime.date(2102, 1, 4)),
            ((12, 1, 4), datetime.date(2012, 1, 4)),
            ((2012, 2, 29), datetime.date(2012, 2, 29)),
            ((2000, 2, 29), datetime.date(2000, 2, 29)),
            ((1012, 1, 4), None),
            ((2100, 2, 29), None),
            ((2112, -1, 31), None),
            ((2112, 1, -1), None),
            ((2112, 1, 32), None),
            ((2112, 13, 31), None),
            )

    def testKnownDates(self):
        for input, output in self.knownDates:
            result = bestbefore.actual_date(*input)
            self.assertEqual(result,output)
