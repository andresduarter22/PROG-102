from concrete_publisher import ConcretePublisher
from concrete_publisher_2 import ConcretePublisher2
from sub_a import ConcreteSubscriberA
from sub_b import ConcreteSubscriberB

if __name__ == "__main__":

    publisher = ConcretePublisher()
    publisher_2 = ConcretePublisher2()

    sub_a = ConcreteSubscriberA()
    publisher.subscribe(sub_a)

    sub_b = ConcreteSubscriberB()
    publisher.subscribe(sub_b)

    publisher.do_something()
    publisher.do_something()

    publisher.unsubscribe(sub_a)

    publisher.do_something()

    publisher_2.subscribe(publisher)

    publisher_2.do_something()
