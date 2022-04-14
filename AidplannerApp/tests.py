import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from AidplannerApp.models import Spot, Item, Service, ItemCollection, ServiceCollection


@pytest.mark.django_db
def test_initial():
    assert True


@pytest.mark.django_db
def test_register_user():
    url = reverse("register")
    client = Client()
    data = {'username':'user', 'pass1':'user', 'pass2':'user'}
    response = client.post(url, data)
    assert response.status_code == 302
    User.objects.get(username='user')
    client.login(username="user", password="user")

@pytest.mark.django_db
def test_login():
    url = reverse("login")
    client = Client()
    data = {'username':'user', 'pass1':'user', 'pass2':'user'}
    response = client.post(url, data)
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
def test_index():
    client = Client()
    url = reverse("index")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_collections():
    client = Client()
    url = reverse("collections")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_schedule():
    client = Client()
    url = reverse("schedule")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_stats():
    client = Client()
    url = reverse("stats")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_show_spots(spots):
    client = Client()
    url = reverse("show_spot")
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(spots)
    for spot in spots:
        assert spot in response.context['object_list']


@pytest.mark.django_db
def test_check_add_spot_logged_out():
    client = Client()
    url = reverse("add_spot")
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_add_spot_logged_in(user):
    url = reverse("add_spot")
    client = Client()
    client.force_login(user)
    data = {'name':'x', 'address':'ulica 1 m 10', 'details':'za rogiem'}
    response = client.post(url, data)
    assert response.status_code == 302
    Spot.objects.get(name='x', address='ulica 1 m 10', details='za rogiem')


@pytest.mark.django_db
def test_show_edit_item_details(user):
    url = reverse("item_list")
    client = Client()
    client.force_login(user)
    data = {'name': 'x', 'description': 'xyz'}
    response = client.post(url, data)
    assert response.status_code == 302
    Item.objects.get(name='x', description='xyz')


@pytest.mark.django_db
def test_show_edit_service_details(user):
    url = reverse("service_list")
    client = Client()
    client.force_login(user)
    data = {'name': 'test', 'description': 'testtest'}
    response = client.post(url, data)
    assert response.status_code == 302
    Service.objects.get(name='test', description='testtest')


@pytest.mark.django_db
def test_show_spot_details(spot, user):
    url = reverse("show_detail_spot", kwargs={'id':1})
    client = Client()
    client.force_login(user)
    data = {'name':'y', 'address':'ulica 2 m 345', 'details':'important details'}
    response = client.post(url, data)
    assert response.status_code == 200
    Spot.objects.get(name='y', address='ulica 2 m 345', details='important details')


@pytest.mark.django_db
def test_show_add_item_collection(user):
    url = reverse("add_collection_item")
    client = Client()
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_item_collection(user, item, spot):
    url = reverse("add_collection_item")
    client = Client()
    client.force_login(user)
    data = {'name': 'xyz', 'spot': spot.id, 'description': 'o', 'items': [item.id]}
    response = client.post(url, data)
    assert response.status_code == 302
    assert ItemCollection.objects.filter(name='xyz').count() == 1


@pytest.mark.django_db
def test_show_add_service_collection(user):
    url = reverse("add_collection_service")
    client = Client()
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_service_collection(user, service, spot):
    url = reverse("add_collection_service")
    client = Client()
    client.force_login(user)
    data = {'name': 'xyz', 'spot': spot.id, 'description': 'o', 'services': [service.id]}
    response = client.post(url, data)
    assert response.status_code == 302
    assert ServiceCollection.objects.filter(name='xyz').count() == 1


@pytest.mark.django_db
def test_show_edit_item_collection(user, item_collection):
    url = reverse("update_item_collection", kwargs={'id': item_collection.id})
    client = Client()
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_edit_collection_item(user, item, spot, item_collection):
    url = reverse("update_item_collection", kwargs={'id': item_collection.id})
    client = Client()
    client.force_login(user)
    data = {'name': 'abc', 'spot': spot.id, 'description': 'o', 'items': [item.id]}
    response = client.post(url, data)
    assert response.status_code == 302
    assert ItemCollection.objects.filter(name='abc').count() == 1


@pytest.mark.django_db
def test_show_edit_service_collection(user, service_collection):
    url = reverse("update_service_collection", kwargs={'id': service_collection.id})
    client = Client()
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_edit_collection_service(user, service, spot, service_collection):
    url = reverse("update_service_collection", kwargs={'id': service_collection.id})
    client = Client()
    client.force_login(user)
    data = {'name': 'abc', 'spot': spot.id, 'description': 'o', 'services': [service.id]}
    response = client.post(url, data)
    assert response.status_code == 302
    assert ServiceCollection.objects.filter(name='abc').count() == 1


# @pytest.mark.django_db
# def test_update_item_in_collection_view(user, item, item_collection):
#     url = reverse()
