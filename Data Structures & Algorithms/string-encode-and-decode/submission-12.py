class Solution:

    def encode(self, strs: List[str]) -> str:
        decode_str = ""
        for s in strs:
            s_len = len(s)
            decode_str += str(s_len) + "#" + s
        return decode_str

    def decode(self, s: str) -> List[str]:
        strs = []
        in_word = False
        current_num_s = ""
        chars_left = -1
        curr_word = ""
        for i, letter in enumerate(s):
            if not in_word:
                if letter.isdigit():
                    current_num_s += letter
                elif letter == "#":
                    chars_left = int(current_num_s)
                    current_num_s = ""
                    in_word = True
                    if chars_left == 0:
                        in_word = False
                        strs.append("")
            else:
                if chars_left > 1:
                    curr_word += letter
                    chars_left -= 1
                elif chars_left == 1:
                    in_word = False
                    curr_word += letter
                    strs.append(curr_word)
                    curr_word = ""
        return strs
                

