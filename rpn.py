
import operator
import readline
from termcolor import colored, cprint

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}

def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)


        #print(stack)
    if len(stack) != 1:
        raise TypeError('malformed input')
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        if result > 0:
            cprint(result, 'magenta')
        elif result < 0:
            cprint(result, 'green')
        else:
            cprint(result, 'blue')

if __name__ == '__main__':
    main()

def greeting():
    hello = "Guten Tag!"
    print(hello)

def story(arg):
    story = "Once upon a time there was"
    story += arg1
    return story

def linearFunction(x, m, b):
    y = m*x
    y += b
    return y

def slope(rise, run):
    slope = rise / run
    return slope

def grade(hw, exam, pres):
    grade = (hw * 0.2)
    grade += (exam * 0.5)
    grade += (pres * 0.3)
    return grade
