import requests
""" CREATE A USER """
# :)
# specify the function to be carried out
signupURL = "api/users/349324458266065113/deleteTestUser"

# specify delete url

# set a variable to equal the URL
pitch59_URL = f"https://api.p59.dev/{signupURL}"
# set arguments that focus the data request
user = {
    # "userID": "349322742934047086",
    # "isTesterUser": True
}
head = {
    "content-type": "application/json",
    "Accept" : "*/*",
    "Accept-Encoding" : "gzip, deflate, br",
    "Connection" : "keep-alive",
    "Authorization" : "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTSUQiOiJEbWZEOE9PM3k0azJIbkp0OWFmVFVuNlBJcGVwN1NENHAvdngvNnhpOHVJZU84Wm1kaHJWa3dxdEsya0I1YkJJIiwiVUlEIjoiQllTVjh5UGlwYk9Hdkk4Y0dVN0lYUmQyL2JHb2pRMElIaFVJSU53L1hlU3RHd2YzMkxuMWIzUXVVUmVyOUkzZiIsIlJJRCI6InRuQVZwYmlKaWlQZlN0UVkybzV1SUJHRWsxWDJHVHpwcWFOb2RHM0VqUGs9Iiwicm9sZSI6IlVzZXIiLCJuYmYiOjE2MjA0Mjc4NDEsImV4cCI6MTYyMDc4Nzg0MSwiaWF0IjoxNjIwNDI3ODQxLCJpc3MiOiJQaXRjaDU5QVBJIiwiYXVkIjoiUGl0Y2g1OVdlYkNsaWVudCJ9.2SIjGTyqVfMsU5V5L3HXE-SEzzlPpX4O4YKGK5Zrn5E"
}
# request information from endpoint according to listed arguments
response = requests.post(pitch59_URL, data=user, headers=head)
# check for successful request
# print(response.status_code) 
if response.status_code == 200:
    #convert data to a python dictionary
    print(response.json())
else:
    #The request failed- print the status code:
    print("Failure with status code:", response.status_code)
    print(response.json())