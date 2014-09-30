import authorization
import sys
import requests
import json
from urls import *


def get_timeline():
##This one works
	auth = authorization.authorize()
	response = requests.get(TIMELINE_URL, auth=auth)
	print json.dumps(response.json(), indent=4)

def get_mentions():
## This one doesn't
	auth = authorization.authorize()
	response = requests.get(MENTIONS_URL, auth=auth)
	print json.dumps(response.json(), indent=4)



def main():
	""" Main function """

	#get_timeline()
	get_mentions()





if __name__ == "__main__":
	print "calling?"
	main()