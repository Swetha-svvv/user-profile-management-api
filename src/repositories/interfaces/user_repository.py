from abc import ABC
from abc import abstractmethod

from src.models.user import User


class IUserRepository(ABC):

    @abstractmethod
    def create(self, user: User):
        pass

    @abstractmethod
    def get_by_id(self, user_id: str):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_email(self, email: str):
        pass

    @abstractmethod
    def update(self, user: User):
        pass

    @abstractmethod
    def delete(self, user: User):
        pass