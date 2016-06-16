import csv, boto
conn = boto.connect_s3()
irs990 = conn.get_bucket('irs-form-990')
with open("vermont_filings.csv", "r") as csvfile:
    csvfile.readline()
    datareader = csv.reader(csvfile)
    for row in datareader:
        filename = row[1][row[1].rfind("/")+1:]
        k = irs990.get_key(filename)
        k.get_contents_to_filename(r"data\\{}".format(filename))
