import os
import glob
from urllib import unquote

def unquote_u(source):
    res = unquote(source)
    if '%u' in result:
        res = result.replace('%u','\\u').decode('unicode_escape')
    return res


os.system("mkdir CourseEra")

for ctr in range(50, 98):

	# Download the file
	string = "wget --content-disposition https://class.coursera.org/compilers-003/lecture/download.mp4?lecture_id=" + str(ctr)
	os.system(string)

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
