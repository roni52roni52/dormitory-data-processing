from abc import ABC, abstractmethod


class Exporter(ABC):
    @abstractmethod
    def export(self, data, file_path):
        # Export data to the selected format
        pass