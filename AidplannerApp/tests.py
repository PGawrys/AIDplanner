from django.test import TestCase
from django.contrib.auth.models import User
import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_initial():
    assert True