import opml
import sys

from xml.etree import ElementTree

with open('Feedly.opml', 'rt') as f:
    tree = ElementTree.parse(f)

for node in tree.iter('outline'):
    url = node.attrib.get('xmlUrl')
    if url:
        print('  %s' % (url))


