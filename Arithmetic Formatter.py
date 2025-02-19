# Find the operation between each problem's operands (assuming + or -)
def find_plus_or_minus(problem):
    if '+' in problem:
        return '+'
    elif '-' in problem:
        return '-'


def one_problem(problem, show_answer=False):
    operation = find_plus_or_minus(problem)
    operands = problem.replace(' ', '').split(operation)
    left_operand, right_operand = operands[0], operands[1]

    # This is the operand digit error check that is used in arithmetic_arranger
    try:
        list(map(int,[left_operand, right_operand]))
    except ValueError:
        return 0

    len_left, len_right = len(left_operand), len(right_operand)
    max_len = max(len_left, len_right)
    dash_offset = max_len + 2

    # This is the digit length check that is used in arithmetic_arranger
    if len_left > 4 or len_right > 4:
        return 1

    print_left_operand = '  ' + left_operand.rjust(max_len)
    print_right_operand = operation + ' ' + right_operand.rjust(max_len)
    print_dashes = '-' * dash_offset
    print_combination = ''

    if show_answer:
        result = str(int(left_operand) + int(right_operand)) if operation == '+' else str(
            int(left_operand) - int(right_operand))
        print_combination = result.rjust(dash_offset)

    return {'left': print_left_operand, 'right': print_right_operand, 'dashes': print_dashes,
            'combination': print_combination}


def arithmetic_arranger(problems, show_answers=False):
    # Error checking
    # Check to see if there are more than 5 problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for problem in problems:
        # Check that all the operations are plus or minus
        if find_plus_or_minus(problem) not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        # Check to see that operands contain only digits
        if one_problem(problem) == 0:
            return 'Error: Numbers must only contain digits.'
        # Check to see that no operand is longer than 4 digits
        if one_problem(problem) == 1:
            return 'Error: Numbers cannot be more than four digits.'

    arranged_problems = [one_problem(problem, show_answers) for problem in problems]

    # Construct each row of the formatted output
    all_lefts = '    '.join(problem['left'] for problem in arranged_problems)
    all_rights = '    '.join(problem['right'] for problem in arranged_problems)
    all_dashes = '    '.join(problem['dashes'] for problem in arranged_problems)
    all_combinations = '    '.join(problem['combination'] for problem in arranged_problems) if show_answers else ''

    # Combine all lines
    arranged_output = f"{all_lefts}\n{all_rights}\n{all_dashes}"
    if show_answers:
        arranged_output += f"\n{all_combinations}"

    return arranged_output


# Example usage
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))