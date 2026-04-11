try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ImportError:
    print("Error: pydantic is not installed.")
    exit(1)
from enum import Enum
from typing import Optional
from datetime import datetime


class ContactType(Enum):

    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType = Field(...)
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate_contact_rules(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.telepathic and
                not self.witness_count > 2):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 40)
    try:
        alien = AlienContact(contact_id="AC_2024_001",
                             timestamp=datetime(2026, 4, 11, 0, 0, 0),
                             location="Area 51, Nevada",
                             contact_type=ContactType.radio,
                             signal_strength=8.5,
                             duration_minutes=45,
                             witness_count=5,
                             message_received='Greetings from Zeta Reticuli')
        print("Valid contact report:")
        print(f"ID: {alien.contact_id}")
        print(f"Type: {alien.contact_type.value}")
        print(f"Location: {alien.location}")
        print(f"Signal: {alien.signal_strength}/10")
        print(f"Duration: {alien.duration_minutes} minutes")
        print(f"Witnesses: {alien.witness_count}")
        print(f"Message: '{alien.message_received}'")
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]['msg'].removeprefix("Value error, "))

    print()
    print("=" * 40)

    try:
        alien = AlienContact(contact_id="AC_2024_001",
                             timestamp=datetime(2026, 4, 11, 0, 0, 0),
                             location="Area 51, Nevada",
                             contact_type=ContactType.telepathic,
                             signal_strength=8.5,
                             duration_minutes=45,
                             witness_count=2,
                             message_received='Greetings from Zeta Reticuli')
        print("Valid contact report:")
        print(f"ID: {alien.contact_id}")
        print(f"Type: {alien.contact_type.value}")
        print(f"Location: {alien.location}")
        print(f"Signal: {alien.signal_strength}/10")
        print(f"Duration: {alien.duration_minutes} minutes")
        print(f"Witnesses: {alien.witness_count}")
        print(f"Message: '{alien.message_received}'")
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]['msg'].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
