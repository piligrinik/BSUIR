import xml.sax
from .SoccerPlayer import SoccerPlayer
from .sax.MainHandler import MainHandler
from xml.dom.minidom import *
from .sax.CriteriaHandler import CriteriaHandler
from controller.SearchCriteria import SearchCriteria

class FileProcessor():
    def __init__(self, file):
        self.file = file

    def __creation(self):
        doc: Document = getDOMImplementation().createDocument(None, 'players', None)
        self._save_doc(doc)

    def doc_update(self, doc):
        with open(self.file, 'w') as file:
            file.write(doc.toxml())

    def get_players_from_file(self) -> list[SoccerPlayer]:
        handler = MainHandler()
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        parser.parse(self.file)
        players_dict: list[dict] = handler.players
        players_list: list[SoccerPlayer] = []

        for player in players_dict:
            players_list.append(SoccerPlayer(player['full_name'], player['birth_date'], player['soccer_team'],
                                             player['home_town'], player['squad'], player['position']))

        return players_list

    def get_players_by_criteria(self, criteria: SearchCriteria):
        handler = CriteriaHandler(criteria)
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        parser.parse(self.file)
        pickled_players_dict: list[dict] = handler.players
        pickled_players_list: list[SoccerPlayer] = []

        for player in pickled_players_dict:
            pickled_players_list.append(SoccerPlayer(player['full_name'], player['birth_date'], player['soccer_team'],
                                             player['home_town'], player['squad'], player['position']))

        return pickled_players_list

    def find_player(self, full_name, birth_date, soccer_team, home_town, squad, position):
        for player in self.get_players_from_file():
            if(player.get_full_name() == full_name and player.get_birth_date() == birth_date and
                    player.get_soccer_team() == soccer_team and player.get_home_town() == home_town and
                    player.get_position() == position and player.get_squad() == squad):
                return True

        return False

    def add_player(self, full_name, birth_date, soccer_team, home_town, squad, position):
        doc = parse(self.file)
        soccer_player = doc.createElement('soccer_player')
        att_full_name = doc.createElement('full_name')
        att_full_name.appendChild(doc.createTextNode(str(full_name)))
        soccer_player.appendChild(att_full_name)

        att_birth_date = doc.createElement('birth_date')
        att_birth_date.appendChild(doc.createTextNode(str(birth_date)))
        soccer_player.appendChild(att_birth_date)

        att_soccer_team = doc.createElement('soccer_team')
        att_soccer_team.appendChild(doc.createTextNode(str(soccer_team)))
        soccer_player.appendChild(att_soccer_team)

        att_home_town = doc.createElement('home_town')
        att_home_town.appendChild(doc.createTextNode(str(home_town)))
        soccer_player.appendChild(att_home_town)

        att_squad = doc.createElement('squad')
        att_squad.appendChild(doc.createTextNode(str(squad)))
        soccer_player.appendChild(att_squad)

        att_position = doc.createElement('position')
        att_position.appendChild(doc.createTextNode(str(position)))
        soccer_player.appendChild(att_position)



        players = doc.getElementsByTagName('soccer_players')[0]
        players.appendChild(soccer_player)

        self.doc_update(doc)

    def delete_players(self, search: SearchCriteria):
        doc = parse(self.file)
        deleted_count: int = 0
        soccer_players = doc.getElementsByTagName('soccer_player')
        for player in soccer_players:
            match search.criteria:
                case "name and birthdate":
                    if (search.name in player.getElementsByTagName('full_name')[0].firstChild.data and
                            search.birth_date == player.getElementsByTagName('birth_date')[0].firstChild.data):
                        parent = player.parentNode
                        parent.removeChild(player)
                        self.doc_update(doc)
                        deleted_count += 1
                case "position":
                    if search.position == player.getElementsByTagName('position')[0].firstChild.data:
                        parent = player.parentNode
                        parent.removeChild(player)
                        self.doc_update(doc)
                        deleted_count += 1
                case "squad":
                    if search.squad == player.getElementsByTagName('squad')[0].firstChild.data:
                        parent = player.parentNode
                        parent.removeChild(player)
                        self.doc_update(doc)
                        deleted_count += 1
                case "soccer team":
                    if search.soccer_team == player.getElementsByTagName('soccer_team')[0].firstChild.data:
                        parent = player.parentNode
                        parent.removeChild(player)
                        self.doc_update(doc)
                        deleted_count += 1
                case "home town":
                    if search.home_town == player.getElementsByTagName('home_town')[0].firstChild.data:
                        parent = player.parentNode
                        parent.removeChild(player)
                        self.doc_update(doc)
                        deleted_count += 1
        return deleted_count
