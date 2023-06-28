from sys import argv

script, user_name = argv

prompt = '>> '

print(f"Wassup, {user_name}. This is the {script} script.")
print("We just need to ask you a few questions.")

print(f"Do you like us, {user_name}?")
like = input(prompt)

print(f"Where do you live, {user_name}?")
location = input(prompt)

print(f"What computer are you using right now, {user_name}?")
com = input(prompt)

print(f"""
      Ok, so when we asked if you like us, you said, '{like}'. 
      You said you live in {location}, and that you're using a {com}. 
      Stay put, our agents are on the way...""")