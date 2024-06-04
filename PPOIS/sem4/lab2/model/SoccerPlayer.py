from datetime import datetime


class SoccerPlayer:
    def __init__(self, full_name, birth_date, soccer_team, home_town, squad, position):
        self.full_name = full_name
        self.soccer_team = soccer_team
        self.home_town = home_town
        self.squad = squad
        self.position = position

        try:
            self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("It appears, you entered invalid date format. Please enter a date in the format YYYY-MM-DD.")

    def get_player_info(self):
        return (
            self.full_name,
            self.birth_date.strftime("%Y-%m-%d"),
            self.soccer_team,
            self.home_town,
            self.squad,
            self.position
        )

    def get_full_name(self):
        return self.full_name

    def get_birth_date(self):
        return self.birth_date

    def get_soccer_team(self):
        return self.soccer_team

    def get_home_town(self):
        return self.home_town

    def get_squad(self):
        return self.squad

    def get_position(self):
        return self.position

