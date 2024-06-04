import xml.sax


class MainHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.players = []
        self.current_player = {}
        self.current_tag = ""

    def startElement(self, tag, attrs):
        self.current_tag = tag
        if tag == "soccer_player":
            self.current_player = {}

    def endElement(self, tag):
        if tag == "soccer_player":
            self.players.append(self.current_player.copy())
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

