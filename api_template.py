import requests
""" CREATE A USER """
# :)
# specify the function to be carried out
signupURL = "api/account/sign-up?otp_check=true"

# specify delete url

# set a variable to equal the URL
pitch59_URL = f"https://api.p59.dev/{signupURL}"
# set arguments that focus the data request
user = {
    "firstName": "Tony",
    "lastName": "Stark",
    "isTesterUser": True,
    "contactNumber": "(999) 999-9874",
    "emailId": "yoloswaggyswaggy@gmail.com",
    "password": "Thi$Pa55word",
    "zipCode": "84440",
    "userReferralModel": {
        "referralEmail": "Shandu@gmail.com"
    },
    "otpCode": 9865
}
head = {
    "content-type": "application/json",
    "Accept" : "*/*",
    "Accept-Encoding" : "gzip, deflate, br",
    "Connection" : "keep-alive"
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