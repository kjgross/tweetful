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

def get_mentions():
	logging.debug("Get Mentions")
	auth = authorization.authorize()
	response = requests.get(MENTIONS_URL, auth=auth)
##This guy should only print the "text" part, and leave out the rest of the info.. but it tdoesn't.
	#for t in response:
		#print t.text.encode('utf8')
		#print t.user.screen_name
##This guy prints everything.
	return json.dumps(response.json(), indent=4)

def search_for(term):
	logging.debug("Search for...")
	auth = authorization.authorize()
	response = requests.get(SEARCH_URL, term=term, auth=auth)
	for t in response:
		print t.text.encode('utf-8')

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
	
	# Subparser for the search command
	logging.debug("Constructing search_for subparser")
	search_parser = subparsers.add_parser("search", help = "Search for a specific tweet text")
	search_parser.add_argument("term", help="The term you are searching for")

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
	elif command == "search":
		my_search = search_for(**arguments)
		print "Getting search info '{}'".format(my_search)




if __name__ == "__main__":
	print "calling main"
	main()