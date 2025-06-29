# in this prob we have the input of 3[a]2[ab]
# the op should be aaaabab
def scale_opperation(s : str) -> str:
    num_stack=[]
    str_stack=[]
    current_num = 0
    current_ele = ""
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            num_stack.append(current_num)
            str_stack.append(current_ele)
            current_num = 0
            current_ele = ""
        elif char == ']':
            prev_num = num_stack.pop()
            prev_str = str_stack.pop()
            current_ele = prev_str + current_ele * prev_num
        else:
            current_ele = current_ele + char
            
    return current_ele
        




letters = scale_opperation("3[a]")
print(letters)
