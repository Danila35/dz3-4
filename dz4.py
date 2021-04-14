from uuid import uuid4
import hashlib
salt = uuid4().hex
ur_ob = {}

def page(url):
    if ur_ob.get(url):
        print("Данный сайт присутствует в кэше")
    else:
        new = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        ur_ob[url] = new
        print(ur_ob)

page('https://vk.com/feed')
page('https://vk.com/feed')
