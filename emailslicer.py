email = str(input('what is your email address:-')).strip()
#slice is the email
user_name = email[:email.index('@')]

domain_name = email[email.index("@")+1:]

res = "your user nameis {} and domain name is '{}' ".format(user_name,domain_name)
print(res)