import authorization
import sys
import requests
import json
import logging
import argparse
from urls import *

logging.basicConfig(filename="output.log", level=logging.DEBUG)



def get_timeline():
	logging.debug("Get Timeline")
	auth = authorization.authorize()
	response = requests.get(TIMELINE_URL, auth=auth)
	return json.dumps(response[text].json(), indent=4)
## FIGURE OUT WHAT TYPE OF STUFF WE'RE WORKING WITH	
	##print json.dumps(response.json(), indent=4)
	##print type(response.json())   -> list

def get_mentions():
	logging.debug("Get Mentions")
	auth = authorization.authorize()
	response = requests.get(MENTIONS_URL, auth=auth)
##This guy prints out only a few items
	for t in response.json():
		print "HERE'S A TWEET"
		print t["text"]
		print t["user"]["name"]
		print t["user"]["screen_name"]
		print t["created_at"]
		print ''

##This guy prints everything.
	#return json.dumps(response.json(), indent=4)



def make_parser():
	"""Construct the command line parser """
	logging.info("Constructing parser")
	description = "Store and retrieve snippets of text"
	parser = argparse.ArgumentParser(description = description)

	subparsers = parser.add_subparsers(dest="command", help="Available commands")

	# Subparser for the get timeline command
	logging.debug("Constructing get_timeline subparser")
	timeline_parser = subparsers.add_parser("timeline", help = "Get your Timeline")

	# Subparser for the get mentions command
	logging.debug("Constructing get_mentions subparser")
	mentions_parser = subparsers.add_parser("mentions", help = "Get your mentions")
	mentions_parser.add_argument("text", nargs="?", help="The text of the tweet")
	mentions_parser.add_argument("user(name)", nargs="?", help="The name of the person who sent the tweet")
	mentions_parser.add_argument("user(screen_name)", nargs="?", help="The screenname of the person who sent the tweet")
	mentions_parser.add_argument("created_at", nargs="?", help="The date the tweet was sent")

	
	return parser






def main():
	""" Main function """
	logging.info("Starting tweetful calls")
	parser = make_parser()
	arguments = parser.parse_args(sys.argv[1:])

	arguments = vars(arguments)
	command = arguments.pop("command")

	if command == "timeline":
		my_timeline = get_timeline()
		print "Getting timeline info '{}'".format(my_timeline)
	elif command == "mentions":
		my_mentions = get_mentions()
		print "Getting mentions info '{}'".format(my_mentions)




if __name__ == "__main__":
	print "calling main"
	main()