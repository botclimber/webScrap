#!/bin/sh
echo "SITE TO SCRAP: "
read SITE
echo "Moving dir"
cd ../stdv
echo "Strating download ..."
scrapy crawl spy -O ../data/data.json -a url=$SITE
echo "starting converting ..."
cd ..
python jsontocsv.py data/data.json
echo "all complete"

