from abc import ABC, abstractmethod
from dataclasses import dataclass, replace


@dataclass
class Item:
    name: str
    sell_in: int
    quality: int


class GildedRoseLegacy:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if (
                item.name != "Aged Brie"
                and item.name != "Backstage passes to a TAFKAL80ETC concert"
            ):
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


@dataclass
class LegendaryItem:
    item: Item

    def update_quality(self):
        pass


@dataclass
class DefaultItem:
    item: Item

    def update_quality(self):
        if (
            self.item.name != "Aged Brie"
            and self.item.name != "Backstage passes to a TAFKAL80ETC concert"
        ):
            if self.item.quality > 0:
                self.item.quality = self.item.quality - 1
        else:
            if self.item.quality < 50:
                self.item.quality = self.item.quality + 1
                if self.item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if self.item.sell_in < 11:
                        if self.item.quality < 50:
                            self.item.quality = self.item.quality + 1
                    if self.item.sell_in < 6:
                        if self.item.quality < 50:
                            self.item.quality = self.item.quality + 1

        self.item.sell_in = self.item.sell_in - 1

        if self.item.sell_in < 0:
            if self.item.name != "Aged Brie":
                if self.item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if self.item.quality > 0:
                        self.item.quality = self.item.quality - 1
                else:
                    self.item.quality = self.item.quality - self.item.quality
            else:
                if self.item.quality < 50:
                    self.item.quality = self.item.quality + 1


class GildedRose:
    def __init__(self, items):
        self.items = items

    def _is_legendary_item(self, item: Item) -> bool:
        return item.name == "Sulfuras, Hand of Ragnaros"

    def update_quality(self):
        for item in self.items:
            if self._is_legendary_item(item):
                LegendaryItem(item).update_quality()
            else:
                DefaultItem(item).update_quality()
