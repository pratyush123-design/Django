import random

answers = [
    "Yes, definitely.",
    "Ask again later.",
    "No way!",
    "Absolutely!",
    "I don't think so.",
    "It is certain.",
    "Very doubtful.",
    "Without a doubt.",
    "Better not tell you now.",
    "Signs point to yes."
]

question = input("Ask the Magic 8-Ball a yes/no question: ")
print("Thinking...\n")
print(random.choice(answers))
