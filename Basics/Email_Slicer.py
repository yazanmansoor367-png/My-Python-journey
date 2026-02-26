YourName = input("whats your name ?").strip().capitalize()
YourEmail = input("whats your email ?").strip()

YourUsername = YourEmail[ :YourEmail.index("@")]
YourWebsite = YourEmail[YourEmail.index("@")+1 :]

print(f" Your name is {YourName}\n Your Email is {YourEmail} \n Your Username is {YourUsername} \n Your Website is {YourWebsite} ")
