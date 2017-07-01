import requests
import json
import time
import os

class FB_parser:



    def __init__(self, token):
        self.token = token
        data = [self.get_numbers()]

        for id in self.get_friend():
            try:
                data.append(self.get_numbers(id))

            except:
                continue
        self.data = data




    def get_posts_date(self,myData):

        posts = myData['data']
        postsTime = []

        for post in posts:

            postsTime.append(post['created_time'].split("T")[0])
        return postsTime





    def next_page(self, myData):

        return myData["paging"]['next']
    '''print(next_page(res))'''



    def get_friend_number(self, id = 'me'):
        friends = self.getPage("https://graph.facebook.com/v2.9/" + id + "/friends?access_token=%s" % (self.token))
        if "summary" in friends.keys():
            return int(friends["summary"]["total_count"])
        else:
            return 0



    '''print(get_friend_number())'''

    @classmethod
    def get_currentTime(self):

        localTime = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
        date = localTime.split("-")
        return date

    @classmethod
    def inlastOneYear(self, dateInput):
        date = dateInput.split("-")

        nowDate = self.get_currentTime()
        if int(date[0]) < int(nowDate[0])-1:

            return False
        elif int(date[0]) == int(nowDate[0])-1 and int(date[1]) < int(nowDate[1]):

            return False
        elif int(date[1]) == int(nowDate[1]) and int(date[2]) < int(nowDate[2]):

            return False
        else:
            return True

    '''print(get_currentTime())'''

    @classmethod
    def getPage(self, url):
        res = requests.get(url)
        page = json.loads(res.text)
        return page

    def get_numbers(self, id = 'me'):
        myData = self.getPage("https://graph.facebook.com/v2.9/" + id + "/posts?access_token=%s" % (self.token))
        posts_date = []
        for date in self.get_posts_date(myData):
            posts_date.append(date)
        while self.inlastOneYear(posts_date[-1]):
            myData = self.getPage(self.next_page(myData))
            for date in self.get_posts_date(myData):
                posts_date.append(date)

        while not self.inlastOneYear(posts_date[-1]):
            posts_date.pop()

        data = {'id':id, 'friend_number':self.get_friend_number(id), 'post_number':len(posts_date)}

        return data

    def get_friend(self, id = "me"):
        friendsData = self.getPage("https://graph.facebook.com/v2.9/" + id + "/friends?access_token=%s" % (self.token))
        friends = []
        for friend in friendsData['data']:
            friends.append(friend['id'])
        return friends



if __name__ == '__main__':
    token = "EAACEdEose0cBAEPMWnvu5hAU4Q6zxrDQwQEOF19iI7ZCzXD9kDYbV4q2j2D0v4SytgXtpY19VIuRr40VGy8j2S7BKuDd8kqn9P4AvjmmAUOVD4uKzhzS6cSw3HrU3AldrRy3y0KaCSsBNHg0LeYKalHM50ZCRHx3ZB2gZCyZB4EPgMLUzVZA61fqWcJdik9uMZD"

    myParser = FB_parser(token)
    print(myParser.get_friend())
    print(myParser.data)

    os.system("pause")










