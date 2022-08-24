refresh_endpoint='http://127.0.0.1:8000/api/token/refresh/'
login_endpoint='http://127.0.0.1:8000/api/token/'
blacklist_endpoint='http://127.0.0.1:8000/api/token/blacklist/'
signup_endpoint='http://127.0.0.1:8000/account/create-user/'
activate_endpoint='http://127.0.0.1:8000/auth/verify-email/'
product_endpoint='http://127.0.0.1:8000/products/all/'



import traceback
import requests
import datetime

# response=requests.post(blacklist_endpoint,{'refresh':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1ODMyNjIxMCwiaWF0IjoxNjU4MjM5ODEwLCJqdGkiOiI1ZWEyMWY4YzczODU0MjEyYjcyZGZmODI3YzBhODQyMCIsInVzZXJfaWQiOjF9.SM9gL9aHmwn91WPQHYxxQPAIrqlkyFJHMQSI5438xms'})


response=requests.post(login_endpoint,{'email':'dayodele89@gmail.com','password':'heso123yam'})
print(response.json())


response=requests.get(product_endpoint)
print(response)











# response=requests.post(signup_endpoint,{'email':'dayodele189@gmail.com','password':'heso123yaml',
#  'fullname':'David Second',"password1":"heso123yaml"})

# response=requests.post(activate_endpoint,{'otp':'738fe5'})
# print(response)

'''
DATE TIME DEMO

current_time=datetime.datetime.now()

print(current_time)

timestamp=current_time.timestamp()
print(timestamp)


print(datetime.datetime.fromtimestamp(timestamp))

'''




def try_and_catch(func):

    def inner(*args,**kwargs):
        try:
            func(*args,**kwargs)

        except Exception as e:
            traceback.print_exc()



    return inner

@try_and_catch
def absurd_function():
    return 1/0


