import unittest
import convertor
# Assuming the functions digit_to_hex, decimal_to_hex, convert_list_to_hex, and convertor.process_and_convert 
# are already defined as provided in the original code

class TestHexConversion(unittest.TestCase):
    
    def test_convertor(self):
        # Test case 1
        self.assertEqual(convertor.process_and_convert([784, 816, 848, 880]), ['310', '330', '350', '370'])

        # Test case 2
        self.assertEqual(convertor.process_and_convert([4000, 8000, 12000, 16000]), ['FA0', '1F40', '2EE0', '3E80'])

        # Test case 3
        self.assertEqual(convertor.process_and_convert([544, 1248, 4096, 6240]), ['220', '4E0', '1000', '1860'])

        # Test case 4
        self.assertEqual(convertor.process_and_convert([3, 5, 7, 9]), ['3', '5', '7', '9'])

        # Test case 5
        self.assertEqual(convertor.process_and_convert([10, 5, 8, 3]), ['A', '5', '8', '3'])

        # Test case 6
        self.assertEqual(convertor.process_and_convert([10, 17, 3, 6]), ['A', '11', '3', '6'])

        # Test case 7
        self.assertEqual(convertor.process_and_convert([12, 5, 8, 11]), ['C', '5', '8', 'B'])

        # Test case 8
        self.assertEqual(convertor.process_and_convert([9, 16, 13, 6]), ['9', '10', 'D', '6'])

        # Test case 9
        self.assertEqual(convertor.process_and_convert([11, 3, 15, 10]), ['B', '3', 'F', 'A'])

        # Test case 10
        self.assertEqual(convertor.process_and_convert([3, 5, 6, 8]), ['3', '5', '6', '8'])

        # Test case 11
        self.assertEqual(convertor.process_and_convert([6, 8, 10, 11]), ['6', '8', 'A', 'B'])

        # Test case 12
        self.assertEqual(convertor.process_and_convert([5, 8, 13, 16]), ['5', '8', 'D', '10'])

        # Test case 13
        self.assertEqual(convertor.process_and_convert([6, 10, 13, 16]), ['6', 'A', 'D', '10'])

        # Test case 14
        self.assertEqual(convertor.process_and_convert([256, 480, 512, 768]), ['100', '1E0', '200', '300'])

        # Test case 15
        self.assertEqual(convertor.process_and_convert([912, 944, 976, 1008]), ['390', '3B0', '3D0', '3F0'])

        # Test case 16
        self.assertEqual(convertor.process_and_convert([272, 304, 336, 368]), ['110', '130', '150', '170'])

        # Test case 17
        self.assertEqual(convertor.process_and_convert([112, 144, 16, 48]), ['70', '90', '10', '30'])

        # Test case 18
        self.assertEqual(convertor.process_and_convert([112, 128, 144, 160]), ['70', '80', '90', 'A0'])

        # Test case 19
        self.assertEqual(convertor.process_and_convert([16, 32, 48, 64]), ['10', '20', '30', '40'])

        # Test case 20
        self.assertEqual(convertor.process_and_convert([720, 1072, 1424, 368]), ['2D0', '430', '590', '170'])

        # Test case 21
        self.assertEqual(convertor.process_and_convert([192, 384, 576, 768]), ['C0', '180', '240', '300'])

        # Test case 22
        self.assertEqual(convertor.process_and_convert([1616, 3232, 4848, 6464]), ['650', 'CA0', '12F0', '1940'])

        # Test case 23
        self.assertEqual(convertor.process_and_convert([48, 96, 144, 192]), ['30', '60', '90', 'C0'])

        # Test case 24
        self.assertEqual(convertor.process_and_convert([13, 2, 16, 8]), ['D', '2', '10', '8'])

        # Test case 25
        self.assertEqual(convertor.process_and_convert([11, 4, 15, 6]), ['B', '4', 'F', '6'])

        # Test case 26
        self.assertEqual(convertor.process_and_convert([17, 7, 12, 2]), ['11', '7', 'C', '2'])

if __name__ == "__main__":
    unittest.main()
