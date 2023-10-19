# %%
class stack:
    def __init__(self):
        self._data = []
    
    def push(self, n):
        self._data.append(n)
        return 'ok'

    def pop(self):
        return self._data.pop()
    
    def back(self):
        return self._data[-1]
    
    def size(self):
        return len(self._data)
    
    def clear(self):
        self._data.clear()
        return 'ok'

# %%
s = stack()

# %%
while True:
    cmd = tuple(input().split())
    match cmd[0]:
        case "push":
            num = int(cmd[1])
            print(s.push(num))

        case "pop":
            print(s.pop())

        case "back":
            print(s.back())

        case "size":
            print(s.size())
        
        case "clear":
            print(s.clear())
        
        case "exit":
            print('bye')
            break


