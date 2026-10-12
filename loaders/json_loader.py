import json


class JsonLoader:
    def load(self, file_path: str) -> list[dict]:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)