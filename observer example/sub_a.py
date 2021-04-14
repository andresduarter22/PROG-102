from sub_interface import Subscriber


class ConcreteSubscriberA(Subscriber):
    def update(self, subject):
        print("Sub A: Reacted to the event")
