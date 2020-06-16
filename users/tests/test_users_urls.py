from django.urls import reverse, resolve
import pytest


def make_reverse(str):
    return reverse(str, kwargs={'username': 'admin'})


@pytest.mark.parametrize("test_input, expected", [(make_reverse('user_detail_url'), 'user_detail_url'), (make_reverse('user_detail_update_url'), 'user_detail_update_url'), (make_reverse('user_detail_delete_url'), 'user_detail_delete_url')])
def test_detail_url(test_input, expected):
    assert resolve(test_input).view_name == expected


def test_users_list_url():
    path = reverse('users_list_url')
    assert resolve(path).view_name == 'users_list_url'

