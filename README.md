# webScrap
Standvirtual powered by web scrapping.

Web scrap for standvirtual powered by websites.
It is made in a generic way just copy the url u want to scrap ex (https://ruisilauto.standvirtual.com/shop/?fbclid=IwAR27DajBHVEurxsXUb_JuR95As8EoJ6pADjnZ1tA-xGobouMq1UxCt1txI4&page=2) and then run the following command:

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
	- create lib/package for jsontocsv func []
