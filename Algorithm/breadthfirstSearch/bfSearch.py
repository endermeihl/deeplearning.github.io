graph = {}
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

from collections import deque

def check_mango(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(person + " is a mango seller")
            return True
        else:
            search_queue += graph[person]
            searched.append(person)
    print("No person is mango seller")
    return False

def person_is_seller(name):
    return name[-1] == 'm'

check_mango("bob")
check_mango("you")