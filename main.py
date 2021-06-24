import jwt
from time import time
private_key = open(r'C:\Users\ag612\PycharmProjects\login-regist-form\nemesis\jwt-key').read()
# token3 = jwt.encode({
#
#     'user_id': 'H125-f115-T548',
#     'username': 'ankit gupta',
#     'roles': ['user', 'moderator'],
#     'exp': time() + 120}, private_key, algorithm='HS256')
# print(token3)
token3= 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiSDEyNS1mMTE1LVQ1NDgiLCJ1c2VybmFtZSI6ImFua2l0IGd1cHRhIiwicm9sZXMiOlsidXNlciIsIm1vZGVyYXRvciJdLCJleHAiOjE2MjQ1NDQ4NDAuOTkxMjc1OH0.Udw5OwLbZzqt_AldqCgy-E62OUDb-kvM1H3ENPcp8jQ'
payload = jwt.decode(token3, private_key, algorithms=['HS256'])
print('connect'if payload else 'disconnct')