import re
strs = input("Enter expression: ")
tokens = re.findall(r'\w+|[;=+\-*/()]|\d+', strs)
op = ['+', '-', '*', '/', '=']
identifier_dict = {}
operator_count = 1
identifier_count = 1
constant_count = 1
for token in tokens:
    if token not in op and token != ';' and not token.isdigit():
        if token not in identifier_dict:
            identifier_dict[token] = f"Identifier_{identifier_count}"
            identifier_count += 1
        print(token," : ",identifier_dict[token])
    elif token in op:
        print(token," : ",f"Operator_{operator_count}")
        operator_count += 1
    elif token == ';':
        print(token," : ","Delimiter")
    elif token.isdigit():
        print(token," : ",f"Constant_{constant_count}")
        constant_count += 1