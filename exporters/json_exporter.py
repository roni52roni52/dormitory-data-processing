import json
from decimal import Decimal

from exporters.exporter import Exporter


class JsonExporter(Exporter):
    def export(self, data, file_path):
        # Write query results to a JSON file
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
                default=self._convert_value,
            )

    @staticmethod
    def _convert_value(value):
        # Convert Decimal values returned by MySQL to float
        if isinstance(value, Decimal):
            return float(value)

        raise TypeError(
            f"Object of type {type(value).__name__} is not JSON serializable"
        )