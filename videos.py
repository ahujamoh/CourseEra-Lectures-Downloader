'''
	The link that I was trying to download was this
	https://class.coursera.org/compilers-003/lecture/download.mp4?lecture_id=1
	
	If you want to use this script to download video lectures then just change the url in the code accordingly
'''

import os
import glob
from urllib import unquote
import urllib2

def unquote_u(source):
    res = unquote(source)
    if '%u' in result:
        res = result.replace('%u','\\u').decode('unicode_escape')
    return res

def download(url):
    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)
    file_size_dl = 0
    block_sz = 8192

    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,
    f.close()




os.system("mkdir CourseEra")

# the initial and final values of documents to be downloaded
initial_value = raw_input("Enter the initial number: ")
final_value = raw_input("Enter the final number: ")

init = int(initial_value)
final = int(final_value)


for ctr in range(init, final + 1):

	# Download the file
	#url = "wget --content-disposition --quiet https://class.coursera.org/compilers-003/lecture/download.mp4?lecture_id=" + str(ctr)
	#os.system(url)
    url = "https://class.coursera.org/compilers-003/lecture/download.mp4?lecture_id=" + str(ctr)
    download(url)

	# Rename the file
    result = []
    result = glob.glob('*.mp4')

    for i in range(0, len(result)):
		x = result[i]
		encoded_name = x[:len(x)/2]
		actual_name = unquote_u(encoded_name)
		
		# Rename the file into its actual name
		os.rename(x, actual_name)
		
		# Move the files into CourseEra Directory
		move_cmd = "find . -name \*.mp4 -exec cp {} CourseEra/ \;"
		os.system(move_cmd)
		print "A new file successfully downloaded"

		# Remove all .mp4 files from parent directory
		del_cmd = "rm *.mp4"
		os.system(del_cmd)
		
		os.popen('notify-send "CourseEra Notification" "File Downloaded :)" ')
		
os.popen('notify-send "CourseEra Notification" "All files successfully downloaded :)"' )
