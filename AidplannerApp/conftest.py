import pytest
from django.contrib.auth.models import User

from AidplannerApp.models import User, Spot, Item


@pytest.fixture
def users():
    users = []
    for i in range(30):
        u = User.objects.create(username=i)
        users.append(u)
    return users

@pytest.fixture
def user():
    return User.objects.create(username='x')

@pytest.fixture
def spots():
    spots = []
    for i in range(20):
        s = Spot.objects.create(name=i)
        spots.append(s)
    return spots

@pytest.fixture
def items():
    items = []
    for i in range(20):
        x = Item.objects.create(name=i)
        items.append(x)
    return items