# from sklearn.LinearRegression import LinearRegression

# model = LinearRegression(normalize=True)
# normalize = model.normalize 

import datetime

class User: 
    def __init__(self, mod_status, username, reputation):
    self.mod_status = mod_status
    self.username = username
    self.reputation = reputation
    self.banned = False

    def upvote_thread(self, thread):
        now = datetime.datetime.now()
        vote = Vote(up=True, time_voted=now, voter=self.username thread=thread)
        return vote

class Moderator():
    def __init__(self, username, reputation):
        self.username = username
        self.reputation = reputation
        self.banned = False
        

    
class Vote:
    def __init__(self, up, time_voted, voter, thread):
        self.up = up
        self.time_voted = time_voted
        self.voter = voter
        self.thread = thread
        self.is_deleted = False

    def delete(self):
        self.is_deleted = True

class thread:
    def __init__(self, title, parent_thread, is_featured):
        self.title = title
        self.parent_thread = parent_thread
        self.upvote_count = 0
        self.downvote_count = 0
        self.comments = []
        self.is_feature = is_featured

    def feature_thread(self):
        self.is_feature = True






sarah = User(mod_status=True, username='sarah', reputation=100)
moto_thread = Thread('motorcycles are cool', 'things that are cool')
sarahs_vote = sarah.upvote_thread(moto_thread, time_voted=datetime.now())
sarahs_vote.delete()
sarahs_username = sarah.username
sarahs_reputation = sarah.reputation
sarahs_mod_status = sarah.mod_status
sarahs_banned = sarah.banned
