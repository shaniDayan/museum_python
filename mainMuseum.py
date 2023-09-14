from Artifact import Artifact
from ArtifactCatalog import ArtifactCatalog, load_catalog_to_json
from Exhibition import Exhibition


def main():
    a = Artifact(1, "one", "shani", 2001, 4000.6)
    b = Artifact(2, "two", "tal", 2002, 3000.0)
    c = Artifact(3, "three", "shani", 2006, 5555.5)
    d = Artifact(4, "four", "david", 1980, 6000.89)
    e = Artifact(5, "five", "tal", 2009, 2568.0)
    catalog = ArtifactCatalog()
    catalog.add_artifact(a)
    catalog.add_artifact(b)
    catalog.add_artifact(c)
    catalog.add_artifact(d)
    catalog.add_artifact(e)
    exhibition = Exhibition("Shani's ART", "2023-09-01", "2023-09-13")
    exhibition.addCatalog(catalog)
    exhibition.add_artifact_to_display(1)
    exhibition.add_artifact_to_display(2)
    exhibition.add_artifact_to_display(3)
    exhibition.remove_artifact_from_display(3)
    load_catalog_to_json('C:\\Users\\shani\\PycharmProjects\\pythonProject\\museum\\jsonCatalog.json', catalog)


if __name__ == "__main__":
    main()
