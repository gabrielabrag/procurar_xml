from xml.dom import minidom

with open("evtCadDeclarante.xml",'r') as f:
    xml= minidom.parse(f)
    nome= xml.getElementsByTagName("nome")

    for tag in nome:
        print(tag.firstChild.data)