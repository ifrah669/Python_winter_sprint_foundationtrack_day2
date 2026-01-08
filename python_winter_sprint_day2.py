name = input("Enter your username :")
platform = input("Enter your platform :")
account = input("Enter your account type (Work / Personal) :")
account_type = {account}
username = [name]
tup = {platform , account}
user_mapping = {
    name : platform
}

print(f"{'Usernames':<15} : {username}")
print(f"{'Platform & Type':<15} : {tup}")
print(f"{'User Mapping':<15} : {user_mapping}")
print(f"{'Account Type':<15} : {account_type}")