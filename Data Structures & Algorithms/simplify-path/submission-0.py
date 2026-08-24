class Solution:
    def simplifyPath(self, path: str) -> str:
        # '.' -> skip
        # '..' -> previous
        # 
        stack = []
        paths = path.split("/")

        print(paths)
        for path in paths:
            if path == "..":
                if stack:
                    stack.pop()
            elif path != "" and path != '.':
                stack.append(path)
        # print(stack)
        return "/" + "/".join(stack)