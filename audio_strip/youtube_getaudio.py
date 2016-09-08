# coding: utf-8

#!/usr/bin/env python

import argparse
import re
import os
import subprocess


audio_title = "youtube-dl --get-title "
ext = "mp3"
# -x : extract audio
utube_cmd = "youtube-dl -x --no-mtime --audio-format mp3 "



def modfileName(oldfile, newname):

	""" rename audio file as requested """

	oldfile = oldfile.strip()
	filname, ext = os.path.splitext(oldfile)
	newfile = newname + ext
	newfile = newfile.strip()

	oldfile = "'" + oldfile + "'"
	newfile = "'" + newfile + "'"
	print("{0} shall be renamed as {1}".format(oldfile, newfile))

	if (os.path.exists(oldfile)):
		subprocess.call('mv oldfile newfile')

	return None



def getAudio(link):

	""" From the youtube link, extract the audio in mp3 format """

	title = videoTitle(link)
	cmd = utube_cmd + link
	print("Audio shall be extracted using this cmd : {}".format(cmd))

	## For real-time output of the cmd
#	subprocess.call([cmd], shell=True, stderr=subprocess.STDOUT)

	print(" == Extraction in progress ==")
	xtraction = subprocess.check_output([cmd], shell=True, stderr=subprocess.STDOUT)
	
	cmd_output = (xtraction.decode("utf-8")).split('\n')[5].split(':')[1]
	print("Audio is saved in {}".format(cmd_output))

	user_choice = input("\n== Do you want to retain this title? (YES or NO) : ")
	
	if (user_choice.upper() == "YES"):
		print("We shall retain the existing title.")
		print("{} is the title of the youtube link".format(title))
	elif (user_choice.upper() == "NO"):
		user_title = input("Give a new title of your choice : ")
		user_title.strip()
#		modfileName(cmd_output, user_title)
		print("{} is the title of the youtube link".format(user_title))
	else:
		print("We shall retain the existing title.")
		print("{} is the title of the youtube link".format(title))


	return None




def videoTitle(link):

	""" Using the youtube url, return the title """

	cmd = audio_title + link
	title = subprocess.check_output([cmd], shell=True, stderr=subprocess.STDOUT) 
	title.strip()
	title = title.decode("utf-8")
	title.strip()
	print("{} is the title of the youtube link".format(title))

	return title



#def videoId(link):
#    
#	""" strip the standard youtube link 
#	and get the video id.
#	"""
#
#	id = re.split("=", link)[1]
#	print("{0} is the ID of the youtube link, {1}".format(id, link))
#
#	return id



def main():

	""" Collect user inputs to get youtube URL, 
	pass it onto relevant functions to strip
	video and fetch only audio.    

	This tool has certain pre-requisites:

	youtube-dl
	ffmpeg

	And, it has been tested on Ubuntu 14.04 LTS with Python v2.7
	"""

	parser = argparse.ArgumentParser("Grab the audio from the given youtube url")
	parser.add_argument("-l", "--link", metavar="youtube link", action="store", help="Provide the youtube URL here")
	parsed_args = parser.parse_args()

	if parsed_args.link:
		utube_link = parsed_args.link
		getAudio(parsed_args.link)
#		id = videoId(utube_link)


    
if __name__ == "__main__":
    main()
