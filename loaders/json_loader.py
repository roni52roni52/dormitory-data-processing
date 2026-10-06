import json


class JsonLoader:
    def load(self, file_path):
        # Open the JSON file and return its contents as Python objects
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)