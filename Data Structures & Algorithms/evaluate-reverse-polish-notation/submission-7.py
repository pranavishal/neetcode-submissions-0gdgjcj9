class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        curr_vals = []
        for token in tokens:
            if token == "+":
                val_2 = curr_vals.pop()
                val_1 = curr_vals.pop()
                curr_vals.append(val_1 + val_2)
                print(str(val_1) + "+" + str(val_2))
            elif token == "-":
                val_2 = curr_vals.pop()
                val_1 = curr_vals.pop()
                curr_vals.append(val_1 - val_2)
                print(str(val_1) + "-" + str(val_2))
            elif token == "*":
                val_2 = curr_vals.pop()
                val_1 = curr_vals.pop()
                curr_vals.append(val_1 * val_2)
                print(str(val_1) + "*" + str(val_2))
            elif token == "/":
                val_2 = curr_vals.pop()
                val_1 = curr_vals.pop()
                curr_vals.append(int(val_1 / val_2))
                print(str(val_1) + "//" + str(val_2))
            else:
                curr_vals.append(int(token))
        
        return curr_vals[0]