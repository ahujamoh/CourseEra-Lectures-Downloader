import sqlite3 as lite
import os
import sys
from module1 import download, scrape

'''
Handling Database 
'''

con = None

if not(os.path.exists('database.db')):
	con = lite.connect('database.db')	
	urls = scrape('https://class.coursera.org/compilers-003/lecture')

	with con:
		cur = con.cursor()
		cur.execute("CREATE TABLE links(url TEXT)")

		for link in urls:
			cur.execute("INSERT INTO links VALUES(?)", (link,))			

else:
	con = lite.connect('database.db')

	with con:
		cur = con.cursor()
		cur.execute("SELECT * FROM links")

		rows = cur.fetchall()

		for row in rows:
			download(row[0])
			cur.execute("DELETE FROM links WHERE url=?", (row[0],))
			con.commit()
			print 'Deleted: ', row[0]