import json

def filter(readfile, outfile):
	tweets_file = open(readfile, "r")
	outfile = open(outfile, 'a')
	for line in tweets_file:
	    try:
	    	tweet = json.loads(line)
	    	if 'http' not in tweet['text'] and tweet['retweeted'] == False:
	    		json.dump(tweet, outfile)
	    		outfile.write('\n')
	    except:
	        continue
	
# def read(readfile):
# 	tweets_file = open(readfile, "r")
# 	for line in tweets_file:
# 	    try:
# 	    	tweet = json.loads(line)
# 	    	print 1
# 	    except:
# 	        continue

def main():
	filter('data.json', 'data_clean.json')
	# read('data_clean.json')

if __name__ == "__main__":
    main()


