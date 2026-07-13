from sqlalchemy.orm import Session

from src.models.user import User
from src.repositories.interfaces.user_repository import IUserRepository


class UserRepository(IUserRepository):

    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User):

        self.db.add(user)

        return user

    def get_by_id(self, user_id: str):

        return (
            self.db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    def get_all(self):

        return (
            self.db.query(User)
            .all()
        )

    def get_by_email(self, email: str):

        return (
            self.db.query(User)
            .filter(User.email == email)
            .first()
        )

    def update(self, user: User):

        self.db.add(user)

        return user

    def delete(self, user: User):

        self.db.delete(user)