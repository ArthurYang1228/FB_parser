import requests
import  json

def get_friend(token, id="me"):
    friendsData = getPage("https://graph.facebook.com/v1.0/" + id + "/friends?access_token=%s" % (token))
    friends = []
    for friend in friendsData['data']:
        friends.append(friend['id'])
    return friends


def getPage(url):
    res = requests.get(url)
    page = json.loads(res.text)
    return page

token = "EAACEdEose0cBAEPMWnvu5hAU4Q6zxrDQwQEOF19iI7ZCzXD9kDYbV4q2j2D0v4SytgXtpY19VIuRr40VGy8j2S7BKuDd8kqn9P4AvjmmAUOVD4uKzhzS6cSw3HrU3AldrRy3y0KaCSsBNHg0LeYKalHM50ZCRHx3ZB2gZCyZB4EPgMLUzVZA61fqWcJdik9uMZD"
print(get_friend(token))