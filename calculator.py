import math


def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero!"
        return num1 / num2
    elif operator == '^':
        return num1 ** num2
    else:
        return "Error: Invalid operator!"


def calculate_function(func, value):
    try:
        if func == 'sqrt':
            if value < 0:
                return "Error: Cannot take square root of a negative number!"
            return math.sqrt(value)
        elif func == 'sin':
            return math.sin(math.radians(value))
        elif func == 'cos':
            return math.cos(math.radians(value))
        elif func == 'tan':
            if math.cos(math.radians(value)) == 0:
                return "Error: Tangent undefined at this angle!"
            return math.tan(math.radians(value))
        else:
            return "Error: Invalid function!"
    except ValueError:
        return "Error: Invalid value for this function!"


def tokenize(expression):
    tokens = []
    i = 0
    last_was_number = False
    while i < len(expression):
        if expression[i].isspace():
            i += 1
            continue
        if expression[i].isdigit() or expression[i] == '.':
            num = ''
            while i < len(expression) and (expression[i].isdigit() or expression[i] in '.'):
                num += expression[i]
                i += 1
            try:
                number = float(num.replace(',', '.'))
                if last_was_number:
                    tokens.append('*')
                tokens.append(number)
                last_was_number = True
            except ValueError:
                return None
            continue
        if expression[i] in '+-*/^()':
            tokens.append(expression[i])
            i += 1
            last_was_number = False
            continue
        if expression[i].isalpha():
            func = ''
            while i < len(expression) and expression[i].isalpha():
                func += expression[i]
                i += 1
            if func.lower() in ['sqrt', 'sin', 'cos', 'tan']:
                if i < len(expression) and expression[i] == '(':
                    i += 1
                    value = ''
                    paren_count = 1
                    while i < len(expression) and paren_count > 0:
                        if expression[i] == '(':
                            paren_count += 1
                        elif expression[i] == ')':
                            paren_count -= 1
                        if paren_count > 0:
                            value += expression[i]
                        i += 1
                    if paren_count != 0:
                        return None
                    try:
                        val = float(value.replace(',', '.'))
                        result = calculate_function(func.lower(), val)
                        if isinstance(result, str):
                            return None
                        if last_was_number:
                            tokens.append('*')
                        tokens.append(result)
                        last_was_number = True
                    except ValueError:
                        return None
                else:
                    return None
            else:
                return None
            continue
        i += 1
    return tokens


def apply_operator(operators, values):
    if not operators:
        return
    op = operators.pop()
    if len(values) < 2:
        return "Error: Not enough values for operation!"
    num2 = values.pop()
    num1 = values.pop()
    result = calculate(num1, num2, op)
    values.append(result)


def precedence(op):
    if op in ['+', '-']:
        return 1
    if op in ['*', '/']:
        return 2
    if op == '^':
        return 3
    return 0


def evaluate_expression(expression):
    tokens = tokenize(expression)
    if tokens is None:
        return "Error: Invalid expression format!"

    values = []
    operators = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if isinstance(token, float):
            if i > 0 and tokens[i - 1] == '-' and (i == 1 or tokens[i - 2] in ['+', '-', '*', '/', '^', '(']):
                values[-1] = -token
            else:
                values.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                result = apply_operator(operators, values)
                if isinstance(result, str):
                    return result
            if operators:
                operators.pop()
        elif token in ['+', '-', '*', '/', '^']:
            while (operators and operators[-1] != '(' and
                   (precedence(operators[-1]) > precedence(token) or
                    (precedence(operators[-1]) == precedence(token) and token != '^'))):
                result = apply_operator(operators, values)
                if isinstance(result, str):
                    return result
            operators.append(token)
        i += 1

    while operators:
        if operators[-1] == '(':
            return "Error: Mismatched parentheses!"
        result = apply_operator(operators, values)
        if isinstance(result, str):
            return result

    if len(values) != 1:
        return "Error: Invalid expression!"
    return values[0]


print("Welcome to the Advanced Calculator!")
print("I can do the following operations:")
print("Addition: 2 + 3 = 5")
print("Subtraction: 5 - 3 = 2")
print("Multiplication: 4 * 3 = 12")
print("Division: 6 / 2 = 3")
print("Exponentiation: 2 ^ 3 = 8")
print("Square root: sqrt(4) = 2")
print("Trigonometric functions (in degrees):")
print("  sin(30) = 0.5")
print("  cos(45) = 0.707...")
print("  tan(45) = 1")
print("Order of operations:")
print("  1. Parentheses: (2 + 3) * 4")
print("  2. Functions: sqrt(4), sin(30)")
print("  3. Exponentiation: 2 ^ 3")
print("  4. Multiplication and Division: 4 * 3, 6 / 2")
print("  5. Addition and Subtraction: 2 + 3, 5 - 3")
print("Enter your expression with or without spaces (e.g., '2 + 3' or '2+3') or a function like 'sin(30)'.")

while True:
    print("Enter a math expression or function (or 'q' to quit):")
    expression = input().strip()
    if expression.lower() == 'q':
        print("Exiting program...")
        break

    if any(func in expression.lower() for func in ['sqrt', 'sin', 'cos', 'tan']) and (
            '(' not in expression or ')' not in expression):
        print("Error: Invalid operation! Use +, -, *, /, ^, or functions like sqrt(4), sin(30) with parentheses")
        continue

    operators = ['+', '-', '*', '/', '^']
    if not any(op in expression for op in operators) and not any(
            func in expression.lower() for func in ['sqrt', 'sin', 'cos', 'tan']):
        print("Error: Invalid operation! Use +, -, *, /, ^, or functions like sqrt(4), sin(30) with parentheses")
        continue

    result = evaluate_expression(expression)
    if isinstance(result, str):
        print(f"Result: {result}")
    else:
        print(f"Result: {result:.6f}")