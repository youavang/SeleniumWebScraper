from Request_modified import Grab_Info
import requests
import json
import csv
import datetime
import pprint as pp
#import psycopg2
isbn_num = []
#check = []


donations = csv.reader(open('C:/Users/ftayl/Desktop/OFR/Projects/Database/genreNTBF2021-06-06.csv', encoding="utf-8"))
for num in donations:
    isbn_num.append(num[0])
    isbn = num[0]



#isbn_num = ['9780140328721', '9789500415842']



ofile = open('/Users/ftayl/Desktop/OFR/Projects/Database/book_upload '+ str(datetime.date.today()) +'.csv', "w", newline = "", encoding = "utf-8")
headers = csv.DictWriter(ofile, fieldnames= ['ISBN', 'Title', 'Author', 'Genres'], delimiter = ',')
headers.writeheader()
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
ISBN = isbn
Title = ''
Author = ''
Genre = ''

for isbn in isbn_num:
    ISBN = isbn
    #Title = ''
    #Author = ''
    #Genre = ''
    #check = []

    try:
        check = []
        response = requests.get('https://openlibrary.org/api/books?bibkeys=ISBN:' + isbn + '&jscmd=data&format=json')
        response_json = json.loads(response.text)
        check.append(response_json)
        

        #pp.pprint(response_json)


        #print(response_json)
        #print(check)


        Grab_Info = response_json['ISBN:' + isbn]
        
        Title = Grab_Info.get('title')
        
        Author_get = Grab_Info['authors']
        for i in Author_get:
            Author = i['name']
        #Author = Author_search.get('name')
            #print(Author)
        
        Genre_get = Grab_Info.get('subjects')
        for dic in Genre_get:
            Genres = dic['name']
        #print(Genres)

        
    except TypeError:
        ISBN = isbn
        Title = Grab_Info.get('title')
        #print(Title)
        Author_get = Grab_Info['authors']
        for i in Author_get:
            Author = i['name']
        Genres = 'To be found'
        
        
    except KeyError:
        ISBN = isbn
        Title = 'To be found'
        Author = 'To be found'
        Genres = 'To be found'
    #    for dic in Genre_get:
    #        Genres.append(dic['name'])

    row = [ISBN, Title, Author, Genres]
    writer.writerow(row)
    print(row)



ofile.close()