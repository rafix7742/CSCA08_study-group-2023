"""CSCA08 Student-led study group (Dec 18th) cumulative project function tester

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.
"""

import unittest
from copy import deepcopy

from housing_sol import find_next_bid, find_largest_room, \
    get_average_room_size, add_room, change_address

from constants import NEXT_BID

EXAMPLE_DATA = [
    {'id': 0, 'address': '764 SANTIAGO AVE', 'postal_code': 'M9C 9G8',
     'location': {'latitude': '33.78223', 'longitude': '-118.14917',
                  'city': 'London'},
     'rooms': {
         'bedroom': [(46.97, 93.01), (73.09, 29.68)],
         'kitchen': [(41.04, 32.48)]},
     'bidding': None
     },
    {'id': 1, 'address': '3114 S CONGRESS AVE UNIT 210',
     'postal_code': 'I4S 8U2',
     'location': {'latitude': '30.24298', 'longitude': '-97.76537',
                  'city': 'Edmonton'},
     'rooms': {'bathroom': [(67.39, 19.34)], 'bedroom': [(10.84, 1.9)],
               'kitchen': [(17.03, 47.03)]},
     'bidding': [101231]
     },
    {'id': 2, 'address': '20141 PARTHENIA ST', 'postal_code': 'N1P 4B4',
     'location': {'latitude': '34.20926', 'longitude': '-118.5755',
                  'city': 'Burnaby'},
     'rooms': {'basement': [(61.58, 92.71), (97.14, 28.49)]},
     'bidding': [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000]
     }
]


