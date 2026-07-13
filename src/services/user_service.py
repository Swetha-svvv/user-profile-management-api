from src.models.user import User
from src.schemas.user_schema import UserCreate, UserUpdate
from src.unit_of_work.unit_of_work import UnitOfWork
from src.services.enrichment_service import EnrichmentService

class UserService:

    def __init__(self):
        self.uow = UnitOfWork()

    def create_user(self, user: UserCreate):

        existing = self.uow.users.get_by_email(user.email)

        if existing:
            raise ValueError("Email already exists")

        new_user = User(
            name=user.name,
            email=user.email
        )

        self.uow.users.create(new_user)

        self.uow.commit()

        return new_user

    def get_user(self, user_id: str):

        user = self.uow.users.get_by_id(user_id)

        if not user:
            raise ValueError("User not found")

        return user

    def get_all_users(self):

        return self.uow.users.get_all()

    def update_user(self, user_id: str, data: UserUpdate):

        user = self.uow.users.get_by_id(user_id)

        if not user:
            raise ValueError("User not found")

        existing = self.uow.users.get_by_email(data.email)

        if existing and existing.id != user.id:
            raise ValueError("Email already exists")

        user.name = data.name
        user.email = data.email

        self.uow.users.update(user)

        self.uow.commit()

        return user

    def delete_user(self, user_id: str):

        user = self.uow.users.get_by_id(user_id)

        if not user:
            raise ValueError("User not found")

        self.uow.users.delete(user)

        self.uow.commit()

        return True
    
    
    def get_enriched_user(self, user_id: str):

        user = self.uow.users.get_by_id(user_id)

        if not user:
            raise ValueError("User not found")

        try:

            enrichment = EnrichmentService.get_enrichment(user_id)

            return {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "registration_date": user.registration_date,
                "recentActivity": enrichment.get("recentActivity", []),
                "loyaltyScore": enrichment.get("loyaltyScore", 0),
                "enrichedDataStatus": "available"
            }

        except Exception:

            return {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "registration_date": user.registration_date,
                "enrichedDataStatus": "unavailable",
                "message": "External enrichment service is currently unavailable."
            }