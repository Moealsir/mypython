# import json
# import sqlite3

# con  = sqlite3.connect('roster.sqlite')
# cur = con.cursor()

# cur.executescript('''
# DROP TABLE IF EXISTS User;
# DROP TABLE IF EXISTS Member;
# DROP TABLE IF EXISTS Course;

# CREATE TABLE User (
#     id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name   TEXT UNIQUE
# );

# CREATE TABLE Course (
#     id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     title  TEXT UNIQUE
# );

# CREATE TABLE Member (
#     user_id     INTEGER,
#     course_id   INTEGER,
#     role        INTEGER,
#     PRIMARY KEY (user_id, course_id)
# )
# ''')


# js = json.loads(open('roster_data.json').read())
# for i in js:
#   name = i[0]
#   title = i[1]
#   role = i[2]

#   print('name :',name,'title :',title,'role :',role)


#   cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)',(name,))
#   cur.execute('SELECT  id FROM User WHERE name=?',(name,))
#   user_id = cur.fetchone()[0]

#   cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)',(title,))
#   cur.execute('SELECT  id FROM Course WHERE title=?',(title,))
#   course_id = cur.fetchone()[0]

#   cur.execute('INSERT OR IGNORE INTO Member (user_id,course_id,role) VALUES (?,?,?)',(user_id,course_id,role))

# # cur.executescript('''SELECT User.name,Course.title, Member.role FROM
# #     User JOIN Member JOIN Course    fix this and figure out how to use fetchone to print date
# #     ON User.id = Member.user_id AND Member.course_id = Course.id
# #     ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;''')
# # data = cur.fetchone()
# # print(data)


# con.commit()


# # SELECT User.name,Course.title, Member.role FROM
# #     User JOIN Member JOIN Course
# #     ON User.id = Member.user_id AND Member.course_id = Course.id
# #     ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;

# # SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM
# #     User JOIN Member JOIN Course
# #     ON User.id = Member.user_id AND Member.course_id = Course.id
# #     ORDER BY X LIMIT 1;


# import xml.etree.ElementTree as et
# import sqlite3

# con = sqlite3.connect('trackdbassment.sqlite')
# cur = con.cursor()
# cur.executescript('''

#  DROP TABLE IF EXISTS Artist;
#  DROP TABLE IF EXISTS Album;
#  DROP TABLE IF EXISTS Track;
#  DROP TABLE IF EXISTS Genre;


# CREATE TABLE Artist (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );

# CREATE TABLE Genre (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );

# CREATE TABLE Album (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     artist_id  INTEGER,
#     title   TEXT UNIQUE
# );

# CREATE TABLE Track (
#     id  INTEGER NOT NULL PRIMARY KEY
#         AUTOINCREMENT UNIQUE,
#     title TEXT  UNIQUE,
#     album_id  INTEGER,
#     genre_id  INTEGER,
#     len INTEGER, rating INTEGER, count INTEGER
# );  ''')

# def look(d, key):
#     found = False
#     for child in d:
#         if found : return child.text
#         if child.tag == 'key' and child.text == key :found = True

# xml = et.parse('Library.xml')
# shti = xml.findall('dict/dict/dict')
# for i in shti:
#   if look(i,'Track ID') is None : continue
#   name = look(i,'Name')
#   artist = look(i,'Artist')
#   album = look(i,'Album')
#   count = look(i,'Play Count')
#   rating = look(i,'Rating')
#   length = look(i,'Total Time')
#   Genre = look(i,'Genre')

#   if name is None or artist is None or album is None or Genre is None: continue

#   print(name,artist,album,count,length,Genre,rating)

#   cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)',(name,))
#   cur.execute('SELECT  id FROM Artist WHERE name=?',(name,))
#   artist_id = cur.fetchone()[0]

#   cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)',(Genre,))
#   cur.execute('SELECT  id FROM Genre WHERE name=?',(Genre,))
#   genre_id = cur.fetchone()[0]

#   cur.execute('INSERT OR IGNORE INTO Album (title,artist_id) VALUES (?,?)',(album,artist_id))
#   cur.execute('SELECT  id FROM Album WHERE title=?',(album,))
#   album_id = cur.fetchone()[0]

#   cur.execute('INSERT OR IGNORE INTO Track (title,album_id,genre_id,len,rating,count) VALUES (?,?,?,?,?,?)',(name,album_id,genre_id,length,rating,count))

