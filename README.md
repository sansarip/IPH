# IPHunter
Looking to find IPs (public and/or private) in a document containing mixed data?

This tool may benefit you. 

How do you run it?
Feed the file you want IPH to hunt through. Specify whether you want IPH to find private IPs, public IPs, or both. Designate an output file for IPH.

Flags:
-p (gets only private IPs)
-u (gets only public IPs)
-pu (gets both public and private IPs)
-i (input file)
-o (output file)

Example:
python IPH.py -i file.csv -p -o file.csv 

Limitations:
Can not go through Excel workbooks as of yet. Also, the way it finds IPs is rather inefficient, but it gets the job done. Working on making it a better tool.
