from random import *
import simplejson as json
from collections import namedtuple
import tweepy

ckey = 'AUAYyrCsZHJSRIeHcj7Jspvkg'
csecret = 'PWVkxulUuCeshZuX2g8hnV4L9pap4i1Afgr13RC3wBz6oTG6bF'
atoken = '846614736053518336-am5ahBGHyOAHdyxqNmUjciWX7vJrPLU'
asecret = 'xyCjdAjqxtryeNKONdbfkpNNK2hWr9FlaxodZ7O9YObtL'

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

def followers_count(info):
    res_raw = api.search_users(q=info,per_page=1,page=1)
    if len(res_raw) == 0:
    	print "rand->>>"
    	return randint(1,500)
    res = res_raw[0]._json['followers_count']
    print "ok"
    return int(res)

with open('res.txt', 'w') as fw:
	with open("AMiner-Author.txt") as fr:
		for line_num,line in enumerate(fr):
			if line_num%10==0:
				index=line[7:-1]
			if line_num%10==1:
				info=line[3:]
			# if line_num%10 == 2:
				# info=info+line[3:]
			if line_num%10 == 3:
				# print info
				followers = str(followers_count(info))
				res = index + ' ' + followers
				print res
				fw.write(res+'\n')

			# print line
			# if line_num == 200:
				# break
			# j = j+1
