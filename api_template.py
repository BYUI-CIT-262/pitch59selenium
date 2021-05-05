import requests

# specify the function to be carried out
signupURL = "/api/account/sign-up?otp_check=true"

# specify delete url


# set a variable to equal the URL
pitch59_URL = f"https://public.p59.dev/{signupURL}"

# set arguments that focus the data request
args = {
    "parameter" : "value"
}

# request information from endpoint according to listed arguments
response = requests.get(endpoint, params=args)

# check for successful request
if response.status_code == 200:
    #convert data to a python dictionary
    data_dict = response.json()
else:
    #The request failed- print the status code:
    print("Failure with status code:", response.status_code)
