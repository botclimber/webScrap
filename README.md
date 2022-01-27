# webScrap

web scrapping program for all powered by standvirtual pages.
it generates a .json and .csv file with the desired data.

edit params.json file to change requested data.

Installation:
to use this application just install the requirements:

```
pip3 install -r requirementes.txt
```

use:
```
scrapy crawl spy -O ../data/data.json -a url=https://ruisilauto.standvirtual.com/shop/?fbclid=IwAR27DajBHVEurxsXUb_JuR95As8EoJ6pADjnZ1tA-xGobouMq1UxCt1txI4
```

- **-O** param:
	- replace existing file 
- **-o** param:
	- append to existing file
- **-a url= (...)**:
	- generic param point to the desired page


to get the .csv file go to the root dir and run the following command:
```
python3 jsontocsv.py data/data.json
```

- data/data.json is the file to be converted 

TODO:
- Convert data.json to .csv
	- [x] try to fin dsome lib to convert it otherwise write one 
	- [x] extract detailed info from title param, atleast brand and year
	- [x] make generic params def jsontocsv 
	
	- [ ] create lib/package for jsontocsv func 
	- [ ] for prod purpose erase 3 pages limitation 	
