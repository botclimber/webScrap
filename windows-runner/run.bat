set RUISILAUTO=https://ruisilauto.standvirtual.com/
set BIREDA=https://bireda.standvirtual.com/
set MIGUEL9001=https://miguel9001.standvirtual.com/
set MEGAPECASLDA=https://megapecaslda.standvirtual.com/
set PECAS=https://pecas.standvirtual.com/
set SERVECARROS=https://servecarros.standvirtual.com/
set AVFPECAS=https://avfpecas.standvirtual.com/
set JESUSEBAPTISTA=https://jesusebaptista.standvirtual.com/
set QUALIPECASLDA=https://qualipecaslda.standvirtual.com/
set RAUTO1=https://rauto1.standvirtual.com/
set JAFCMLS=https://jafcmls.standvirtual.com/
set YMCSAUTOPECAS=https://ymcsautopecas.standvirtual.com/
set AUTOPECASANHA=https://autopecasanha.standvirtual.com/

echo "Moving dir"
cd ../stdv
echo "Starting download ..."
scrapy crawl spy -a url=%RUISILAUTO% -O ../data/data.csv
scrapy crawl spy -a url=%BIREDA% -o ../data/data.csv
scrapy crawl spy -a url=%MIGUEL9001% -o ../data/data.csv
scrapy crawl spy -a url=%MEGAPECASLDA% -o ../data/data.csv
scrapy crawl spy -a url=%PECAS% -o ../data/data.csv
scrapy crawl spy -a url=%SERVECARROS% -o ../data/data.csv
scrapy crawl spy -a url=%AVFPECAS% -o ../data/data.csv
scrapy crawl spy -a url=%JESUSEBAPTISTA% -o ../data/data.csv
scrapy crawl spy -a url=%QUALIPECASLDA% -o ../data/data.csv
scrapy crawl spy -a url=%RAUTO1% -o ../data/data.csv
scrapy crawl spy -a url=%JAFCMLS% -o ../data/data.csv
scrapy crawl spy -a url=%YMCSAUTOPECAS% -o ../data/data.csv
scrapy crawl spy -a url=%AUTOPECASANHA% -o ../data/data.csv 
echo "all complete"
PAUSE