email=input("enter your email: ").strip()
username=email[:email.index("@")]
domName=email[email.index("@")+1:]
format_=(f"your username: '{username}'\nyour domain: '{domName}'")
print(format_)
