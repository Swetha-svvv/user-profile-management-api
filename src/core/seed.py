from sqlalchemy.orm import Session

from src.models.user import User


def seed_users(db: Session):

    if db.query(User).count() > 0:
        return

    users = [

        User(
            id="user-1",
            name="Alice Wonderland",
            email="alice@example.com"
        ),

        User(
            id="user-2",
            name="Bob The Builder",
            email="bob@example.com"
        ),

        User(
            id="user-3",
            name="Charlie Chaplin",
            email="charlie@example.com"
        )

    ]

    db.add_all(users)
    db.commit()