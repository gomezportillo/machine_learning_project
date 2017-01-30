import xml.dom.minidom

xml = xml.dom.minidom.parse('data/datos2007.xml') # or xml.dom.minidom.parseString(xml_string)
pretty_xml_as_string = xml.toprettyxml()

with open('data/datos2007_pretty.xml', 'w') as f:
    f.write(pretty_xml_as_string)
