from random import randrange
from typing import List
from publisher_interface import PublisherInterface
from sub_interface import Subscriber
import os.path


class ConcretePublisher(PublisherInterface, Subscriber):

    _state: int = None
    _subs_list: List[Subscriber] = []

    def subscribe(self, subscriber: Subscriber):
        print("Publisher: New sub :D")
        self._subs_list.append(subscriber)

    def unsubscribe(self, subscriber: Subscriber):
        print("Publisher: bye sub :c")
        self._subs_list.remove(subscriber)

    def notify(self):

        print("Publisher: Notifying subs...")
        for sub in self._subs_list:
            sub.update(self)

    def do_something(self):

        print("\nPublisher: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Publisher: My state has just changed to: {self._state}")
        self.notify()

    def update(self, subject):
        if os.path.isfile("example_file.txt"):
            f = open("example_file.txt", "a")
            f.write(subject._text)
            f.close()
        else:
            f = open("example_file.txt", "x")
            f.write(subject._text)
            f.close()
        f = open("example_file.txt", "r")
        print(f.read())
        print("Publisher 1 as a sub: Reacted to the event")
