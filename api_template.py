import requests
""" CREATE A USER """
#Call create user API (from postman)
# :)
# specify the function to be carried out
signupURL = "/api/account/sign-up?otp_check=true"

# specify delete url


# set a variable to equal the URL
pitch59_URL = f"https://public.p59.dev/{signupURL}"
# set arguments that focus the data request
args = {
        "firstName": "Tony",
        "lastName": "Stark",
        "isTesterUser": True,
        "contactNumber": "(999) 999-9641",
        "emailId": "testmurdock8@gmail.com",
        "password": "BetterThanCap10",
        "zipCode": "84440",
        "userReferralModel": {
            "referralEmail": "Shandu@gmail.com"
        },
        "otpCode": 9865
    }
# request information from endpoint according to listed arguments
response = requests.get(pitch59_URL, params=args)
# check for successful request
print(response.status_code) 
if response.status_code == 200:
    #convert data to a python dictionary
    data_dict = response.json()
else:
    #The request failed- print the status code:
    print("Failure with status code:", response.status_code)