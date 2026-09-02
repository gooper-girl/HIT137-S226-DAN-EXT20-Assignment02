import os

def tokenize(expression):
    tokens = []
    i = 0
    lenght = len(expression)
    
    while i < lenght:
        char = expression[i]
        
        if char == " " or char == "\t":
            i = i + 1
            
        elif char.isdigit():
            start = i
            while i < lenght and expression[i].isdigit():
                i = i + 1
            if i < lenght and expression[i] == "." and i + 1 < lenght and expression[i + 1].isdigit():
                i = i + 1
                while i < lenght and expression[i].isdigit():
                    i = i + 1
            number_text = expression[start:i]
            tokens.append({"type": "NUM", "value": number_text})
            
        elif char in "+-*/%^":
            tokens.append({"type": "OP", "value": char})
            i = i + 1
            
        elif char == "(":
            tokens.append({"type": "LPAREN", "value": "("})
            i = i + 1
            
        elif char == ")":
            tokens.append({"type": "RPAREN", "value": ")"})
            i = i + 1
            
        else:
            return None
            
    tokens.append({"type": "END", "value": ""})
    return tokens
    
def tokens_to_string(tokens):
    pieces = []
    for token in tokens:
        if token["type"] == "END":
            pieces.append("[END]")
        else:
            pieces.append("[" + token["type"] + ":" + token["value"] + "]")
    return " ".join(pieces)