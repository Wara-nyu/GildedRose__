* sellIn : nombre de jours restant pour vendre l'article
* quality : combien l'article est précieux
* diminution de ces deux valeur chaque fin de journée

* quand la date de péremption est passée, la qualité se dégrade deux plus rapidement
* la "quality" ne peux pas être négative
* "Aged Brie" augmente sa "quality" plus le temps passe
* "quality" n'est jamais au dessus de 50
* "Sufuras", pas de date de péremption et "quality" ne change pas
* "Backstage passes" augment en "quality" plus le temps passe (sellIn); la "quality" augment de 2 quand il reste 10 jours ou moin et de 3 quand il reste 5 jours ou moins, mais la "qualité" tombe à 0 après le concert.

- "+5 dexterity vest"                           sell_in  =10  quality  =20
- "Aged brie"                                   sell_in  =2   quality  =0
- "Elixir of the mongoose"                      sell_in  =5   quality  =7
- "Sulfuras, hand of ragnaros"                  sell_in  =0   quality  =80
- "Sulfuras, hand of ragnaros"                  sell_in  =-1  quality  =80
- "Backstage passes to a tafkal80etc concert"   sell_in  =15  quality  =20
- "Backstage passes to a tafkal80etc concert"   sell_in  =10  quality  =49
- "Backstage passes to a tafkal80etc concert"   sell_in  =5   quality  =49
- "Conjured mana cake"                          sell_in  =3   quality  =6
            
