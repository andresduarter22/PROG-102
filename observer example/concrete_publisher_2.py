from publisher_interface import PublisherInterface
from sub_interface import Subscriber


class ConcretePublisher2(PublisherInterface):
    _subs_list = []
    _text = None

    def subscribe(self, subscriber):
        print("Publisher 2: New sub :D")
        self._subs_list.append(subscriber)

    def unsubscribe(self, subscriber):
        print("Publisher 2: bye sub :c")
        self._subs_list.remove(subscriber)

    def notify(self):
        print("Publisher 2: Notifying subs...")
        for sub in self._subs_list:
            sub.update(self)

    def do_something(self):
        self._text = input("Type something: ")
        print("Doing something")
        self.notify()
