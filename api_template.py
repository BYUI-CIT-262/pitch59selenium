import requests
""" CREATE A USER """
# specify the function to be carried out
signupURL = "api/account/sign-up?otp_check=true"
# set a variable to equal the URL
pitch59_URL = f"https://api.p59.dev/{signupURL}"
# set arguments that focus the data request
body = {
        "firstName": "Tony",
        "lastName": "Stark",
        "isTesterUser": True,
        "contactNumber": "(999) 999-9456",
        "emailID": "jarenbrownlee@gmail.com",
        "password": "BetterThanCap10",
        "zipCode": "84440",
        "userReferralModel": {
            "referralEmail": "ironman@gmail.com"
        },
        "otpCode": 9865
    }
# request information from endpoint according to listed arguments
response = requests.post(pitch59_URL, json=body)
# , headers=head)
# check for successful request
if response.status_code == 200:
    #convert data to a python dictionary
    print(response.status_code, "- Success!")
    data_dict = response.json()["data"]
    print("User ID:", data_dict["userId"])
    print("Token:", data_dict["token"])
else:
    #The request failed- print the status code:
    print("Failure with status code:", response.status_code)
    print(response.json())