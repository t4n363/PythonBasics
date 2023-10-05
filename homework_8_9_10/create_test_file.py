import json
import xml.etree.ElementTree as ET

# Generate test data
data = [
    {
        "type": "News",
        "text": "This is a news article.",
        "city": "New York",
        "expiration": "2023-12-31"
    },
    {
        "type": "Advertisement",
        "text": "Buy one, get one free!",
        "city": "",
        "expiration": "2023-11-30"
    },
    {
        "type": "Joke",
        "text": "Why did the chicken cross the road? To get to the other side!",
        "city": "None",
        "expiration": "2023-10-15"
    }
]

# Save as JSON
with open("input_news_feed.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

# Save as XML
root = ET.Element("publications")

for item in data:
    publication = ET.SubElement(root, "publication")
    
    type_elem = ET.SubElement(publication, "type")
    type_elem.text = item["type"]
    
    text_elem = ET.SubElement(publication, "text")
    text_elem.text = item["text"]
    
    city_elem = ET.SubElement(publication, "city")
    city_elem.text = item["city"]
    
    expiration_elem = ET.SubElement(publication, "expiration")
    expiration_elem.text = item["expiration"]

tree = ET.ElementTree(root)
tree.write("input_news_feed.xml")
