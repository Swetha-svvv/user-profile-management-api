from abc import ABC, abstractmethod

from src.core.database import SessionLocal
from src.repositories.implementations.user_repository import UserRepository


class IUnitOfWork(ABC):

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass


class UnitOfWork(IUnitOfWork):

    def __init__(self):
        self.db = SessionLocal()
        self.users = UserRepository(self.db)

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

    def close(self):
        self.db.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        if exc_type:
            self.rollback()
        else:
            self.commit()

        self.close()