class HousingTestCases(unittest.TestCase):
    def test_find_next_bid_01(self):
        """Change of input"""
        description = "the function is changing the input"

        testcase = deepcopy(EXAMPLE_DATA)
        find_next_bid(testcase, 2)
        expected = EXAMPLE_DATA
        actual = testcase
        self.assertEqual(expected, actual, description)

    def test_find_next_bid_02(self):
        """0 bids"""
        description = "the function is not working for 0 bids"

        testcase = deepcopy(EXAMPLE_DATA)
        expected = 0
        actual = find_next_bid(testcase, 0)

        self.assertEqual(expected, actual, description)

    def test_find_next_bid_03(self):
        """1 bid"""
        description = "the function is not working for 1 bid"

        testcase = deepcopy(EXAMPLE_DATA)
        expected = EXAMPLE_DATA[1]['bidding'][0] + NEXT_BID
        actual = find_next_bid(testcase, 1)

        self.assertEqual(expected, actual, description)

    def test_find_next_bid_04(self):
        """many bids"""
        description = "the function is not working for many bids"

        testcase = deepcopy(EXAMPLE_DATA)
        expected = EXAMPLE_DATA[2]['bidding'][-1] + NEXT_BID
        actual = find_next_bid(testcase, 2)

        self.assertEqual(expected, actual, description)

    def test_find_next_bid_05(self):
        """same bids"""
        description = "the function is not working for same bids"

        testcase = deepcopy(EXAMPLE_DATA)
        testcase[1]['bidding'].append(EXAMPLE_DATA[1]['bidding'][0])

        expected = EXAMPLE_DATA[1]['bidding'][0] + NEXT_BID
        actual = find_next_bid(testcase, 1)

        self.assertEqual(expected, actual, description)

    def test_find_next_bid_06(self):
        """no house with idx"""
        description = "the function is not working for no house with idx"

        testcase = deepcopy(EXAMPLE_DATA)
        expected = 0
        actual = find_next_bid(testcase, 10)

        self.assertEqual(expected, actual, description)

    def test_find_largest_room_01(self):
        """Change of input"""
        description = "the function is changing the input"

        testcase = deepcopy(EXAMPLE_DATA)
        find_largest_room(testcase, 2)
        expected = EXAMPLE_DATA
        actual = testcase
        self.assertEqual(expected, actual, description)

    def test_find_largest_room_02(self):
        """1 room"""
        description = "the function is not working for 1 room"

        testcase = deepcopy(EXAMPLE_DATA)
        expected = 'basement'
        actual = find_largest_room(testcase, 2)

        self.assertEqual(expected, actual, description)

    def test_find_largest_room_03(self):
        """many rooms"""
        description = "the function is not working for many rooms"

        testcase = deepcopy(EXAMPLE_DATA)
        expected = 'bathroom'
        actual = find_largest_room(testcase, 1)

        self.assertEqual(expected, actual, description)

    def test_find_largest_room_04(self):
        """same sqrf"""
        description = "the function is not working for same sqrf"

        testcase = deepcopy(EXAMPLE_DATA)
        testcase[1]['rooms']['bedroom'].append((67.39, 19.34))
        expected_1 = 'bedroom'
        expected_2 = 'bathroom'

        actual = find_largest_room(testcase, 1)
        if actual == expected_1:
            self.assertEqual(expected_1, actual, description)
        else:
            self.assertEqual(expected_2, actual, description)

    def test_find_largest_room_05(self):
        """no house with idx"""
        description = "the function is not working for no house with idx"

        testcase = deepcopy(EXAMPLE_DATA)
        expected = ''
        actual = find_largest_room(testcase, 10)

        self.assertEqual(expected, actual, description)

    def test_get_average_room_size_01(self):
        """Change of input"""
        description = "the function is changing the input"

        testcase = deepcopy(EXAMPLE_DATA)
        get_average_room_size(testcase, 2)
        expected = EXAMPLE_DATA
        actual = testcase
        self.assertEqual(expected, actual, description)

    def test_get_average_room_size_02(self):
        """1 room"""
        description = "the function is not working for 1 room"

        testcase = deepcopy(EXAMPLE_DATA)
        testcase[2]['rooms']['basement'].pop()
        expected = 5709.081799999999
        actual = get_average_room_size(testcase, 2)

        self.assertEqual(expected, actual, description)

    def test_get_average_room_size_03(self):
        """many rooms"""
        description = "the function is not working for many rooms"

        testcase = deepcopy(EXAMPLE_DATA)
        expected = 708.2798333333334
        actual = get_average_room_size(testcase, 1)

        self.assertEqual(expected, actual, description)

    def test_get_average_room_size_04(self):
        """same type, different size"""
        description = ("the function is not working for same type, different "
                       "size")

        testcase = deepcopy(EXAMPLE_DATA)
        expected = 4238.3002
        actual = get_average_room_size(testcase, 2)

        self.assertEqual(expected, actual, description)

    def test_get_average_room_size_05(self):
        """no house with idx"""
        description = "the function is not working for no house with idx"

        testcase = deepcopy(EXAMPLE_DATA)
        expected = 0.0
        actual = get_average_room_size(testcase, 10)

        self.assertEqual(expected, actual, description)

    def test_add_room_01(self):
        """already existing type"""
        description = ("the function is not working for already existing type "
                       "of room")

        testcase = deepcopy(EXAMPLE_DATA)
        add_room(testcase, 2, 'basement', 100.0, 100.0)
        expected = [(61.58, 92.71), (97.14, 28.49), (100, 100)]
        actual = testcase[2]['rooms']['basement']

        self.assertEqual(expected, actual, description)

    def test_add_room_02(self):
        """new type"""
        description = "the function is not working for new type of room"

        testcase = deepcopy(EXAMPLE_DATA)
        add_room(testcase, 2, 'living room', 100.0, 100.0)
        expected = [(100, 100)]
        actual = testcase[2]['rooms']['living room']

        self.assertEqual(expected, actual, description)

    def test_change_address_01(self):
        """change address"""
        description = "the function is not working for changing address"

        testcase = deepcopy(EXAMPLE_DATA)
        change_address(testcase, 2, '12 new address', 'M1M N2N', 0)
        expected = deepcopy(EXAMPLE_DATA)
        expected[2]['address'] = '12 new address'
        actual = testcase

        self.assertEqual(expected, actual, description)

    def test_change_address_02(self):
        """change postal code"""
        description = "the function is not working for changing postal code"

        testcase = deepcopy(EXAMPLE_DATA)
        change_address(testcase, 2, '12 new address', 'M1M N2N', 1)
        expected = deepcopy(EXAMPLE_DATA)
        expected[2]['postal_code'] = 'M1M N2N'
        actual = testcase

        self.assertEqual(expected, actual, description)

    def test_change_address_03(self):
        """change both"""
        description = "the function is not working for changing both"

        testcase = deepcopy(EXAMPLE_DATA)
        change_address(testcase, 2, '12 new address', 'M1M N2N', 2)
        expected = deepcopy(EXAMPLE_DATA)
        expected[2]['address'] = '12 new address'
        expected[2]['postal_code'] = 'M1M N2N'
        actual = testcase

        self.assertEqual(expected, actual, description)

    def test_change_address_04(self):
        """no house with idx"""
        description = "the function is not working for no house with idx"

        testcase = deepcopy(EXAMPLE_DATA)
        change_address(testcase, 10, '12 new address', 'M1M N2N', 2)
        expected = deepcopy(EXAMPLE_DATA)
        actual = testcase

        self.assertEqual(expected, actual, description)


if __name__ == '__main__':
    unittest.main()
