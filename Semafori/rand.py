import random

if __name__ == '__main__':
    n = int(input("Introduce n: "))
    l = int(input("Introduce l: "))
    road_range = l - 1
    last = 1
    number_list = []
    for i in range(n):
        number_list.append(random.randint(last, road_range))
        last = number_list[-1] + 1
        number_list.append(random.randint(1, 100))
        number_list.append(random.randint(1, 100))
    number_str = ' '.join(str(e) for e in number_list)
    print(n, l, number_str)

