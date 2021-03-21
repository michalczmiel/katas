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


@dataclass(frozen=True)
class DateDays:
    value: int

    def next_day(self) -> "Days":
        value = self.value - 1
        return replace(self, value=value)

    @property
    def date_passed(self) -> bool:
        return self.value < 0


class ItemPolicy(ABC):
    @classmethod
    @abstractmethod
    def update_quality(cls, quality: Quality, sell_in: DateDays) -> [Quality, DateDays]:
        pass


class LegendaryItemPolicy(ItemPolicy):
    @classmethod
    def update_quality(cls, quality: Quality, sell_in: DateDays) -> [Quality, DateDays]:
        return [quality, sell_in]


class AgedCheeseItemPolicy(ItemPolicy):
    @classmethod
    def update_quality(cls, quality: Quality, sell_in: DateDays) -> [Quality, DateDays]:
        new_quality = quality.increase()

        new_sell_in = sell_in.next_day()

        return [new_quality, new_sell_in]


class BackstagePassItemPolicy(ItemPolicy):
    @classmethod
    def update_quality(cls, quality: Quality, sell_in: DateDays) -> [Quality, DateDays]:
        new_quality = quality.increase()

        if sell_in.value < 11:
            new_quality = new_quality.increase()
        if sell_in.value < 6:
            new_quality = new_quality.increase()

        new_sell_in = sell_in.next_day()

        if new_sell_in.date_passed:
            new_quality = new_quality.reset()

        return [new_quality, new_sell_in]


class DefaultItemPolicy(ItemPolicy):
    @classmethod
    def update_quality(cls, quality: Quality, sell_in: DateDays) -> [Quality, DateDays]:
        new_quality = quality.decrease()

        new_sell_in = sell_in.next_day()

        if new_sell_in.date_passed:
            new_quality = new_quality.decrease()

        return [new_quality, new_sell_in]


class GildedRose:
    def __init__(self, items):
        self.items = items

    def _is_legendary_item(self, item: Item) -> bool:
        return item.name == "Sulfuras, Hand of Ragnaros"

    def _is_aged_cheese_item(self, item: Item) -> bool:
        return item.name == "Aged Brie"

    def _is_backstate_pass_item(self, item: Item) -> bool:
        return item.name == "Backstage passes to a TAFKAL80ETC concert"

    def get_policy_for_item(self, item: Item):
        if self._is_legendary_item(item):
            return LegendaryItemPolicy
        elif self._is_aged_cheese_item(item):
            return AgedCheeseItemPolicy
        elif self._is_backstate_pass_item(item):
            return BackstagePassItemPolicy
        else:
            return DefaultItemPolicy

    def update_quality(self):
        for item in self.items:
            policy = self.get_policy_for_item(item)
            quality = Quality(item.quality)
            sell_in = DateDays(item.sell_in)

            updated_quality, updated_sell_in = policy.update_quality(quality, sell_in)

            item.quality = updated_quality.value
            item.sell_in = updated_sell_in.value
