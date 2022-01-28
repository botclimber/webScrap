# webScrap

web scrapping program for all powered by standvirtual pages.
it generates a .json and .csv file with the desired data.

edit params.json file to change requested data.

Installation:

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
