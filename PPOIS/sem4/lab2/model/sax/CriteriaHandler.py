import xml.sax
from controller.SearchCriteria import SearchCriteria


class CriteriaHandler(xml.sax.ContentHandler):
    def __init__(self, search_criteria: SearchCriteria):
        self.players = []
        self.current_player = {}
        self.current_tag = ""
        self.search_criteria = search_criteria

    def startElement(self, tag, attrs):
        self.current_tag = tag
        if tag == "soccer_player":
            self.current_player = {}

    def endElement(self, tag):
        if tag == "soccer_player":
            match self.search_criteria.criteria:
                case "name and birthdate":
                    if self.search_criteria.name and self.current_player["full_name"] \
                            and self.search_criteria.name in self.current_player["full_name"]:
                        if self.search_criteria.birth_date and self.current_player["birth_date"] \
                            and self.search_criteria.birth_date == self.current_player["birth_date"]:
                            self.players.append(self.current_player)
                            return
                case "position":
                    if self.search_criteria.position and self.current_player["position"] \
                        and self.search_criteria.position == self.current_player["position"]:
                        self.players.append(self.current_player)
                        return
                case  "squad":
                    if self.search_criteria.squad and self.current_player["squad"] \
                            and self.search_criteria.squad == self.current_player["squad"]:
                        self.players.append(self.current_player)
                        return
                case "soccer team":
                    if self.search_criteria.soccer_team and self.current_player["soccer_team"] \
                            and self.search_criteria.soccer_team == self.current_player["soccer_team"]:
                        self.players.append(self.current_player)
                        return
                case "home town":
                    if self.search_criteria.home_town and self.current_player["home_town"] \
                            and self.search_criteria.home_town == self.current_player["home_town"]:
                        self.players.append(self.current_player)
                        return
        self.current_tag = ""

    def characters(self, content):
        if self.current_tag:
            if self.current_tag == "full_name":
                self.current_player["full_name"] = content
            elif self.current_tag == "birth_date":
                self.current_player["birth_date"] = content
            elif self.current_tag == "soccer_team":
                self.current_player["soccer_team"] = content
            elif self.current_tag == "home_town":
                self.current_player["home_town"] = content
            elif self.current_tag == "squad":
                self.current_player["squad"] = content
            elif self.current_tag == "position":
                self.current_player["position"] = content

    def endDocument(self):
        print('parsing process success')
        return self.players

