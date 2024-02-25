import xml.etree.ElementTree as ET


def edit_xml_file():
    tree = ET.parse("./datasets/persons.xml")

    root = tree.getroot()
    for child in root:
        name = child.find("name").text
        age = child.find("age").text
        city = child.find("city").text
        food = child.find("food").text
        # print(f"{name}さん {age}歳 {city}出身 好きな食べ物は{food}")
        if city == "青森県":
            child.find("food").text = "りんご"

    new_tree = ET.ElementTree(root)
    new_tree.write(
        "./datasets/output_persons.xml", encoding="utf-8", xml_declaration=True
    )


if __name__ == "__main__":
    edit_xml_file()
