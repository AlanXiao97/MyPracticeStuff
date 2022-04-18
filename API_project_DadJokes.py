import requests
import random
from colorama import init
import termcolor
from pyfiglet import figlet_format
init()

print(termcolor.colored(figlet_format("Dad Joke 3000",font="standard"),"cyan"))
topic=input("Let me tell you a joke! Give me a topic: ")
url="https://icanhazdadjoke.com/search"
response=requests.get(url, 
	headers={"Accept":"application/json"},
	params={"term":topic})
output=response.json()
count=len(output["results"])
if count==0:
	print(f"Sorry, I don't have any jokes about {topic}! Please try another topic.")
else:
	print(f"I've got {count} joke/jokes about {topic}. Here it is:")
	print(output["results"][random.randint(0,count)]["joke"])
