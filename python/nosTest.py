# -*- coding: utf-8 -*-

import unittest
from gilded_rose import *

class GildedRoseTest(unittest.TestCase):
    #J -12
    def test_12(self):
        items = [
            #Item("nom", sellIn, quality)
            Item("+5 dexterity vest", 10, 20)
            Item("Aged brie", 2, 0)
            Item("Elixir of the mongoose", 5, 7)
            Item("Sulfuras, hand of ragnaros", 0, 80)
            Item("Sulfuras, hand of ragnaros",-1, 80)
            Item("Backstage passes to a tafkal80etc concert", 15, 20)
            Item("Backstage passes to a tafkal80etc concert", 10, 49)
            Item("Backstage passes to a tafkal80etc concert", 5, 49)
            Item("Conjured mana cake", 3, 6)
            Item("une attente d'erreur", 0, 48)
            ]

        #faut faire une boucle pour faire tout les items pour ce jour
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        print("jour", unTrucEncoreObscure)
        self.assertEquals("jeNeSaisPasEncore",items[surementPasCorect].quelqueChose)

If __name__ == '__main__':
    unittest.main()
