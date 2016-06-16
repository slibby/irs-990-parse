import ijson, csv
o = open(r"output.csv", "w")
writer = csv.writer(o)
writer.writerow("NAME,URL\n")
with open(r"index.json") as f:
    parser = ijson.parse(f)
    count = 0
    obj = {}
    for prefix, event, value in parser:
        #print (prefix, event, value)
        count +=1
        #print(prefix, value)
        if count > 500000: break
        if prefix == 'AllFilings.item.URL' and len(value)>0:
            obj = {'url':value}
        if prefix == 'AllFilings.item.OrganizationName':
            if "VERMONT" in value:
                obj['name'] = value
                print(obj)
                writer.writerow(",".join(obj['name'],obj['url']))
    print(count)
