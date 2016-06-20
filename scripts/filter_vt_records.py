import ijson, csv
with open(r"c:\temp\irs990\output.csv", "w", newline = '') as o:
    dataWriter = csv.writer(o,delimiter=',', quoting=csv.QUOTE_MINIMAL)
    dataWriter.writerow(['NAME','URL'])
    with open("index.json") as f:
        parser = ijson.parse(f)
        obj = {}
        for prefix, event, value in parser:
            if prefix == 'AllFilings.item.URL' and len(value)>0:
                obj = {'url':value}
            if prefix == 'AllFilings.item.OrganizationName':
                if "VERMONT" in valueor "VT " in value or " VT " in value:
                    obj['name'] = value
                    #print(obj)
                    dataWriter.writerow([obj['name'].strip(),obj['url'].replace("\\n","")])
