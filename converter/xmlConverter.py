import xml.etree.ElementTree as ET

def parse_wordpress_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    namespace = {'wp': 'http://wordpress.org/export/1.2/', 'dc': 'http://purl.org/dc/elements/1.1/'}
    items = root.findall('.//item', namespace)

    pages = ET.Element('pages')
    for item in items:
        page = ET.SubElement(pages, 'page')

        title = ET.SubElement(page, 'title')
        title.text = item.find('title').text

        link = ET.SubElement(page, 'link')
        link.text = item.find('link').text

        content = ET.SubElement(page, 'content')
        content.text = item.find('{http://purl.org/rss/1.0/modules/content/}encoded').text

        author = ET.SubElement(page, 'author')
        author.text = item.find('dc:creator', namespace).text

        date = ET.SubElement(page, 'date')
        date.text = item.find('wp:post_date', namespace).text

    return pages

def write_output_xml(pages, file_path):
    tree = ET.ElementTree(pages)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

# Replace these with the path to your WordPress XML file and the desired output XML file path
wordpress_xml_path = r'C:\Users\kakarla.rajesh\Downloads\AEM-Migration-Script-master\handytool.wordpress.2024-05-09.000.xml'
output_xml_path = r'C:\Users\kakarla.rajesh\Downloads\AEM-Migration-Script-master\output.xml'

pages = parse_wordpress_xml(wordpress_xml_path)
write_output_xml(pages, output_xml_path)
