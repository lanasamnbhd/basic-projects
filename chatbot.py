from nltk.chat.util import Chat, reflections

#pairs is a list of patterns and responses
pairs=[
    [
        r"(.*)my name is (.*)",
        ["hello %2, how are you doing?",]
    ],
    [
        r"(.*)help (.*)",
        ["i can help you",]
    ],
    [
        r"(.*)your name?",
        ["my name is chatbot, but you can call me as you want.",]
    ],
    [
        r"how are you (.*)?",
        ["i am doing very well","i am great, thanks for asking",]
    ],
    [
        r"sorry (.*)",
        ["it's alright","it's OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["nice to hear that", "alright, great!", ]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["hello", "hey there", ]
    ],
    [
        r"what (.*) want?",
        ["make me an offer i can't refuse", ]

    ],
    [
        r"(.*)created(.*)",
        ["sorry, but i don't have any information about it ", "top secret ;)", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Berlin, Germany', ]
    ],
    [
        r"(.*)raining in (.*)",
        ["no rain in the past 4 days here in %2",]
    ],
    [
        r"how (.*) health (.*)",
        ["health is very important, but i am a computer, so i don't need to worry about that :) ", ]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["i'm a very big fan of swimming and basketball", ]
    ],
    [
        r"quit",
        ["bye for now. see you later :)) ", "it was nice talking to you. see you soon :)"]
    ],
    [
        r"(.*)",
        ['that is nice to hear']
    ],
]

print(reflections)

myDummyReflections={
    "go"    : "gone",
    "hello"    : "hey there"
}

#default message at the start of chat
print("Hi, I'm chatbot and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")
#create chat bot
chat = Chat(pairs, reflections)

#start conversation
chat.converse()

