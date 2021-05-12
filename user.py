import names
# Print (text)
def simple_user():
    name= names.get_first_name() + names.get_last_name()
    print(name)
    return name
simple_user()