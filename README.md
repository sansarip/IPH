# IPHunter
Looking to find IPs (public and/or private) in a document containing mixed data?

This tool may benefit you. 

How do you run it?
Feed the file you want IPH to hunt through. Specify whether you want IPH to find private IPs, public IPs, or both. Designate an output file for IPH.

Flags:
_____________________________________________________________________________________________________________________________
-p (gets only private IPs)
_____________________________________________________________________________________________________________________________
-u (gets only public IPs)
_____________________________________________________________________________________________________________________________
-pu (gets both public and private IPs)
_____________________________________________________________________________________________________________________________
-i (input file)
_____________________________________________________________________________________________________________________________
-o (output file)
_____________________________________________________________________________________________________________________________

Example:
python IPH.py -i file.csv -p -o file.csv 

Update 7.16.2015:
This tool now accepts Excel workbook files. In order to have this feature work, you must install the xlrd library. Installation of the library can be found on page 5 of this pdf document: http://www.simplistix.co.uk/presentations/python-excel.pdf

If installed correctly, then the IPH file will import it by itself.

Note:
It can read Excel workbook files, but it CAN'T write Excel files. So, you can gather IP addresses from multiple sheets of a workbook without turning each sheet into a csv file to do so, and then you can output all IPs you've gathered into a single file such as a csv file.
