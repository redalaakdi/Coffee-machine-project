def format_name(first_name, last_name):
    fromated_f_name = first_name.title()
    fromated_l_name = last_name.title()
    return f"{fromated_f_name} {fromated_l_name}" #becomes the output
print(format_name("mohammed reda", "LAAKDI"))

def function_1(text):
    return text + text

def function_2(text):
    return text.title()
output = function_2(function_1("hello"))
print(output)

