from django.test import TestCase
from django.contrib.auth.models import User
import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_initial():
    assert True


@pytest.mark.django_db
def test_index():
    client = Client()
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_list(users):
    client = Client()
    url = reverse("userlist")
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(users)
    for user in users:
        assert user in response.context['object_list']