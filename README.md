# webScrap

web scrapping program for all powered by standvirtual pages.
it generates a .json and .csv file with the desired data.

edit params.json file to change requested data.

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

in this case it will only get title, price and link to detail page

TODO:
- Convert data.json to .csv
	- try to fin dsome lib to convert it otherwise write one [x]
	- extract detailed info from title param, atleast brand and year[x]
	- make generic params def jsontocsv [x]
	
	- create lib/package for jsontocsv func [ ]
	- for prod purpose erase 3 pages limitation [ ]
	
