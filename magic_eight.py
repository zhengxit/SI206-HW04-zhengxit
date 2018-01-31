def user_input():
    current_input = input("What is your question?")
    while (current_input != "quit"):
        if current_input[-1] != "?":
            print("I’m sorry, I can only answer questions.")
        current_input = input("What is your question?")


user_input()
