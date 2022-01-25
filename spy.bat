ECHO Starting Spy
ECHO Starting environment ...
call venv/Scripts/activate.bat
cd stdv
ECHO Environment set 
ECHO Downloading Data ...
scrapy crawl spy -O ../data/data.json -a url=https://ruisilauto.standvirtual.com/shop/?fbclid=IwAR27DajBHVEurxsXUb_JuR95As8EoJ6pADjnZ1tA-xGobouMq1UxCt1txI4
ECHO Data downloaded, file created
ECHO Converting json data to csv
cd ..
python jsontocsv.py data/data.json
call venv/Scripts/deactivate.bat
ECHO All done successufully
PAUSE