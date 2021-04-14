from sub_interface import Subscriber


class ConcreteSubscriberB(Subscriber):
    def update(self, subject):
        if subject._state == 0 or subject._state >= 2:
            print("Sub B: Reacted to the event")
