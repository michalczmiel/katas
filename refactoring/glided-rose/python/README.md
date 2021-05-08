# Python

## Assumptions and changes

> However, do not alter the Item class or Items property...

Plain class was changed to dataclass for better assertion in tests

## Metrics

Computed using [Radon](https://radon.readthedocs.io/en/latest/index.html)

### Cyclomatic Complexity

```text
glided_rose_legacy.py
    M 5:4 GildedRoseLegacy.update_quality - C
    C 1:0 GildedRoseLegacy - C
    M 2:4 GildedRoseLegacy.__init__ - A
glided_rose.py
    C 70:0 BackstagePassItem - A
    M 130:4 ItemsCatalog.from_item - A
    M 74:4 BackstagePassItem.update - A
    C 13:0 Quality - A
    C 90:0 ConjuredItem - A
    C 105:0 NormalItem - A
    C 117:0 ItemsCatalog - A
    C 146:0 GildedRose - A
    M 16:4 Quality.increase - A
    M 20:4 Quality.decrease - A
    C 29:0 DateDays - A
    C 41:0 GildedRoseItem - A
    C 51:0 LegendaryItem - A
    C 60:0 AgedCheeseItem - A
    M 94:4 ConjuredItem.update - A
    M 109:4 NormalItem.update - A
    M 151:4 GildedRose.update_quality - A
    C 6:0 Item - A
    M 24:4 Quality.reset - A
    M 32:4 DateDays.next_day - A
    M 37:4 DateDays.date_passed - A
    M 46:4 GildedRoseItem.update - A
    M 55:4 LegendaryItem.update - A
    M 64:4 AgedCheeseItem.update - A
    M 118:4 ItemsCatalog._is_legendary_item - A
    M 121:4 ItemsCatalog._is_aged_cheese_item - A
    M 124:4 ItemsCatalog._is_backstate_pass_item - A
    M 127:4 ItemsCatalog._is_conjured_item - A
    M 147:4 GildedRose.__init__ - A
```

### Halstead Metrics

```text
glided_rose_legacy.py:
    h1: 7
    h2: 13
    N1: 26
    N2: 52
    vocabulary: 20
    length: 78
    calculated_length: 67.75720079023742
    volume: 337.11039140121426
    difficulty: 14.0
    effort: 4719.545479617
    time: 262.1969710898333
    bugs: 0.11237013046707142
glided_rose.py:
    h1: 6
    h2: 21
    N1: 12
    N2: 24
    vocabulary: 27
    length: 36
    calculated_length: 107.74844088268091
    volume: 171.1759500778849
    difficulty: 3.4285714285714284
    effort: 586.8889716956053
    time: 32.60494287197807
    bugs: 0.05705865002596163
```