#   con.commit()


# import xml.etree.ElementTree as et
# import sqlite3

# con = sqlite3.connect('trackdb.sqlite')
# cur = con.cursor()

# cur.executescript('''
# DROP TABLE IF EXISTS Artist;
# DROP TABLE IF EXISTS Album;
# DROP TABLE IF EXISTS Track;

# CREATE TABLE Artist(
#   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#   name TEXT UNIQUE
# );

# CREATE TABLE Album (
#   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#   artistId INTEGER ,
#   title TEXT UNIQUE
#   );
#   CREATE TABLE Track (
#   id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#   albumId INTEGER ,
#   title TEXT UNIQUE,
#   len INTEGER,rating INTEGER , count INTEGER

#   );

#             ''')
# fname = 'Library.xml'

# def look(d, key):
#     found = False
#     for child in d:
#         if found : return child.text
#         if child.tag == 'key' and child.text == key :found = True

#     return None

# shit = et.parse(fname)
# all = shit.findall('dict/dict/dict')
# print('there are',len(all),'dicts')

# for i in all :
#   if look(i,'Track ID') is None: continue
#   name = look(i,'Name')
#   artist = look(i,'Artist')
#   album = look(i,'Album')
#   count = look(i,'Play Count')
#   rating = look(i,'Rating')
#   length = look(i,'Total Time')
#   # Genre = look(i,'Genre')

#   if name is None or artist is None or album is None :continue
#   print(name,artist,album,count,rating,length)

#   cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)',(artist,))
#   cur.execute('SELECT id FROM Artist WHERE name=?',(artist,))
#   artistID = cur.fetchone()[0]
#   cur.execute('INSERT OR IGNORE INTO Album (title ,artistId ) VALUES (?,?)',(album,artistID))
#   cur.execute('SELECT id FROM Album WHERE title=?',(album,))
#   albumId = cur.fetchone()[0]
#   cur.execute('INSERT OR REPLACE INTO Track (title,albumId,len,rating,count ) VALUES (?,?,?,?,?)',(name,albumId,length,rating,count))
#   con.commit()

# SELECT Track.title , Album.title, Artist.name FROM Track join Album JOIN Artist on Track.albumId = Album.id AND Album.artistId = Artist.id


# import sqlite3

# con = sqlite3.connect('emaildb.sqlite')
# cur = con.cursor()

# cur.execute('DROP TABLE IF EXISTS Counts')
# cur.execute('CREATE TABLE Counts (org TEXT , count INTEGER)')

# fname = input('Enter file name: ')
# if (len(fname) < 1): fname = 'mbox.txt'
# fh = open(fname)
# for i in fh:
#   if not i.startswith('From: '): continue
#   org = i.split()[1].split('@')[1]
#   # print(org)
#   cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
#   row = cur.fetchone()

#   if row is None:
#     cur.execute('INSERT INTO Counts (org,count) VALUES (?,1)',(org,))
#   else:
#     cur.execute('UPDATE Counts  SET count=count +1 WHERE org=?',(org,))
# con.commit()

# sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])

# cur.execute('DELETE FROM Counts')
# cur.close()


# In this assignment you will write a Python program somewhat
# similar to http://www.py4e.com/code3/geojson.py. The program
# will prompt for a location, contact a web service and retrieve
# JSON for the web service and parse that data, and retrieve the
# first place_id from the JSON. A place ID is a textual identifier
# that uniquely identifies a place as within Google Maps.

# import urllib.request as ur
# import urllib.parse as up
# import json

# serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# loc = input('enter location :')

# url = serviceurl + up.urlencode({'key':42,'address':loc})
# uh = ur.urlopen(url)
# data = uh.read().decode()


# js = json.loads(data)
# print(json.dumps(js, indent=2))

# print("Retrieving ", url)
# print('Retrieved ',len(data),' characters')
# print('place_id :',js['results'][0]['place_id'])


# import urllib.request, urllib.parse, urllib.error
# import json
# import ssl


# api_key = False
# # If you have a Google Places API key, enter it here
# # api_key = 'AIzaSy___IDByT70'
# # https://developers.google.com/maps/documentation/geocoding/intro

