# Days until end of year

import threading
import time
import re

affirmatives = set((
    "yes",
    "yeah",
    "yep",
    "yup",
    "sure",
    "ok",
    "okay",
    "aye",
    "indeed",
    "certainly",
    "absolutely",
    "affirmative",
    "roger",
    "right",
    "true",
    "correct",
    "exactly",
    "totally",
    "definitely",
    "gladly",
    "willingly",
    "surely",
    "naturally",
    "clearly",
    "undoubtedly",
    "obviously",
    "positively",
    "granted",
    "accepted",
    "confirmed",
    "noted",
    "fine",
    "alright",
    "agreed",
    "amen",
    "yea",
    "yo",
    "uh-huh",
    "mm-hmm",
    "righto",
    "alrighty",
    "okey",
    "okeydokey",
    "for-sure",
    "solid",
    "word",
    "facts",
    "bet",
    "done",
    "hell yeah",
    "fuck yeah",
    "hell yes",
    "fuck yes",
    "absolutely yes",
    "damn right",
    "hella yes",
    "oh yes",
    "heck yes",
    "heck yeah",
    "undoubtedly",
    "absolutely",
    "indubiably",
    "yessir",
    "yuh"
))

def is_locked_in():
    response = input("Are you going to lock in today?")
    response = re.sub(r"\s", "", response.lower())
    if response == "exit":
        print("Fine, but let's keep the momentum going.")
        quit()
    return response in affirmatives

active = True

while active:
    locked_in = False
    while not locked_in:
        locked_in = is_locked_in()
    print("There we go, let's earn that sunset!")
    time.sleep(24*60*60)


# implement multithreading next time