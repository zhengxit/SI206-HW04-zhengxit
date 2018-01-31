from random import randrange

def user_input():
    current_input = input("What is your question?")
    while (current_input != "quit"):
        if current_input[-1] != "?":
            print("I’m sorry, I can only answer questions.")
        current_input = input("What is your question?")

def get_answer():
    answers = ['It is certain', 'It is decidedly so', 'without a doubt', 'yes definitely', 'you may rely on it', 'as i see it yes', 'most likely', 'outlook good','yes','signs point to yes','reply hazy try again','ask again later','better not tell you now','cannot predict now','concentrate and ask again',"don't count on it",'my reply is no', 'my sources say no','outlook not so good','very doubtful']
    return answers[randrange(len(answers))]

user_input()
print(get_answer())
