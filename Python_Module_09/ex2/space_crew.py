try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ImportError:
    print("Error: pydantic is not installed.")
    exit(1)
from enum import Enum
from datetime import datetime
from typing import List


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):

    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        ranks = [Rank.commander, Rank.captain]
        has_rank = any(member.rank in ranks for member in self.crew)
        if not has_rank:
            raise ValueError(
                "Mission must have at least one Commander or Captain")

        if self.duration_days > 365:
            experienced = 0
            for i in self.crew:
                if i.years_experience >= 5:
                    experienced += 1
            if experienced / len(self.crew) < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) need 50% :"
                    "experienced crew (5+ years)")

        for i in self.crew:
            if not i.is_active:
                raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)
    try:
        member1 = CrewMember(member_id="0001",
                             name="Sarah Connor",
                             rank=Rank.commander,
                             age=46,
                             specialization="Mission Command",
                             years_experience=26)
        member2 = CrewMember(member_id="0002",
                             name="John Smith",
                             rank=Rank.lieutenant,
                             age=35,
                             specialization="Navigation",
                             years_experience=15)
        member3 = CrewMember(member_id="0003",
                             name="Alice Johnson",
                             rank=Rank.officer,
                             age=26,
                             specialization="Engineering",
                             years_experience=6)
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2026, 4, 10, 1, 10),
            duration_days=900,
            crew=[member1, member2, member3],
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print("Mission:", mission.mission_name)
        print("ID:", mission.mission_id)
        print("Destination:", mission.destination)
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print("Crew size:", len(mission.crew))
        print("Crew members:")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank.value}) - {member.specialization}")
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]['msg'].removeprefix("Value error, "))

    print()

    print("=" * 40)
    try:
        member1 = CrewMember(member_id="0004",
                             name="John Smith",
                             rank=Rank.lieutenant,
                             age=35,
                             specialization="Navigation",
                             years_experience=15)
        member2 = CrewMember(member_id="0005",
                             name="Alice Johnson",
                             rank=Rank.officer,
                             age=26,
                             specialization="Engineering",
                             years_experience=6)
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2026, 4, 10, 1, 10),
            duration_days=900,
            crew=[member1, member2],
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print("Mission:", mission.mission_name)
        print("ID:", mission.mission_id)
        print("Destination:", mission.destination)
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print("Crew size:", len(mission.crew))
        print("Crew members:")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank.value}) - {member.specialization}")
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]['msg'].removeprefix("Value error, "))


if __name__ == "__main__":
    main()
