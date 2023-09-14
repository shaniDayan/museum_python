from datetime import datetime
from ArtifactCatalog import ArtifactCatalog


def check_values(types):
    name, start_day, end_date = types
    format = "%Y-%m-%d"
    if type(name) is not str:
        raise ValueError("Name needs to be string")
    if not datetime.strptime(start_day, format) or not datetime.strptime(end_date, format):
        raise ValueError("Dates need to be in format of YYYY-MM-DD")


class Exhibition:
    def __init__(self, name, start_day, end_date):
        types = (name, start_day, end_date)
        check_values(types)
        self.name = name
        self.start_day = start_day
        self.end_date = end_date
        self.catalog = ArtifactCatalog
        self.articat_list = []

    def addCatalog(self, catalog):
        self.catalog = catalog

    def add_artifact_to_display(self, artifact_id):
        self.articat_list.append(self.catalog.find_artifacts_by_id(artifact_id))


    def remove_artifact_from_display(self,artifact_id):
        self.articat_list.remove(self.catalog.find_artifacts_by_id(artifact_id))
    def print_display(self):
        for art in self.articat_list:
            print(art)

    def get_duration(self):
        start_year, start_month, start_day = self.start_day.split("-")
        end_year, end_month, end_day = self.end_date.split("-")
        return (int(end_year)-int(start_year))*360 + (int(end_month)-int(start_month))*30 +(int(end_day)-int(start_day))

