from django.urls import reverse
from django.test import RequestFactory
from users.models import User
from users.views import users_list, user_detail_update, user_detail_view, UserDelete
from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestUsersView:

    def test_user_detail_view(self):
        path = reverse('user_detail_url', kwargs={'username': 'sdaf'})
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = user_detail_view(request, username='wrer')
        assert response.status_code == 200

    def test_user_update_view(self):
        path = reverse('user_detail_update_url', kwargs={'username': 'sdaf'})
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = user_detail_update(request, username='wrer')
        assert response.status_code == 200

    def test_user_list_view(self):
        path = reverse('users_list_url')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = users_list(request)
        assert response.status_code == 200