import xml.etree.ElementTree
import sys

# Parse
xml_person = xml.etree.ElementTree.parse(sys.argv[1])

# Get root element
e = xml_person.getroot()

# Get a certain child
friends = e.find("friends")

# Get attribute tuples (everything is a string)
for f in friends.getchildren():
    print(f.text)

# Iterate over child elements
scores = e.find("scores")
for score in scores.getchildren():
    print(score.get("id"), score.text)

