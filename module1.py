import urllib2

def scrape(page_url):
	f = urllib2.urlopen(page_url)
	s = f.read()

	base_url = 'https://class.coursera.org/compilers-003/lecture/download.mp4?lecture_id='

	links = []

	while True:
		start_pos = s.find(base_url)

		if start_pos == -1:
			break
		else:
			endpos = s.find('"', start_pos)
			links.append(s[start_pos:endpos])
			s = s[endpos:]

	return links

def download(_url):
	lec_no = _url.split('=')[-1]
	file_name = ("%s_%s.mp4") %("Lecture", lec_no) 

	u = urllib2.urlopen(_url)
	f = open(file_name, 'wb')

	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])

	print "Downloading: %s Bytes: %s" % (file_name, file_size)

	file_size_dl = 0
	block_sz = 8192

	while True:
		buf = u.read(block_sz)
		if not buf:
			break

		file_size_dl += len(buf)
		f.write(buf)
		status = r"%10d  [%3.2f%%]" % (file_size_dl, \
            file_size_dl * 100. / file_size)
		status = status + chr(8)*(len(status)+1)
		print status,
	
	f.close()