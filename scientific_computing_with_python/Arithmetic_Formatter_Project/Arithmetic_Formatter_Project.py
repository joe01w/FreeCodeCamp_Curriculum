def arithmetic_arranger(problems, show_answers=False):
    # Error Checking
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line = []
    second_line = []
    dashes = []
    solutions = []
    
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid format."
        
        num1, operator, num2 = parts
        
        # Check if the operator is valid
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        
        # Check if numbers contain only digits
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        
        # Check the length of the numbers
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Calculate the width of the problem
        width = max(len(num1), len(num2)) + 2
        
        # Prepare each line
        first_line.append(num1.rjust(width))
        second_line.append(operator + ' ' + num2.rjust(width - 2))
        dashes.append('-' * width)
        
        # Calculate the solution if required
        if show_answers:
            if operator == '+':
                solution = str(int(num1) + int(num2))
            else:
                solution = str(int(num1) - int(num2))
            solutions.append(solution.rjust(width))
    
    # Join the lines with 4 spaces between problems
    arranged_problems = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(dashes)
    
    if show_answers:
        arranged_problems += '\n' + '    '.join(solutions)
    
    return arranged_problems