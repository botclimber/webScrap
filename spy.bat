ECHO Starting Spy
cd stdv
ECHO Downloading Data ...
scrapy crawl spy -O ../data/data.json 
ECHO Data downloaded, file created
ECHO Converting json data to csv
cd ..
python jsontocsv.py data/data.json
ECHO All done successufully
PAUSE