# if api_key is False:
#     api_key = 42
#     serviceurl = 'http://py4e-data.dr-chuck.net/json?'
# else :
#     serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'


# address = input('Enter location: ')

# # parms = dict()
# # parms['address'] = address
# # if api_key is not False: parms['key'] = api_key
# url = serviceurl + urllib.parse.urlencode({'key':42,'address':address})
# print('Retrieving', url)
# uh = urllib.request.urlopen(url)
# data = uh.read().decode()
# print('Retrieved', len(data), 'characters')

# try:
#     js = json.loads(data)
# except:
#     js = None
# if not js or 'status' not in js or js['status'] != 'OK':
#     print('==== Failure To Retrieve ====')
#     print(data)
#     exit()

# # print(json.dumps(js, indent=4))
# lat = js['results'][0]['geometry']['location']['lat']
# lng = js['results'][0]['geometry']['location']['lng']

# print('lat', lat, 'lng', lng)
# location = js['results'][0]['formatted_address']
# print(location)
# print('place_id :', js['results'][0]['place_id'])


# International Institute of Information Technology Hyderabad


# In this assignment you will write a Python program somewhat similar
# to http://www.py4e.com/code3/json2.py. The program will prompt for a
# URL, read the JSON data from that URL using urllib and then parse and
# extract the comment counts from the JSON data, compute the sum of the
# numbers in the file and enter the sum below:

# import urllib.request as ur
# import json

# date = ur.urlopen('http://py4e-data.dr-chuck.net/comments_1763026.json').read().decode()
# jd = json.loads(date)['comments']
# print(len(jd))
# sum = 0
# for i in jd:
#   sum+=i['count']
# print(sum)


# import urllib.request as ur
# import xml.etree.ElementTree as et

# url='http://py4e-data.dr-chuck.net/comments_1763025.xml'
# print('Retrieving',url)

# xml = ur.urlopen(url).read()
# print("Retrieved",len(xml),'characters')
# doc = et.fromstring(xml)
# counts = doc.findall('.//count')
# print('count',len(counts))
# sum =0
# for i in counts:
#  sum+=int(i.text)
# print('sum:',sum)


