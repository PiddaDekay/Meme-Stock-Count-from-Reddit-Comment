from psaw import PushshiftAPI
import datetime as dt

api = PushshiftAPI()
start_time=int(dt.datetime(2021, 10, 12).timestamp())
submissions = api.search_submissions(after=start_time,
                            subreddit='wallstreetbets',
                            filter=['url','author', 'title', 'subreddit'])


wordsearch = open('stockmentions.txt','w')
for submission in submissions:
    words = submission.title.split()
    cashtags = set(filter(lambda word: word.lower().startswith('$'),words))
    if len(cashtags)>0:
        for cashtag in cashtags:
            cashtag=cashtag.replace('$','')
            cashtag=cashtag.replace(',','')
            cashtag=cashtag.replace('.','')
            cashtag=cashtag.replace('!','')
            cashtag=cashtag.replace('?','')
            cashtag=cashtag.replace(':','')
            if(len(cashtag)>0 and cashtag.isalpha()==True):
                wordsearch.write(str(cashtag)+" ")
                print(cashtag)
wordsearch.close()



