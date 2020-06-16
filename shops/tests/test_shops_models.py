from shops.models import Shop, Item, Category
from mixer.backend.django import mixer
import pytest


@pytest.fixture
def shop(request, db):
    return mixer.blend(Shop)


@pytest.fixture
def item(request, db):
    return mixer.blend(Item)


@pytest.fixture
def category(request, db):
    return mixer.blend(Category)


def test_shop_model(shop):
    assert shop.test_shop == (shop.title, shop.description, shop.founder, shop.thumbnail)


def test_item_model(item):
    assert item.test_item == (item.title, item.description, item.shop, item.category, item.price, item.quantity)


def test_category_model(category):
    assert category.test_category == category.name
