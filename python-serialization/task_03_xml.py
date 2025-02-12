#!/usr/bin/python3
"""task_03_xml.py"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    serialize the dictionary into XML and save it to the given filename
    """

    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = value

    tree = ET.ElementTree(root)

    try:
        tree.write(filename)

    except Exception as e:
        print("Error during serialization: {}".format(e))
        return None


def deserialize_from_xml(filename):
    """
    read the XML data from that file,
    and return a deserialized Python dictionary.
    """

    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        dictionnary = {}

        for child in root:
            dictionnary[child.tag] = child.text

        return dictionnary

    except Exception as e:
        print("Error during deserialization: {}".format(e))
