
new, old = [], []

queries = int(input().strip())

for _ in range(queries):
    entry = list(map(int, input().strip().split(" ")))
    command = entry[0]
    if command == 1:
        new.append(entry[1])
    elif command == 2:
        if not old:
            while new: old.append(new.pop())
        old.pop()
    elif command == 3:
        if old:
            print(old[-1])
        else:
            if new:
                while new: old.append(new.pop())
                print(old[-1])
            else:
                print(None)
