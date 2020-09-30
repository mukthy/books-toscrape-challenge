# books-toscrape-challenge

1. Install Scrapy module.

```
sudo pip install scrapy
```

2. To run the project, execute the below commands.

```
git clone https://github.com/mukthy/books-toscrape-challenge.git
cd books-toscrape-challenge
scrapy runspider books-toscrape.py
```

3. To Export the output to a csv file, execute the below command.

```
scrapy runspider books-toscrape.py -o filename.csv
```

I have uploaded the output of the website http://books.toscrape.com/ in a CSV format.

It contains the following fields : 

```
Book URL

Book Price

Book Image URL

Book Title
```
##Start

![alt text](https://github.com/mukthy/books-toscrape-challenge/blob/master/start.png)

##End

![alt text](https://github.com/mukthy/books-toscrape-challenge/blob/master/end.png)