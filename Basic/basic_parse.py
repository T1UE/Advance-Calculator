
Codex = str.maketrans({"+":"+", "-":"-", "x":"*", "X":"*", "/":4, "^":"**", "R":"%", "r":"%"})
# deCodex = {"+":"+", "-":"-", "x":"*", "X":"*", "/":4, "^":"**", "R":"%", "r":"%"}
indexes = []
split_expression = []
def Parser(string, expression):
    for i in range(len(string)):
        if string[i] in Codex:
            indexes.append(i)
    indexes = expression.split()

