import urllib
import json
import sys

def search_twitter(query='mailchimp'):
  url = 'http://search.twitter.com/search.json?show_user-true&q=' + query
  response = urllib.urlopen(url).read()
  data = json.loads(response)
  return data['results']
  
def search_user(query):
  url = 'http://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&screen_name=' + query
  response = urllib.urlopen(url).read()
  data = json.loads(response)
  return data

def print_tweets(tweets):
  for tweet in tweets:
    print tweet['from_user'] + ': ' + tweet['text'] + '\n'

if __name__ == "__main__":
  query = sys.argv[1]
  results = search_twitter(query)
  print_tweets(results)