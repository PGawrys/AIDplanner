from django.test import TestCase
from django.contrib.auth.models import User
import pytest
from django.test import Client
from django.urls import reverse

from AidplannerApp.models import Spot, Item


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



@pytest.mark.django_db
def test_show_spots(spots):
    client = Client()
    url = reverse("show_spot")
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(spots)
    for spot in spots:
        assert spot in response.context['object_list']
#
# @pytest.mark.django_db
# def test_post_list(posts):
#     client = Client()
#     url = reverse("show_post")
#     response = client.get(url)
#     assert response.status_code == 200
#     assert response.context['object_list'].count() == len(posts)
#     for post in posts:
#         assert post in response.context['object_list']


@pytest.mark.django_db
def test_check_add_spot_logged_out():
    client = Client()
    url = reverse("add_spot")
    response = client.get(url)
    assert response.status_code == 302   # bo w bazowej wersji nie jestesmy zalogowani wiec code 302


@pytest.mark.django_db
def test_add_spot_logged_in(user):
    url = reverse("add_spot")
    client = Client()
    client.force_login(user)
    data = {'name':'x', 'address':'ulica 1 m 10', 'details':'za rogiem'}
    response = client.post(url, data)         #czy wchodzi i czy udalo sie dane przeslac bo POST jak get to response 200
    assert response.status_code == 302
    Spot.objects.get(name='x', address='ulica 1 m 10', details='za rogiem')   #nie trzeba asserta

@pytest.mark.django_db
def test_check_add_item_logged_out():
    client = Client()
    url = reverse("add_item")
    response = client.get(url)
    assert response.status_code == 200        #a moze redirect w view? wtedy 302


@pytest.mark.django_db
def test_add_item_logged_in(user):
    url = reverse("add_item")
    client = Client()
    client.force_login(user)
    data = {'name':'x', 'description':'przedmiot', 'number_needed':15, 'number_delivered':5 }
    response = client.post(url, data)
    assert response.status_code == 302
    Item.objects.get(name='x', description='przedmiot', number_needed=15, number_delivered=5)

# @pytest.mark.django_db
# def test_register_user():
#     url = reverse("register")
#     client = Client()
#     data = {'username':'user', 'pass1':'user', 'pass2':'user'}
#     response = client.post(url, data)         #czy wchodzi i czy udalo sie dane przeslac bo POST jak get to response 200
#     assert response.status_code == 302
#     User.objects.get(username='user')               #sprawdza czy dodano usera
#     client.login(username="user", password="user")  #sprawdza czy uda sie zalogowac z haslem
#
#
# @pytest.mark.django_db
# def test_add_post(blogs):
#     url = reverse("add_post")
#     client = Client()
#     data = {'text':'nanana','blog':blogs[0].id}
#     response = client.post(url, data)
#     assert response.status_code == 302
#
#     assert Post.objects.first()     # zwraca true / false