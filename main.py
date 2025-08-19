# main.py
import random, os
from datetime import datetime

# Some jokes    
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "I told my computer I needed a break... it froze.",
    "There are 10 types of people: those who understand binary and those who don’t.",
    "Debugging is like being the detective in a crime movie where you are also the murderer."      
]

print("Hello from GitHub Actions!")
print(f"Current date and time: {datetime.now()}")
print(f"Your lucky number today is: {random.randint(1, 100)}")
print(f"Here’s a random joke: {random.choice(jokes)}")
