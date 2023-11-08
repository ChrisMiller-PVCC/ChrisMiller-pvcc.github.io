# Name: Christopher Miller
#   Prog purpose: This Magic 8-ball code uses a Python tuple since the 
#   user does not have the ability to change the 8-Ball answers.
#   However, the program could have used a Python list instead of a tuple.
#   NOTE: Tuples use parenthese; lists use square braces

import random

answers_8_ball=("As I see it, yet", "Ask again later",
                 "Better not tell you now", "Cannot predict now",
                 "Concentrate and ask again", "Don't count on it",
                 "It is most certain", "It is decidedly so",
                 "Most likely", "My reply is so",
                 "My sources say no", "Outlook good",
                 "Outlook not so good", "Reply hazy try again",
                 "Signs point to yes", "Very doubtful",
                 "Without a doubt", "Yes",
                 "Yes definitely", "You may rely on it", )

def main():

    print("I am the MAGIC-8 BALL and can answer any YES or NO question!")

    another_question = True
    while another_question:
        answer = random.choice(answers_8_ball)

        print("\nShake the MAGIC-8 BALL")
        print("...and now...")
        question = input("\nWhat is your YES or NO question? ")
        print("The MAGIC-8 ball says: " + answer)

        askAgain = input("\nWould you like to ask me another question (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain == "n":
            another_question = False

        print("\nCome back again when you have other important question.")
        print("...Magic-8 Ball OUT.")

main()