import unittest
from info_sci_special.csv_printer import CSVPrinter


# def setUpModule():
#     print('Running setUpModule')


# def tearDownModule():
#     print('Running tearDownModule')


# class TestCSVPrinter(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         print('Running setUpClass')

#     @classmethod
#     def tearDownClass(cls):
#         print('Running tearDownClass')

#     def setUp(cls):
#         print('Running setUp')

#     def tearDown(cls):
#         print('Running tearDown')

#     def test_one(self):
#         printer = CSVPrinter('sample.csv')
#         l = printer.read()
#         self.assertEqual(len(l), 3)

#     def test_two(self):
#         printer = CSVPrinter('sample.csv')
#         l = printer.read()
#         self.assertGreater(len(l[0]), 1)

#     def test_three(self):
#         with self.assertRaises(FileNotFoundError):
#             printer = CSVPrinter('not_existing_file.csv')
#             l = printer.read()


class TestCSVPrinter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        printer = CSVPrinter('sample.csv')
        cls.l = printer.read()

    @classmethod
    def tearDownClass(cls):
        del cls.l

    def test_one(self):
        self.assertEqual(len(self.l), 3)

    def test_two(self):
        self.assertGreater(len(self.l[0]), 1)

    def test_three(self):
        with self.assertRaises(FileNotFoundError):
            printer_2 = CSVPrinter('not_existing_file.csv')
            printer_2.read()
