# coding: utf-8

#!/usr/bin/env python

import argparse
import re
import os
import shutil
import subprocess
import fnmatch


## Ask the use for audio format
notime = " --no-mtime"
utube_cmd = "youtube-dl "


def renameFile(old_filename, new_filename):

	""" rename media file as requested """

	file_pattern = '*'

	file_exists = fnmatch.fnmatch(old_filename, file_pattern)
	if (file_exists):
		print(" ==> {} exists in local filesystem directory".format(old_filename, file_exists))
		##--> ugly kludge-ry necessary to match complete filename with wierd extensions!!!
		this_file = old_filename + file_pattern
		files = os.listdir('.')
		for file_name in files:
			match = re.search(this_file, file_name)
			if (match):
				print(" ==> Got the matching file...............", file_name)
				old_filename = file_name
				shutil.move(old_filename, new_filename)
				rename_flag = True
				break
			else:
				rename_flag = False
	else:
		rename_flag = False

	if rename_flag:
		print("\n=~=~>{} is the name of the new media file".format(new_filename))
	else:
		print("No file renaming operation happened.")

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
	title = title.strip()
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
	print(" ==>Video is saved as {}".format(title))

	user_choice = input("==> Do you want to rename {} (YES or NO):".format(title))
	
	if (user_choice.upper() == "YES"):
		new_filename = input(" ==> Enter the name for the new file : ")
		print(" ==> Video file shall be renamed as ", new_filename)
		renameFile(title, new_filename)
	elif (user_choice.upper() == "NO"):
		print(" ==> Video file not renamed")
	else:
		print(" ==> Video file not renamed")

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

	user_choice = input("==> Do you want to rename {} (YES or NO):".format(title))
	
	if (user_choice.upper() == "YES"):
		new_filename = input(" ==> Enter the name for the new file : ")
		print(" ==> Audio file shall be renamed as ", new_filename)
		renameFile(cmd_output, new_filename)
	elif (user_choice.upper() == "NO"):
		print(" ==> Audio file not renamed")
	else:
		print(" ==> Audio file not renamed")

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
	ffprobe or avprobe

	And, it has been tested on Ubuntu 16.04 LTS with Python v3.5.2
	"""

	parser = argparse.ArgumentParser("Grab the audio or video from the given youtube url")
	parser = argparse.ArgumentParser(add_help=True)

	parser.add_argument('link', action="store", help="Provide the youtube URL here")
	parser.add_argument('type', action="store", help="Valid values: audio or video")
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
