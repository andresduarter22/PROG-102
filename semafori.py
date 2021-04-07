if __name__ == '__main__':
    string = input()
    values = string.split()
    N, L = values[0], values[1]
    values.pop(0)
    values.pop(0)
    print(N, L, values)
    # lights=[[for j in values]for i in N]