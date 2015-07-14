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

Limitations:
Can not go through Excel workbooks (.xls files) as of yet (working on it). Also, the way it finds IPs is rather inefficient, but it gets the job done.
