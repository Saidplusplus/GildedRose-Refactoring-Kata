# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass
class ItemTypes(object):
    "Item types in the store that have special treatement in the GildedRose.update_quality"

    BRIE = "Aged Brie"
    BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    CONJURED = "Conjured"


def update_brie_item_quality(item):
    if item.quality < 50:
        item.quality = item.quality + 1
    item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        if item.quality < 50:
            item.quality = item.quality + 1


def update_sulfuras_item_quality(item):
    """
        "Sulfuras" is a legendary item and as such its Quality is 80 and it never alters
    """
    ...


def update_backstage_item_quality(item):
    if item.quality < 50:
        item.quality = item.quality + 1
        if item.sell_in < 11:
            if item.quality < 50:
                item.quality = item.quality + 1
        if item.sell_in < 6:
            if item.quality < 50:
                item.quality = item.quality + 1
    item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        item.quality = item.quality - item.quality


def update_normal_item_quality(item):
    if item.quality > 0:
        item.quality = item.quality - 1
    item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        if item.quality > 0:
            item.quality = item.quality - 1


def update_conjured_item_quality(item):
    if item.quality > 0:
        item.quality = item.quality - 2
    item.sell_in = item.sell_in - 1
    if item.sell_in < 0:
        if item.quality > 0:
            item.quality = item.quality - 2


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == ItemTypes.BRIE:
                update_brie_item_quality(item)
            elif item.name == ItemTypes.BACKSTAGE:
                update_backstage_item_quality(item)
            elif item.name == ItemTypes.SULFURAS:
                update_sulfuras_item_quality(item)
            elif item.name == ItemTypes.CONJURED:
                update_conjured_item_quality(item)
            else:
                update_normal_item_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
