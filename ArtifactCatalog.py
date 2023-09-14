import json


class ArtifactCatalog:
    def __init__(self):
        self.catalog = {}

    def add_artifact(self, artifact):
        self.catalog[artifact.id] = artifact

    def find_artifacts_by_artist(self, artist):
        return [self.catalog[id].name for id in self.catalog.keys() if self.catalog[id].artist == artist]

    def find_artifacts_by_id(self, artifact_id):
        if id not in self.catalog.keys():
            return self.catalog[artifact_id]
        raise KeyError()

    def calculate_total_value(self):
        return sum([self.catalog[id].value for id in self.catalog.keys()])

    def get_oldest_artifact(self):
        return min([self.catalog[id].year for id in self.catalog.keys()])

    def remove_artifact(self, artifact_id):
        del self.catalog[artifact_id]


def load_catalog_from_json(filename):
    pass


def make_dict(item):
    dict_item = {'id': item.id, 'name': item.name, 'artist': item.artist, 'year': item.year, 'value': item.value}
    return dict_item


def load_catalog_to_json(filename, artifact_catalog):
    dict_list_catalog = [make_dict(artifact_catalog.catalog[id]) for id in artifact_catalog.catalog.keys()]
    with open(filename, 'w') as f:
        json.dumps(dict_list_catalog)
