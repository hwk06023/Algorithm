import sys

input = sys.stdin.readline

while True:
    commands = []
    while True:
        command = input().rstrip()
        if command == 'QUIT':
            break
        elif command == 'END':
            break
        else:
            commands.append(command)

    if command == 'QUIT':
        break

    n = int(input())
    for _ in range(n):
        stack = []
        stack.append(int(input()))
        error = False
        for command in commands:
            if command[:3] == 'NUM':
                stack.append(int(command[4:]))
            elif command == 'POP':
                if len(stack) == 0:
                    error = True
                    break
                else:
                    stack.pop()
            elif command == 'INV':
                if len(stack) == 0:
                    error = True
                    break
                else:
                    stack[-1] *= -1
            elif command == 'DUP':
                if len(stack) == 0:
                    error = True
                    break
                else:
                    stack.append(stack[-1])
            elif command == 'SWP':
                if len(stack) < 2:
                    error = True
                    break
                else:
                    stack[-1], stack[-2] = stack[-2], stack[-1]
            elif command == 'ADD':
                if len(stack) < 2:
                    error = True
                    break
                else:
                    stack.append(stack.pop() + stack.pop())
            elif command == 'SUB':
                if len(stack) < 2:
                    error = True
                    break
                else:
                    stack.append(-stack.pop() + stack.pop())
            elif command == 'MUL':
                if len(stack) < 2:
                    error = True
                    break
                else:
                    stack.append(stack.pop() * stack.pop())
            elif command == 'DIV':
                if len(stack) < 2:
                    error = True
                    break
                else:
                    a = stack.pop()
                    b = stack.pop()
                    if a == 0:
                        error = True
                        break
                    else:
                        if a * b < 0:
                            if b < 0:
                                stack.append(-((-b) // a))
                            else:
                                stack.append(-(b // (-a)))
                        else:
                            stack.append(b // a)
            elif command == 'MOD':
                if len(stack) < 2:
                    error = True
                    break
                else:
                    a = stack.pop()
                    b = stack.pop()
                    if a == 0:
                        error = True
                        break
                    else:
                        if b < 0 and a > 0:
                            stack.append(-((-b) % a))
                        elif b < 0 and a < 0:
                            stack.append(-((-b) % (-a)))
                        elif b > 0 and a < 0:
                            stack.append(b % (-a))
                        else:
                            stack.append(b % a)
        if error:
            print('ERROR')
        else:
            if len(stack) == 1 and abs(stack[0]) <= 10 ** 9:
                print(stack[0])
            else:
                print('ERROR')
    print()
