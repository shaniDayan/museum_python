**Question:**

**Scenario:**
You are hired by a prestigious museum to develop a Python program for cataloging and managing their valuable artifact collection. The museum's artifacts include rare historical items, artworks, and archaeological finds. Your task is to create an advanced system that can handle various aspects of artifact management efficiently.

**Task 1: Classes and Dictionaries**

Create three classes: `Artifact`, `ArtifactCatalog`, and `Exhibition`. Each class has specific responsibilities:

**a) `Artifact` Class:**

Create a class called `Artifact` to represent individual artifacts. Each artifact should have the following attributes:

- `id` (integer): A unique identifier for the artifact.
- `name` (string): The name or title of the artifact.
- `artist` (string): The name of the artist or creator.
- `year` (integer): The year the artifact was created or discovered.
- `value` (float): The estimated value of the artifact.

In addition to the attributes, implement the following methods for the `Artifact` class:

- `__init__(self, id, name, artist, year, value)`: Initializes a new artifact object with the provided attributes.
- `__str__(self)`: Returns a string representation of the artifact in the format "ID: [id], Name: [name], Artist: [artist], Year: [year], Value: [value]".
- `set_value(self, new_value)`: Updates the estimated value of the artifact.
- `get_age(self, current_year)`: Returns the age of the artifact by subtracting its creation year from the current year.

**b) `ArtifactCatalog` Class:**

Create a class called `ArtifactCatalog` to manage the museum's artifact collection. This class should have the following attributes:

- `artifacts` (dictionary): A dictionary to store `Artifact` objects, where the keys are the artifact IDs.

Implement the following methods for the `ArtifactCatalog` class:

- `__init__(self)`: Initializes an empty catalog.
- `add_artifact(self, artifact)`: Adds an `Artifact` object to the catalog with its ID as the key.
- `find_artifacts_by_artist(self, artist)`: Returns a list of artifact names created by a specific artist.
- `calculate_total_value(self)`: Returns the total estimated value of all artifacts in the catalog.
- `get_oldest_artifact(self)`: Returns the `Artifact` object representing the oldest artifact in the catalog.
- `remove_artifact(self, artifact_id)`: Removes an artifact from the catalog by its ID.

**c) `Exhibition` Class:**

Create a class called `Exhibition` to manage museum exhibitions. This class should have the following attributes:

- `name` (string): The name or title of the exhibition.
- `start_date` (string): The start date of the exhibition in the format "YYYY-MM-DD".
- `end_date` (string): The end date of the exhibition in the format "YYYY-MM-DD".
- `artifacts_on_display` (list): A list of artifact IDs that are currently on display in the exhibition.

Implement the following methods for the `Exhibition` class:

- `__init__(self, name, start_date, end_date)`: Initializes a new exhibition with the provided attributes.
- `add_artifact_to_display(self, artifact_id)`: Adds an artifact to the list of artifacts on display.
- `remove_artifact_from_display(self, artifact_id)`: Removes an artifact from the list of artifacts on display.
- `get_duration(self)`: Returns the duration of the exhibition in days.

**Task 2: JSON Files and Exceptions**

Create a function called `load_catalog_from_json(filename)` outside of the `ArtifactCatalog` class. This function should load the museum's artifact catalog from a JSON file and return it as a dictionary with artifact IDs as keys. If the file does not exist or the JSON data is malformed, raise appropriate exceptions.

**Task 3: Main Function with User Input**

Implement a `main()` function that takes user input arguments and performs the following actions based on the user's choice:

- Add artifacts to the catalog.
- Assign artifacts to exhibitions.
- Calculate the total value of artifacts.
- Find the oldest artifact.
- Save the catalog to a JSON file.
- Load the catalog from a JSON file.

Use command-line arguments provided by the user to determine the action to be taken. Utilize list comprehensions in your code where applicable.

Your task is to:

1. Implement the `Artifact`, `ArtifactCatalog`, and `Exhibition` classes as described in Task 1.
2. Implement the `load_catalog_from_json` function as described in Task 2.
3. Create a `main()` function as described in Task 3.

Write a Python program that demonstrates the usage of these classes and functions. The program should interact with the user through the command line, and the user's input should determine which actions are performed on the artifact catalog. Handle any exceptions that may occur during this process.

Your program should also include comments to explain the purpose of each class, method, and function.

---

This enhanced question includes a `main()` function that interacts with the user through command-line arguments and allows them to perform various actions on the artifact catalog. It also incorporates list comprehensions where applicable to demonstrate the candidate's proficiency in Python programming.