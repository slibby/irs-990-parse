from lxml import etree
import os
for f in os.listdir("data"):
    tree = etree.parse(os.path.join("data",f))
    root = tree.getroot()
    for i in root[0]:
        if i.tag == "{http://www.irs.gov/efile}Filer":
            print(i[1][0].text)
            print(i[4][0].text)
            print(i[4][1].text)
            print(i[4][2].text)
    print("\n")
