import xml.etree.ElementTree as ET

# https://digi.kansalliskirjasto.fi/aikakausi/titles/0355-0257?year=1841
# yksi alto on yksi sivu
# teksti on jäsennelty kappaleisiin
# sanat on eroteltu <sp> tageilla
# halutaan ainakin issn, lehden nimi, vuosi, teksti, lehden numero
def get_text_from_xml(path):
    tree = ET.parse(path)
    root = tree.getroot()

    text_parts = []
    for block in root.iter('TextBlock'):
        for node in block:
            for element in node:
                if element.tag == "SP":
                    text_parts.append(" ")
                elif element.tag == "String":
                    text_parts.append(element.get("CONTENT", ""))

    final_text = "".join(text_parts) + "\n"
    return final_text

