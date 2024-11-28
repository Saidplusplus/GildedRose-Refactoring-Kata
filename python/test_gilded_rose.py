# -*- coding: utf-8 -*-
import pytest

from gilded_rose import Item, GildedRose


def test_update_quality_when_sell_in_passed():
    "Once the sell by date has passed, Quality degrades twice as fast"
    quality = 17
    items = [
        Item("item_name", -1, quality),
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    for item in gilded_rose.items:
        assert item.quality == quality - 2


def test_update_quality_quality_never_negative():
    "The Quality of an item is never negative"

    items = [
        Item("item_name", 10, 1),
        Item("item_name", -1, 0),
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    for item in gilded_rose.items:
        assert item.quality >= 0


def test_update_quality_quality_bellow_50():
    "The Quality of an item is never more than 50"

    quality = 50
    sell_in = 10
    items = [
        Item("item_name", sell_in, 49),
        Item("item_name", sell_in, quality),
        Item("Aged Brie", sell_in, quality),
        Item("Sulfuras, Hand of Ragnaros", sell_in, quality),
        Item("Backstage passes to a TAFKAL80ETC concert", sell_in, quality)
    ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    for item in gilded_rose.items:
        assert item.quality <= 50


def test_update_quality_aged_brie_quality_increase():
    "'Aged Brie' actually increases in Quality the older it gets"

    sell_in = 10
    initial_quality = 40

    items = [
        Item("Aged Brie", sell_in, initial_quality),
    ]

    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    for item in gilded_rose.items:
        assert item.quality > initial_quality


def test_update_quality_sulfuras_quality_never_decrease():
    "'Sulfuras', being a legendary item, never has to be sold or decreases in Quality"

    initial_quality = 4
    items = [
        Item("Sulfuras, Hand of Ragnaros", 10, initial_quality),
        Item("Sulfuras, Hand of Ragnaros", -1, initial_quality),
    ]

    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    for item in gilded_rose.items:
        assert item.quality >= initial_quality


def test_update_quality_quality_backstage_when_sell_in_between_5_and_10():
    "Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but"

    initial_quality = 40
    items = [
        Item("Backstage passes to a TAFKAL80ETC concert", 10, initial_quality),
        Item("Backstage passes to a TAFKAL80ETC concert", 7, initial_quality),
    ]

    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    for item in gilded_rose.items:
        assert item.quality == initial_quality + 2


def test_update_quality_quality_backstage_when_sell_in_lt_5():
    "Quality increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but"

    initial_quality = 40
    items = [
        Item("Backstage passes to a TAFKAL80ETC concert", 5, initial_quality),
        Item("Backstage passes to a TAFKAL80ETC concert", 2, initial_quality),
    ]

    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    for item in gilded_rose.items:
        assert item.quality == initial_quality + 3


def test_update_quality_quality_backstage_when_sell_in_negative():
    "Quality drops to 0 after the concert"

    initial_quality = 40
    items = [
        Item("Backstage passes to a TAFKAL80ETC concert", 0, initial_quality),
        Item("Backstage passes to a TAFKAL80ETC concert", -1, initial_quality),
    ]

    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    for item in gilded_rose.items:
        assert item.quality == 0
