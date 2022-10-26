def main():
    f = open("questions.txt", "r", encoding='utf-8')
    q = {}
    for line in f:
        try:
            l = line.split(":")
            q[l[0].strip()] = l[1].strip()
        except:
            print("oops")
    while 1:
        question = input("Enter question:\n")
        if question in q:
            print(q[question])
        else:
            print("idk")
if __name__ == '__main__':
    main()
