# irs-990-parse: finding value in 3.5M Non-profit tax returns
This repository contains guidance and Python scripts for parsing IRS 990 releases in Amazon S3

to begin, you'll need the `index.json` file from the S3 bucket, it's 1GB so don't try it on a mobile tether :thumbsdown:
Install the AWS CLI and run the following command from your desired destination folder:
`aws s3 cp s3://irs-form-990/index.json index.json`

the CLI should download the file in parts for you, and you'll end up with a big, big JSON file.

The contents of this file are a list of objects contained within a top-level `AllFilings` tag, each similar to:
```
{
	"EIN": "270678774",
	"SubmittedOn": "2016-02-09",
	"TaxPeriod": "201509",
	"DLN": "93492308002265",
	"LastUpdated": "2016-03-21T17:23:53",
	"URL": "https://s3.amazonaws.com/irs-form-990/201513089349200226_public.xml",
	"FormType": "990EZ",
	"ObjectId": "201513089349200226",
	"OrganizationName": "KIWANIS CLUB OF GLENDORA PROJECTS FUND INC",
	"IsElectronic": true,
	"IsAvailable": true
}
```
Not all attributes are available in all objects, for example if `IsAvailable` is `false`, `URL` will not be present.

Parsing through the file in-memory is generally not possible, so a streaming approach can be used through the module **ijson**. To acquire **ijson**, run `pip install ijson` from your Python environment.

Some useful filtering options available for this large file are to search by `OrganizationName` and by `IsAvailable`. An example is provided in [filter_vt_records.py](scripts/filter-vt-records.py). This will parse the entire file and pull out any record containing the word "VERMONT", exporting it to a more manageable CSV:
[Sample Image](http://i.imgur.com/pBU8Jyc.png)
