from datetime import datetime



class Spy:
    def __init__(self,name, age, rating):
        self.name = name
        self.age =age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

class Spy_friend:
    def __init__(self,name, age, rating,chat):
        self.name = name
        self.age =age
        self.rating = rating
        self.is_online = True
        self.chats = chat
        self.current_status_message = None

spy = Spy('Mr Ashish Mishra',23,7)

friend_one = Spy_friend('mr ram',23,6,[])
friend_two = Spy_friend('mr shyam',23,6, [])
friend_three = Spy_friend('mr baam',23,6, [])

friends = [friend_one,friend_two,friend_three]


class ChatMessage:

    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me