from abc import ABC, abstractmethod
from dataclasses import dataclass, replace


@dataclass
class Item:
    name: str
    sell_in: int
    quality: int


@dataclass(frozen=True)
class Quality:
    value: int

    def increase(self) -> "Quality":
        value = self.value + 1 if self.value < 50 else self.value
        return replace(self, value=value)

    def decrease(self) -> "Quality":
        value = self.value - 1 if self.value > 0 else self.value
        return replace(self, value=value)

    def reset(self) -> "Quality":
        return replace(self, value=0)


@dataclass(frozen=True, order=True)
class DateDays:
    value: int

    def next_day(self) -> "Days":
        value = self.value - 1
        return replace(self, value=value)

    @property
    def date_passed(self) -> bool:
        return self.value < 0


class GildedRoseItem(ABC):
    @abstractmethod
    def update(self):
        pass


@dataclass
class LegendaryItem(GildedRoseItem):
    quality: Quality
    sell_in: DateDays

    def update(self):
        pass


@dataclass
class AgedCheeseItem(GildedRoseItem):
    quality: Quality
    sell_in: DateDays

    def update(self):
        self.quality = self.quality.increase()
        self.sell_in = self.sell_in.next_day()


@dataclass
class BackstagePassItem(GildedRoseItem):
    quality: Quality
    sell_in: DateDays

    def update(self):
        self.quality = self.quality.increase()

        if self.sell_in < DateDays(11):
            self.quality = self.quality.increase()

        if self.sell_in < DateDays(6):
            self.quality = self.quality.increase()

        self.sell_in = self.sell_in.next_day()

        if self.sell_in.date_passed:
            self.quality = self.quality.reset()


@dataclass
class NormalItem(GildedRoseItem):
    quality: Quality
    sell_in: DateDays

    def update(self):
        self.quality = self.quality.decrease()
        self.sell_in = self.sell_in.next_day()

        if self.sell_in.date_passed:
            self.quality = self.quality.decrease()


class ItemsCatalog:
    def _is_legendary_item(self, item: Item) -> bool:
        return item.name == "Sulfuras, Hand of Ragnaros"

    def _is_aged_cheese_item(self, item: Item) -> bool:
        return item.name == "Aged Brie"

    def _is_backstate_pass_item(self, item: Item) -> bool:
        return item.name == "Backstage passes to a TAFKAL80ETC concert"

    def from_item(self, item: Item) -> GildedRoseItem:
        quality = Quality(item.quality)
        sell_in = DateDays(item.sell_in)

        if self._is_legendary_item(item):
            return LegendaryItem(quality=quality, sell_in=sell_in)
        elif self._is_aged_cheese_item(item):
            return AgedCheeseItem(quality=quality, sell_in=sell_in)
        elif self._is_backstate_pass_item(item):
            return BackstagePassItem(quality=quality, sell_in=sell_in)
        else:
            return NormalItem(quality=quality, sell_in=sell_in)


class GildedRose:
    def __init__(self, items: Item):
        self.items = items
        self._catalog = ItemsCatalog()

    def update_quality(self):
        for item in self.items:
            glided_rose_item = self._catalog.from_item(item)

            glided_rose_item.update()

            item.quality = glided_rose_item.quality.value
            item.sell_in = glided_rose_item.sell_in.value
