import xml.etree.ElementTree as ET
from decimal import Decimal

from exporters.exporter import Exporter


class XmlExporter(Exporter):
    def export(self, data, file_path):
        # Create the root XML element
        root = ET.Element("results")

        # Add every query result to the XML document
        for section_name, records in data.items():
            section = ET.SubElement(root, section_name)

            for record in records:
                item = ET.SubElement(section, "room")

                for key, value in record.items():
                    element = ET.SubElement(item, key)
                    element.text = self._convert_value(value)

        # Create and save the XML document
        tree = ET.ElementTree(root)
        ET.indent(tree, space="    ")
        tree.write(
            file_path,
            encoding="utf-8",
            xml_declaration=True,
        )

    @staticmethod
    def _convert_value(value):
        # Convert database values to text used by XML
        if isinstance(value, Decimal):
            return str(value)

        return str(value)