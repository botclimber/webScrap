#!/bin/sh

RUISILAUTO="https://ruisilauto.standvirtual.com/" 
BIREDA="https://bireda.standvirtual.com/"
MIGUEL9001="https://miguel9001.standvirtual.com/"
MEGAPECASLDA="https://megapecaslda.standvirtual.com/"
PECAS="https://pecas.standvirtual.com/"
SERVECARROS="https://servecarros.standvirtual.com/"
AVFPECAS="https://avfpecas.standvirtual.com/"
JESUSEBAPTISTA="https://jesusebaptista.standvirtual.com/"
QUALIPECASLDA="https://qualipecaslda.standvirtual.com/"
RAUTO1="https://rauto1.standvirtual.com/"
JAFCMLS="https://jafcmls.standvirtual.com/"
YMCSAUTOPECAS="https://ymcsautopecas.standvirtual.com/"
AUTOPECASANHA="https://autopecasanha.standvirtual.com/"


echo "Moving dir"
cd ../stdv
echo "Strating download ..."
scrapy crawl spy -a url=$RUISILAUTO -O ../data/data.csv && 
scrapy crawl spy -a url=$BIREDA -o ../data/data.csv &&
scrapy crawl spy -a url=$MIGUEL9001 -o ../data/data.csv &&
scrapy crawl spy -a url=$MEGAPECASLDA -o ../data/data.csv &&
scrapy crawl spy -a url=$PECAS -o ../data/data.csv &&
scrapy crawl spy -a url=$SERVECARROS -o ../data/data.csv &&
scrapy crawl spy -a url=$AVFPECAS -o ../data/data.csv &&
scrapy crawl spy -a url=$JESUSEBAPTISTA -o ../data/data.csv &&
scrapy crawl spy -a url=$QUALIPECASLDA -o ../data/data.csv &&
scrapy crawl spy -a url=$RAUTO1 -o ../data/data.csv &&
scrapy crawl spy -a url=$JAFCMLS -o ../data/data.csv &&
scrapy crawl spy -a url=$YMCSAUTOPECAS -o ../data/data.csv &&
scrapy crawl spy -a url=$AUTOPECASANHA -o ../data/data.csv 
echo "all complete"
