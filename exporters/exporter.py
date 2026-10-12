from abc import ABC, abstractmethod


class Exporter(ABC):
    @abstractmethod
    def export(self, data: dict, file_path: str) -> None:
        # Export data to the selected format
        pass