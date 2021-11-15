from urllib import request
from toml import loads
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)
        p_inf = loads(content)["tool"]["poetry"]
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(p_inf["name"], p_inf["description"],p_inf["dependencies"], p_inf["dev-dependencies"])
