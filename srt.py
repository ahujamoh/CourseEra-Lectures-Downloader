'''
    The link that I was trying to download was this
    https://class.coursera.org/compilers-003/lecture/subtitles?q=1_en&format=srt
    
    If you want to use this script to download srt's then just change the url in the code accordingly.
    
'''

import os
import glob
from urllib import unquote

def unquote_u(source):
    res = unquote(source)
    if '%u' in result:
        res = result.replace('%u','\\u').decode('unicode_escape')
    return res


os.system("mkdir CourseEra")

# the initial and final values of documents to be downloaded
initial_value = raw_input("Enter the initial number: ")
final_value = raw_input("Enter the final number: ")

init = int(initial_value)
final = int(final_value)

for ctr in range(init, final + 1):

	# Download the file
	url = 'wget --content-disposition --no-http-keep-alive --quiet "https://class.coursera.org/compilers-003/lecture/subtitles?q=' + str(ctr) + '_en&format=srt"'
	os.system(url)

	# Rename the file
	result = []
	result = glob.glob('*.srt')

	for i in range(0, len(result)):
		x = result[i]
		encoded_name = x[:len(x)/2]
		actual_name = unquote_u(encoded_name)
		
		# Rename the file into its actual name
		os.rename(x, actual_name)
		
		# Move the files into CourseEra Directory
		move_cmd = "find . -name \*.srt -exec cp {} CourseEra/ \;"
		os.system(move_cmd)

		# Remove all .srt files from parent directory
		del_cmd = "rm *.srt"
		os.system(del_cmd)

os.popen('notify-send "CourseEra Notification" "All subtitles successfully downloaded :)"' )
