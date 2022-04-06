import pytest
from django.contrib.auth.models import User

from AidplannerApp.models import User


@pytest.fixture
def users():
    users = []
    for i in range(30):
        u = User.objects.create(username=i)
        users.append(u)
    return users