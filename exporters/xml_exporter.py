import xml.etree.ElementTree as ET

from exporters.exporter import Exporter


class XmlExporter(Exporter):
    def export(self, data: dict, file_path: str) -> None:
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

    def _convert_value(self, value: object) -> str:
        # Convert database values to text used by XML
        return str(value)