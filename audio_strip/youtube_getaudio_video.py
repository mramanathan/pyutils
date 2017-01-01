# coding: utf-8

#!/usr/bin/env python

import argparse
import re
import os
import subprocess


## Ask the use for audio format
notime = " --no-mtime"
utube_cmd = "youtube-dl "



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



def askUser(link):

	""" Get the list of supported audio or video formats """

	# -F : list all formats, no download shall begin
	listfmts = " -F "

	cmd = utube_cmd + listfmts + link

	## For real-time output of the cmd
	print(" ==> List of supported audio or video formats")
	subprocess.call([cmd], shell=True, stderr=subprocess.STDOUT)

	user_choice = input("\n== Which format you wish to download (value from only second column is accepted) ?: ")

	return user_choice



def getVideo(link):

	""" From the youtube link, extract the Video in the format chosen by the user """

	title = getTitle(link)
	video_type = askUser(link)

	if (video_type == ""):
		video_type = " mp4 "
	else:
		video_type = video_type + " "
	video = " -f " + video_type + " "
	cmd = utube_cmd + video + link
	print(" ==> Video shall be extracted using this cmd : {}".format(cmd))

	print(" ==> Extraction in progress ==")
	xtraction = subprocess.check_output([cmd], shell=True, stderr=subprocess.STDOUT)
	
	# to be used as filename
	cmd_output = (xtraction.decode("utf-8")).split('\n')[5].split(':')[1]
	print(" ==> Video is saved in {}".format(cmd_output))

	return None



def getAudio(link):

	""" From the youtube link, extract the audio in the format chosen by the user """

	title = getTitle(link)
	audio_type = askUser(link)

	# -x : extract audio
	audio_extract = " -x"
	# (Re)member ==> logical operators are words
	if (audio_type == " ") or (audio_type == "webm"):
		# set it to default type provided by the tool
		audio_type = " best "
	else:
		audio_type = audio_type + " "
	audio = " --audio-format " + audio_type + " "
	cmd = utube_cmd + notime + audio_extract + audio + link
	print(" ==> Audio shall be extracted using this cmd : {}".format(cmd))

	print(" ==> Extraction in progress ==")
	xtraction = subprocess.check_output([cmd], shell=True, stderr=subprocess.STDOUT)
	
	# to be used as filename
	cmd_output = (xtraction.decode("utf-8")).split('\n')[5].split(':')[1]
	print(" ==> Audio is saved in {}".format(cmd_output))

	## Should find out why file cannot be renamed after the audio
	## extraction is done???
#	user_choice = input("\n== Do you want to retain this title? (YES or NO) : ")
#	
#	if (user_choice.upper() == "YES"):
#		print("We shall retain the existing title.")
#		print("{} is the title of the youtube link".format(title))
#	elif (user_choice.upper() == "NO"):
#		user_title = input("Give a new title of your choice : ")
#		user_title.strip()
##		modfileName(cmd_output, user_title)
#		print("{} is the title of the youtube link".format(user_title))
#	else:
#		print("We shall retain the existing title.")
#		print("{} is the title of the youtube link".format(title))


	return None




def getTitle(link):

	""" Using the youtube url, return the title """
 
	title = " --get-title "
	cmd = utube_cmd + title + link
	title = subprocess.check_output([cmd], shell=True, stderr=subprocess.STDOUT) 
	title.strip()
	title = title.decode("utf-8")
	title.strip()
	print(" ==> {} is the title of the youtube link".format(title))

	return title



# Example: To get the id from the youtube video link
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
	avconv or ffmpeg

	And, it has been tested on Ubuntu 16.04 LTS with Python v3.5.2
	"""

	parser = argparse.ArgumentParser("Grab the audio or video from the given youtube url")
	parser = argparse.ArgumentParser(add_help=True)

	parser.add_argument('link', action="store", help="Provide the youtube URL here")
	parser.add_argument('type', action="store", help="Strip audio only or video")
	parsed_args = parser.parse_args()

	
	if (parsed_args.link) and (parsed_args.type):
		utube_link = parsed_args.link
		utube_type = parsed_args.type
		if (utube_type == "audio"):
			getAudio(parsed_args.link)
		if (utube_type == "video"):
			getVideo(parsed_args.link)
#		id = videoId(utube_link)


    
if __name__ == "__main__":
    main()
