from API_tweeter import Client_id,Client_secret,Username,Password
import praw
from textblob import TextBlob    

def sentimente_analysis(text):
    test = TextBlob(text)
    polar = test.polarity
    
    pos,neg,neu = 0,0,0
    
    if polar>0.00000:
        pos +=1
        
    elif polar<0.000:
        neg +=1
        
    else:
        neu += 1
        
    return pos,neg,neu
        


reddit = praw.Reddit(client_id = Client_id,
                     client_secret = Client_secret,
                     user_agent = "Test",
                     username = Username,
                     password = Password)
desire_subreddit = input("Type in the subreddit: ")
search_in_subreddit = input("Topic: ")
print("\n")
subreddit = reddit.subreddit(desire_subreddit)

#search within a subreddit
for submission in subreddit.search(search_in_subreddit):
    
    positive,negative,neutral = [],[],[]
#all comments
    for comment in submission.comments.list():
        try:
    
             p,neg,n = sentimente_analysis(comment.body)
             positive.append(p)
             negative.append(neg)
             neutral.append(n)
 
        except AttributeError:
            pass

    if len(submission.comments.list()) >0:
        pos = sum(positive)*100/len(submission.comments.list())
        neg = sum(negative)*100/len(submission.comments.list())
        neu = sum(neutral)*100/len(submission.comments.list())
        print("number of comments",len(submission.comments.list()))
        print("Overall sentiment of '{}' is".format(submission.title))
        print("pos:",round(pos,2),"\t","neg:",round(neg,2),"\t","neu:",round(neu,2))
        print(20*"===")