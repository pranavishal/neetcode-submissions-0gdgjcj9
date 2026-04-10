class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split('/')
        print(components)
        stack = []
        for component in components:
            if len(component) == 0 or component == ".":
                continue
            elif component == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(component)
        
        return "/" + "/".join(stack)

        