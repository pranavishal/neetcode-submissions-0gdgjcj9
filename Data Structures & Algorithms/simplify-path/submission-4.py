class Solution:
    def simplifyPath(self, path: str) -> str:
        path_stack = []
        for i, p in enumerate(path):
            if i == 0 or p != "/":
                path_stack.append(p)
                continue
            if path_stack[-1] == '/':
                continue
            dot_count = 0
            while path_stack and path_stack[-1] == ".":
                dot_count += 1
                path_stack.pop()

            if dot_count == 2:
                print(path_stack)
                path_stack.pop()
                while path_stack and path_stack[-1] != "/":
                    path_stack.pop()
                if path_stack:
                    path_stack.pop()
            
            elif dot_count == 1 and path_stack and path_stack[-1] == "/":
                path_stack.pop()

            else:
                for i in range(dot_count):
                    path_stack.append('.')
            
            path_stack.append(p)

        while path_stack and path_stack[-1] == "/":
            path_stack.pop()
        
        dot_count = 0
        while path_stack and path_stack[-1] == ".":
            dot_count += 1
            path_stack.pop()

        if dot_count == 2:
            print(path_stack)
            path_stack.pop()
            while path_stack and path_stack[-1] != "/":
                path_stack.pop()
            if path_stack:
                path_stack.pop()
            
        elif dot_count == 1 and path_stack and path_stack[-1] == "/":
            path_stack.pop()

        else:
            for i in range(dot_count):
                path_stack.append('.')
        
        if len(path_stack) == 0:
            return "/"

        return "".join(path_stack)            




        