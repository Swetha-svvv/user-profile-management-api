from unittest.mock import MagicMock, patch

import pytest

from src.schemas.user_schema import UserCreate
from src.services.user_service import UserService


@patch("src.services.user_service.UnitOfWork")
def test_create_user_success(mock_uow):

    mock_instance = MagicMock()

    mock_uow.return_value = mock_instance

    mock_instance.users.get_by_email.return_value = None

    service = UserService()

    user = UserCreate(
        name="Swetha",
        email="swetha@example.com"
    )

    result = service.create_user(user)

    assert result.name == "Swetha"

    assert result.email == "swetha@example.com"

    mock_instance.users.create.assert_called_once()

    mock_instance.commit.assert_called_once()


@patch("src.services.user_service.UnitOfWork")
def test_create_duplicate_email(mock_uow):

    mock_instance = MagicMock()

    mock_uow.return_value = mock_instance

    mock_instance.users.get_by_email.return_value = MagicMock()

    service = UserService()

    user = UserCreate(
        name="Swetha",
        email="swetha@example.com"
    )

    with pytest.raises(ValueError):

        service.create_user(user)