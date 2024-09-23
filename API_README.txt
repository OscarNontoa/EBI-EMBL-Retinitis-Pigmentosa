Code >

This is a open source code

This script uses a URL to look for a specific query on UniProt
The URL is generated directly on UniProt

The response of UniProt for that specific URL is used as a .json file

From the .json file the primary accession number, the name of the protein, and
the comments of the entry

Finally, the information gathered is organized as a dataframe, and it is exported
as a .xlsx file

Python version: 3.8.10