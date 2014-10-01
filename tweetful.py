import authorization
import sys
import requests
import json
import logging
import argparse
from urls import *

logging.basicConfig(filename="output.log", level=logging.DEBUG)



def get_timeline():
##This one works
	logging.debug("Get Timeline")
	auth = authorization.authorize()
	response = requests.get(TIMELINE_URL, auth=auth)
	print json.dumps(response.json(), indent=4)

def get_mentions():
## This one doesn't
	logging.debug("Get Mentions")
	auth = authorization.authorize()
	response = requests.get(MENTIONS_URL, auth=auth)
	print json.dumps(response.json(), indent=4)

def make_parser():
	"""Construct the command line parser """
	logging.info("Constructing parser")
	description = "Store and retrieve snippets of text"
	parser = argparse.ArgumentParser(description = description)

	subparsers = parser.add_subparsers(dest="command", help="Available commands")

	# Subparser for the get timeline command
	logging.debug("Constructing get_timeline subparser")
	timeline_parser = subparsers.add_parser("timeline", help = "Get your Timeline")
	#put_parser.add_argument("name", help="The name of the snippet")
	#put_parser.add_argument("snippet", help="The snippet")
	#put_parser.add_argument("filename", default="snippets.csv", nargs="?", help="The snippet filename")

	logging.debug("Constructing get_mentions subparser")
	mentions_parser = subparsers.add_parser("mentions", help = "Get your mentions")

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