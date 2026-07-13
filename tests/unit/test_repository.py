from unittest.mock import MagicMock

from src.models.user import User
from src.repositories.implementations.user_repository import UserRepository


def test_create_user():

    db = MagicMock()

    repo = UserRepository(db)

    user = User(
        name="Swetha",
        email="swetha@example.com"
    )

    repo.create(user)

    db.add.assert_called_once_with(user)


def test_update_user():

    db = MagicMock()

    repo = UserRepository(db)

    user = User(
        name="Swetha",
        email="swetha@example.com"
    )

    repo.update(user)

    db.add.assert_called_once_with(user)


def test_delete_user():

    db = MagicMock()

    repo = UserRepository(db)

    user = User(
        name="Swetha",
        email="swetha@example.com"
    )

    repo.delete(user)

    db.delete.assert_called_once_with(user)