# data = '''<commentinfo>
# <note>This file contains the actual data for your assignment - good luck!</note>
# <comments>
# <comment>
# <name>Virginie</name>
# <count>100</count>
# </comment>
# <comment>
# <name>Kady</name>
# <count>98</count>
# </comment>
# <comment>
# <name>Ida</name>
# <count>94</count>
# </comment>
# <comment>
# <name>Krishan</name>
# <count>94</count>
# </comment>
# <comment>
# <name>Fruin</name>
# <count>90</count>
# </comment>
# <comment>
# <name>Kaylin</name>
# <count>89</count>
# </comment>
# <comment>
# <name>Sami</name>
# <count>86</count>
# </comment>
# <comment>
# <name>Aon</name>
# <count>84</count>
# </comment>
# <comment>
# <name>Sehar</name>
# <count>84</count>
# </comment>
# <comment>
# <name>Paidamoyo</name>
# <count>84</count>
# </comment>
# <comment>
# <name>Calan</name>
# <count>82</count>
# </comment>
# <comment>
# <name>Samuel</name>
# <count>80</count>
# </comment>
# <comment>
# <name>Keir</name>
# <count>77</count>
# </comment>
# <comment>
# <name>Lowena</name>
# <count>76</count>
# </comment>
# <comment>
# <name>Lena</name>
# <count>71</count>
# </comment>
# <comment>
# <name>Luis</name>
# <count>69</count>
# </comment>
# <comment>
# <name>Kaye</name>
# <count>65</count>
# </comment>
# <comment>
# <name>Oluwafemi</name>
# <count>64</count>
# </comment>
# <comment>
# <name>Rohin</name>
# <count>63</count>
# </comment>
# <comment>
# <name>Kofi</name>
# <count>60</count>
# </comment>
# <comment>
# <name>Krista</name>
# <count>57</count>
# </comment>
# <comment>
# <name>Jess</name>
# <count>56</count>
# </comment>
# <comment>
# <name>Ameelia</name>
# <count>55</count>
# </comment>
# <comment>
# <name>Braiden</name>
# <count>55</count>
# </comment>
# <comment>
# <name>Possum</name>
# <count>50</count>
# </comment>
# <comment>
# <name>Mahum</name>
# <count>46</count>
# </comment>
# <comment>
# <name>Romilly</name>
# <count>45</count>
# </comment>
# <comment>
# <name>Azedine</name>
# <count>41</count>
# </comment>
# <comment>
# <name>Morton</name>
# <count>41</count>
# </comment>
# <comment>
# <name>Ryhanna</name>
# <count>39</count>
# </comment>
# <comment>
# <name>Jamal</name>
# <count>35</count>
# </comment>
# <comment>
# <name>Ezekiel</name>
# <count>35</count>
# </comment>
# <comment>
# <name>Georgy</name>
# <count>33</count>
# </comment>
# <comment>
# <name>Capri</name>
# <count>32</count>
# </comment>
# <comment>
# <name>Kenneth</name>
# <count>30</count>
# </comment>
# <comment>
# <name>Laurabeth</name>
# <count>30</count>
# </comment>
# <comment>
# <name>Yaris</name>
# <count>28</count>
# </comment>
# <comment>
# <name>Aimeeleigh</name>
# <count>28</count>
# </comment>
# <comment>
# <name>Harleigh</name>
# <count>28</count>
# </comment>
# <comment>
# <name>Saman</name>
# <count>26</count>
# </comment>
# <comment>
# <name>Livie</name>
# <count>22</count>
# </comment>
# <comment>
# <name>Renas</name>
# <count>22</count>
# </comment>
# <comment>
# <name>Roary</name>
# <count>22</count>
# </comment>
# <comment>
# <name>Kelvin</name>
# <count>18</count>
# </comment>
# <comment>
# <name>Laughlan</name>
# <count>15</count>
# </comment>
# <comment>
# <name>Marwad</name>
# <count>13</count>
# </comment>
# <comment>
# <name>Mohanad</name>
# <count>13</count>
# </comment>
# <comment>
# <name>Rebeka</name>
# <count>7</count>
# </comment>
# <comment>
# <name>Robbie</name>
# <count>7</count>
# </comment>
# <comment>
# <name>Saicu</name>
# <count>6</count>
# </comment>
# </comments>
# </commentinfo>
# '''
# stuff = ET.fromstring(data)
# # print(stuff.findall('comments/comment/count'))
# print(len(stuff.findall('comments/comment/count')))


# ls  = [ x.text for x in  stuff.findall('comments/comment/count')]
# print((ls))

# sum =0
# for i in ls:
#     sum +=int(i)
# print(sum)


# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# c = int(input('Enter count: '))
# p = int(input('Enter position: '))
# for i in range(c):
#   html = urllib.request.urlopen(url, context=ctx).read()
#   soup = BeautifulSoup(html, 'html.parser')
#   print(html)


#   # Retrieve all of the anchor tags
#   tags = soup('a')
#   ll =list()
#   for tag in tags:
#      # print(tag.get('href', None))
#       ll.append(tag.get('href', None))
#   url = ll[p-1]
#   print(ll[p-1])

# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Taira.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: E


# # To run this, download the BeautifulSoup zip file
# # http://www.py4e.com/code3/bs4.zip
# # and unzip it in the same directory as this file

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")

# # Retrieve all of the anchor tags
# tags = soup('span')
# c=0
# for tag in tags:
#     # Look at the parts of a tag
#     print('TAG:', tag)
#     print('URL:', tag.get('href', None))
#     print('Contents:', tag.contents[0])
#     print('Attrs:', tag.attrs)
#     c+=int(tag.contents[0])
# print(c)


# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')

# mysock.close()


# In this assignment you will read through and parse a
# file with text and numbers. You will extract all the
# numbers in the file and compute the sum of the numbers.
# import re

# f= open('regexft.txt')
# h1= []
# for i in f:
#   h = re.findall('[0-9]+',i)
#   h1.extend(h)

# sh =0
# for i in h1:
#   sh += int(i)

# print(sh)

# print(sum([ i for i  in f'[0-9]+',**************************.read()) ] ) )


# s = " omer 12 in 2003 learning py3a"
# s1 = " omer 19 in 555 learning py8"

# h = re.findall('[0-9]+',s)
# h1 = re.findall('[0-9]+',s1)
# h1.extend(h)
# print(h1)


# 10.2 Write a program to read through the
# mbox-short.txt and figure out the distribution
# by hour of the day for each of the messages.
# You can pull the hour out from the 'From '
# line by finding the time and then splitting
# the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.

# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)
# count= 0
# dh = dict()
# for line in handle:
#   if line.startswith('From'):
#     count+=1
#     if count%2==1:
#       hold = line.split()[5].split(':')[0]
#       dh[hold] = dh.get(hold,0)+1

# dh =sorted(dh.items())
# for k,v in dh:
#   print(k,v)


# 9.4 Write a program to read through the mbox-short.
# txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word
# of those lines as the person who sent the mail. The program
# creates a Python dictionary that maps the sender's mail
# address to a count of the number of times they appear in
# the file. After the dictionary is produced, the program
# reads through the dictionary using a maximum loop to find
# the most prolific committer.

# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)

# emaild = dict()
# for line in handle:
#   if line.startswith('From'):
#     emaild[line.split()[1]] = emaild.get(line.split()[1],0)+1
# sed = sorted(emaild.items(), key=lambda x : x[1], reverse=True) #cool asf
# print(sed[0][0],int(sed[0][1]/2))


# 8.5 Open the file mbox-short.txt and read it line by line.
# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word
# in the line (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
# Also look at the last line of the sample output to see how to print the count.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = "mbox-short.txt"
# hell yeah i fixed it
# fh = open(fname)
# count = 0
# cn2 =0
# for i in fh:
#   if not i.startswith('From'):
#     continue

#   cn2+=1
#   if cn2%2==0:
#    continue

#   print(i.rstrip().split()[1])
#   count+=1

# print("There were", count, "lines in the file with From as the first word")


# 8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split()
# method. The program should build a list of words.
# For each word on each line check to see if the word is
# already in the list and if not append it to the list.
# When the program completes, sort and print the resulting
# words in python sort() order as shown in the desired output.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
#  l = line.split()
#  for i in l:
#    if i not in lst:
#      lst.append(i)
# lst.sort()
# print(lst)


# 7.2 Write a program that prompts for a file name,
# then opens that file and reads through the file,
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from
# each of the lines and compute the average of those values
# and produce an output as shown below. Do not use the sum()
# function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)
# count =0
# hold =0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"):
#         continue
#     hold+=float(line[line.find("0"):])
#     count+=1
# print('Average spam confidence:',hold/count)


# 7.1 Write a program that prompts for a file name,
# then opens that file and reads through the file,
# and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.

# Use words.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)
# for i in fh:
#      print(i.upper().rstrip())


# 6.5 largest = None
# smallest = None
# while True:
#     num = (input("Enter a number: "))
#     if num == "done":
#         break
#     try:
#      num= int(num)
#     except:
#       print('Invalid input')
#       continue
#     if largest is None:
#      largest = num
#     elif largest < num:
#      largest =num
#     if smallest is None:
#       smallest = num
#     elif smallest >num:
#       smallest = num


# print("Maximum is", int(largest))
# print("Minimum is",  int(smallest))


# 4.6 def computepay(h, r):
#     if h > 40:
#       hold = h - 40
#       return 40*r + hold*r*1.5
#     else:
#       return h*r
# hrs = float(input("Enter Hours:"))
# rate =float( input("Enter rate:"))
# p = computepay(hrs, rate)

# print("Pay", p)


# 3.3 score = float(input("Enter Score: "))
# if score >= 0.9 and score <= 1.0:
#   print('A')
# elif score >= 0.8 and score <= 1.0 :
#   print('B')
# elif score >= 0.7 and score <= 1.0:
#   print('C')
# elif score >= 0.6 and score <= 1.0:
#   print('D')
# elif score < 0.6 and score <= 1.0:
#   print('F')
# else:
#   print('Error')
#   quit()


# 6.5  Write code using find() and string slicing (see section 6.10) to
#   extract the number at the end of the line below. Convert the extracted
#   value to a floating point number and print it out.
# text = "X-DSPAM-Confidence:    0.8475"
# print(float(text[text.find("0"):]))


# 3.1 Write a program to prompt the user for hours
# and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input -
# assume the user types numbers properly.
# hrs = input("Enter Hours:")
# h = float(hrs)
# rate = input("Enter rate:")
# r = float(rate)
# if h > 40:
#   hold =h-40
#   print(40*r+hold*r*1.5)
# else:
#   print(r*h)
