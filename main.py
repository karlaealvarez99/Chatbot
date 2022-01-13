import nltk
from nltk.chat.util import Chat, reflections

def chatbot():
        print("Hey!I'm your friendly helping chatbot! Start with a hello or your name.") 

chatbot()

set_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, I do not byte so say hello!",]
    ],
    [
        r"hi|hey|hello",
        ["Hello, I'm chatbot! But call me Botbot and you will be my friend forever.", "Hey there, I heard you are a developer. Need my help? Yes or no?",]
    ], 
    [
        r"what is your name?",
        ["You can call me a chatbot. My friends call me the enemy of Alexa..",]
    ],
    [
        r"yes",
        ["Awesome sauce! Let's start with Pluralsight. Check their website for coding courses. Type other for another source",]
    ],
    [
        r"no",
        ["Well, I tried..I will get to Siris level I promise..",]
    ],
    [
        r"other",
        ["Codewars is another good one. Check their website for hands on practice", "Try the freecodecamp website. It is simple and easy!",]
    ],
    [
        r"Botbot",
        ["Y-yeah?",":)",]
    ],
    [
        r"thank you|thanks",
        ["I am happy to help. Type quit to end the chat.", "No problem, you're welcome. Type quit to end the chat.",]
    ],
    [
        r"quit",
    ["Bye, take care. See you soon and happy coding :) ","It was nice talking to you. Happy coding and see you soon :)"]
],
]

    

chat = Chat(set_pairs, reflections)
print(chat)

#
chat.converse()
if __name__ == "__main__":
    chatbot()
