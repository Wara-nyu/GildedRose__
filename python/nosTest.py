# -*- coding: utf-8 -*-
#python3

import unittest
from gilded_rose import *
from items import *

class GildedRoseTest(unittest.TestCase):
    def test_0(self):
        jour = 0
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        for obj in range(len(items)):
            print("jour = " + jour)
            print(items)
        #self.assertEquals("jeNeSaisPasEncore",items[surementPasCorect].quelqueChose)

if __name__ == '__main__':
    unittest.main()
