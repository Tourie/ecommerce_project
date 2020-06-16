from users.models import User
from mixer.backend.django import mixer
import pytest


@pytest.fixture
def user(request, db):
    return mixer.blend(User, is_admin=False)


def test_user_model(user):
    assert user.test_person == (user.name, user.username, user.email, user.age, user.activity)

