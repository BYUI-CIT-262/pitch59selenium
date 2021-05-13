from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import sys
import getopt
import requests
import names

""" CREATE A USER """
#Call create user API (from postman)
# :)
# specify the function to be carried out
signupURL = "api/account/sign-up?otp_check=true"

# specify delete url


# set a variable to equal the URL
pitch59_URL = f"https://api.p59.dev/{signupURL}"
# firstname = input("Please input first name: ")
# lastname = input("Please enter last name: ")
# phonenumber = input("PlEASE enter a phone numbER: ")
# email = input("Plase entar ya'rr email here: ")
# passwordInput = input("Enter password: ")
# zipcode = input("Now your zip code: ")

# set arguments that focus the data request
# args = {
#         "firstName": firstname,
#         "lastName": lastname,
#         "isTesterUser": True,
#         "contactNumber": phonenumber,
#         "emailId": email,
#         "password": passwordInput,
#         "zipCode": zipcode,
#         "otpCode": 9865
#     }
body = {
    "firstName": "Julie",
    "lastName": "Tester",
    "isTesterUser": True,
    "contactNumber": "(999) 999-4444",
    "emailId": "bobhope1234@hotmail.com",
    "password": "BetterThanCap10",
    "zipCode": "84440",
    "otpCode": 9865
}
# request information from endpoint according to listed arguments
response = requests.post(pitch59_URL, json=body)
# check for successful request
if response.status_code == 200:
    #convert data to a python dictionary
    print(response.status_code, "- Success!")
    data_dict = response.json()["data"]
    userId = data_dict["userId"]
    userToken = data_dict["token"]
    print(userId)
    print(userToken)
else:
    #The request failed- print the status code:
    print("Failure with status code:", response.status_code)
    print(response.json())