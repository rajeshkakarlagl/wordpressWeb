import csv
import xml.etree.ElementTree as ET

def parse_wordpress_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    namespace = {'wp': 'http://wordpress.org/export/1.2/', 'dc': 'http://purl.org/dc/elements/1.1/'}

    items = root.findall('.//item', namespace)

    pages = []
    for item in items:
        title = item.find('title').text
        link = item.find('link').text
        content = item.find('{http://purl.org/rss/1.0/modules/content/}encoded').text
        author = item.find('dc:creator', namespace).text
        date = item.find('wp:post_date', namespace).text

        page = {
            'title': title,
            'link': link,
            'content': content,
            'author': author,
            'date': date
        }
        pages.append(page)

    return pages

def write_output_csv(pages, file_path):
    with open(file_path, 'w', newline='') as file:
        fieldnames = ['title', 'link', 'content', 'author', 'date']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for page in pages:
            writer.writerow(page)

# Replace these with the path to your WordPress XML file and the desired output CSV file path
wordpress_xml_path = r'C:\Users\kakarla.rajesh\Downloads\AEM-Migration-Script-master\handytool.wordpress.2024-05-09.000.xml'
output_csv_path = r'C:\Users\kakarla.rajesh\Downloads\AEM-Migration-Script-master\output.csv'

pages = parse_wordpress_xml(wordpress_xml_path)
write_output_csv(pages, output_csv_path)
