"""
User related functionality
"""

from sqlalchemy import Column, Integer, String
from src import repo
from typing import Optional
from src.models.base import Base
from datetime import datetime


class User(Base):
    """User representation"""
    __tablename__ = 'users'

    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)

    def __init__(
        self,
        email: str,
        first_name: str,
        last_name: str,
        password: Optional[str] = None,
        **kw,
    ):
        """Dummy init"""
        super().__init__(**kw)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self) -> str:
        """Dummy repr"""
        return f"<User {self.id} ({self.email})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(user: dict) -> "User":
        """Create a new user"""
        users: list["User"] = User.get_all()

        for u in users:
            if u.email == user["email"]:
                raise ValueError("User already exists")

        new_user = User(**user)

        repo.save(new_user)

        return new_user

    @staticmethod
    def update(user_id: str, data: dict) -> "User | None":
        """Update an existing user"""
        user: User | None = User.get(user_id)

        if not user:
            return None

        if "email" in data:
            user.email = data["email"]
        if "first_name" in data:
            user.first_name = data["first_name"]
        if "last_name" in data:
            user.last_name = data["last_name"]

        repo.update(user)

        return user
