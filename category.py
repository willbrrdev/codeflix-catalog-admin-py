from dataclasses import dataclass, field
import uuid
from uuid import UUID


@dataclass
class Category:
    name: str
    description: str = ""
    is_active: bool = True
    id: UUID = field(default_factory=uuid.uuid4)

    def __post_init__(self):
        self.validate()

    # def __init__(
    #     self,
    #     name,
    #     id="",
    #     description="",
    #     is_active=True,
    # ):
    #     self.id = id or uuid.uuid4()
    #     self.name = name
    #     self.description = description
    #     self.is_active = is_active

    #     self.validate()

    def validate(self):
        if len(self.name) > 255:
            raise ValueError("name cannot be longer than 255 characters")

        if not self.name:  # len(self.name) == 0:
            raise ValueError("name cannot be empty")

    def __str__(self):
        return f"{self.name} - {self.description} - {self.is_active}"

    def __repr__(self):
        return f"<Category {self.name} ({self.id})>"

    def __eq__(self, other):
        if not isinstance(other, Category):
            return False

        return self.id == other.id

    def update(self, name, description):
        self.name = name
        self.description = description

        self.validate()

    def activate(self):
        self.is_active = True
        self.validate()

    def deactivate(self):
        self.is_active = False
        self.validate()
