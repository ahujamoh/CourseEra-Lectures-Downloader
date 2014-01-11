#https://class.coursera.org/compilers-003/lecture/subtitles?q=1_en&format=srt
import urllib2

def scrape(page_url):
	f = urllib2.urlopen(page_url)
	s = f.read()

	base_url = 'https://class.coursera.org/compilers-003/lecture/subtitles?q='

	links = []

	while True:
		start_pos = s.find(base_url)

		if start_pos == -1:
			break
		else:
			endpos = s.find('_', start_pos)
			links.append(s[start_pos:endpos])
			s = s[endpos:]

	return links

def download(_url):
	lec_no = _url.split('=')[-1]
	file_name = ("%s_%s.srt") %("Lecture", lec_no) 

	_url += '_en&format=txt'

	f = urllib2.urlopen(_url)
	ff = open(file_name, 'wb')

	while True:
		packet = f.read()
		if not packet:
			break
		ff.write(packet)
	f.close()
