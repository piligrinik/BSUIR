from typing import Optional
from datetime import datetime


class SearchCriteria:
    def __init__(self, name: Optional[str] = None, birth_date: Optional[datetime] = None, position: Optional[str] = None,
                 squad: Optional[str] = None, soccer_team: Optional[str] = None, home_town: Optional[str] = None,
                 criteria: str | None = None):
        self.name = name
        self.birth_date = birth_date
        self.position = position
        self.squad = squad
        self.soccer_team = soccer_team
        self.home_town = home_town
        self.criteria = criteria
