import unittest
from gilded_rose import *

class GildedRoseTest(unittest.TestCase):
    def test_(self):
        items = [
            #Item("nom", sellIn, quality)
            Item("+5 dexterity vest", 10, 20),
            Item("Aged brie", 2, 0),
            Item("Elixir of the mongoose", 5, 7),
            Item("Sulfuras, hand of ragnaros", 0, 80),
            Item("Sulfuras, hand of ragnaros",-1, 80),
            Item("Backstage passes to a tafkal80etc concert", 15, 20),
            Item("Backstage passes to a tafkal80etc concert", 10, 49),
            Item("Backstage passes to a tafkal80etc concert", 5, 49),
            #Item("Conjured mana cake", 3, 6),
            Item("yusk2", 0, -8),
            Item("yusk3", 0, 48)
            ]
        jours = [-30, -1, 0, 1, 5, 10, 15]
        for j in jours:
            gilded_rose = GildedRose(items)
            gilded_rose.update_quality()
            print ()
            print ("jour =", j)
            for obj in range(len(items)):
                print ("object", items[obj].name, "vaut", items[obj].quality, "périme dans", items[obj].sell_in)

if __name__ == "__main__":
    unittest.main()

