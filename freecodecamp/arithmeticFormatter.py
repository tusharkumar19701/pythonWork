def arithmetic_arranger(problems, show_answers=False):
    ans = ""
    if len(problems) > 5:
        return 'Error: Too many problems.'
        
    
    for prob in problems:
        if '+' in prob:
            res = prob.split('+')
        elif '-' in prob:
            res = prob.split('-')
        else:
            return "Error: Operator must be '+' or '-'."
        

        if not res[0].strip().isdigit() or not res[1].strip().isdigit():
            return 'Error: Numbers must only contain digits.'
        
        if (res[0].strip().isnumeric() and len(res[0].strip()) <= 4) and (res[1].strip().isnumeric() and len(res[1].strip()) <= 4):
            maxi = max(len(res[0].strip()),len(res[1].strip()))
            maxspace = maxi + 2
            space = maxspace-len(res[0].strip())

            ans += ' ' * space
            
            ans += res[0].strip()
            ans += ' '*4
        else:
            return "Error: Numbers cannot be more than four digits."

    ans = ans.rstrip() + '\n'
    for prob in problems:
        if '+' in prob:
            res = prob.split('+')
            sign = '+'
        elif '-' in prob:
            res = prob.split('-')
            sign = '-'
        else:
            return "Error: Operator must be '+' or '-'."
        
        if res[1].strip().isnumeric() and len(res[1].strip()) <= 4:
            ans += sign
            maxi = max(len(res[0].strip()),len(res[1].strip()))
            maxspace = maxi+2
            space = maxspace - len(res[1].strip()) - 1
            for i in range(space):
                ans += ' '
            
            ans += res[1].strip()
            for i in range(4):
                ans += ' '

    ans = ans.rstrip() + '\n'
    for prob in problems:
        if '+' in prob:
            res = prob.split('+')
            sign = '+'
        elif '-' in prob:
            res = prob.split('-')
            sign = '-'
        else:
            return "Error: Operator must be '+' or '-'."
            

        maxi = max(len(res[0].strip()),len(res[1].strip()))
        maxspace = maxi+2

        for i in range(maxspace):
            ans += '-'
        
        for i in range(4):
            ans += ' '
        
    ans = ans.rstrip()

    if show_answers:
        ans += '\n'
        for prob in problems:
            if '+' in prob:
                res = prob.split('+')
                obs = int(res[0].strip()) + int(res[1].strip())
            else:
                res = prob.split('-')
                obs = int(res[0].strip()) - int(res[1].strip())
            
            maxi = max(len(res[0].strip()),len(res[1].strip()))
            maxspace = maxi + 2
            ans += str(obs).rjust(maxspace)
            ans += ' '*4
        
        ans = ans.rstrip()
    return ans

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
# print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
