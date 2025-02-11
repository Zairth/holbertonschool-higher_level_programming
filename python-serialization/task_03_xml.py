#!/usr/bin/python3
"""task_03_xml.py"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    serialize the dictionary into XML and save it to the given filename
    """

    pass


def deserialize_from_xml(filename):
    """
    read the XML data from that file,
    and return a deserialized Python dictionary.
    """

    pass


def main():
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)


if __name__ == "__main__":
    main()
