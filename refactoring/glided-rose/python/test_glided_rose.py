import unittest

from glided_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_normal_item_quality_degrades(self):
        items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        ]
        rose = GildedRose(items)
        rose.update_quality()
        self.assertListEqual(
            rose.items,
            [
                Item(name="+5 Dexterity Vest", sell_in=9, quality=19),
                Item(name="Elixir of the Mongoose", sell_in=4, quality=6),
            ],
        )

    def test_once_sell_date_has_passed_quality_of_normal_item_degrades_twice_as_fast(
        self,
    ):
        items = [
            Item(name="+5 Dexterity Vest", sell_in=0, quality=20),
        ]
        rose = GildedRose(items)
        rose.update_quality()
        self.assertListEqual(
            rose.items,
            [
                Item(name="+5 Dexterity Vest", sell_in=-1, quality=18),
            ],
        )

    def test_item_quality_is_never_negative(self):
        items = [
            Item(name="+5 Dexterity Vest", sell_in=1, quality=0),
        ]
        rose = GildedRose(items)
        rose.update_quality()
        self.assertListEqual(
            rose.items,
            [
                Item(name="+5 Dexterity Vest", sell_in=0, quality=0),
            ],
        )

    def test_aged_brie_increases_quality_over_time(self):
        items = [
            Item(name="Aged Brie", sell_in=2, quality=0),
        ]
        rose = GildedRose(items)
        rose.update_quality()
        self.assertListEqual(
            rose.items,
            [
                Item(name="Aged Brie", sell_in=1, quality=1),
            ],
        )

    def test_item_quality_is_never_more_than_50_for_normal_items(self):
        items = [
            Item(name="Aged Brie", sell_in=2, quality=50),
        ]
        rose = GildedRose(items)
        rose.update_quality()
        self.assertListEqual(
            rose.items,
            [
                Item(name="Aged Brie", sell_in=1, quality=50),
            ],
        )

    def test_legendary_item_sulfuras_does_not_have_to_be_sold_or_decrease_quality(self):
        items = [
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
        ]
        rose = GildedRose(items)
        rose.update_quality()
        self.assertListEqual(
            rose.items,
            [
                Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
                Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            ],
        )

    def test_backstage_pass_increases_quality_over_time(self):
        items = [
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20
            ),
        ]
        rose = GildedRose(items)
        rose.update_quality()
        self.assertListEqual(
            rose.items,
            [
                Item(
                    name="Backstage passes to a TAFKAL80ETC concert",
                    sell_in=14,
                    quality=21,
                ),
            ],
        )

    def test_backstage_pass_increases_more_in_quality_when_10_days_or_less(self):
        items = [
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=20
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=20
            ),
        ]
        rose = GildedRose(items)
        rose.update_quality()
        self.assertListEqual(
            rose.items,
            [
                Item(
                    name="Backstage passes to a TAFKAL80ETC concert",
                    sell_in=10,
                    quality=21,
                ),
                Item(
                    name="Backstage passes to a TAFKAL80ETC concert",
                    sell_in=9,
                    quality=22,
                ),
                Item(
                    name="Backstage passes to a TAFKAL80ETC concert",
                    sell_in=8,
                    quality=22,
                ),
            ],
        )

    def test_backstage_pass_increases_even_more_in_quality_when_5_days_or_less(self):
        items = [
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=6, quality=20
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=20
            ),
        ]
        rose = GildedRose(items)
        rose.update_quality()
        self.assertListEqual(
            rose.items,
            [
                Item(
                    name="Backstage passes to a TAFKAL80ETC concert",
                    sell_in=5,
                    quality=22,
                ),
                Item(
                    name="Backstage passes to a TAFKAL80ETC concert",
                    sell_in=4,
                    quality=23,
                ),
                Item(
                    name="Backstage passes to a TAFKAL80ETC concert",
                    sell_in=3,
                    quality=23,
                ),
            ],
        )

    def test_backstage_pass_quality_drops_to_zero_after_concert(self):
        items = [
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=23
            ),
        ]
        rose = GildedRose(items)
        rose.update_quality()
        self.assertListEqual(
            rose.items,
            [
                Item(
                    name="Backstage passes to a TAFKAL80ETC concert",
                    sell_in=-1,
                    quality=0,
                ),
                Item(
                    name="Backstage passes to a TAFKAL80ETC concert",
                    sell_in=-2,
                    quality=0,
                ),
            ],
        )

    def test_conjured_items_degrade_in_quality_twice_as_fast(self):
        items = [
            Item(name="Conjured Mana Pie", sell_in=10, quality=20),
            Item(name="Conjured Mana Cookie", sell_in=0, quality=8),
        ]
        rose = GildedRose(items)
        rose.update_quality()
        self.assertListEqual(
            rose.items,
            [
                Item(
                    name="Conjured Mana Pie",
                    sell_in=9,
                    quality=18,
                ),
                Item(
                    name="Conjured Mana Cookie",
                    sell_in=-1,
                    quality=4,
                ),
            ],
        )


if __name__ == "__main__":
    unittest.main()
