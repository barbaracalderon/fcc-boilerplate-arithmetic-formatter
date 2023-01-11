def arithmetic_arranger(problems_input: list, show_results=False):
    if len(problems_input) > 5:
        return 'Error: Too many problems.'
    first_problem = problems_input[0]
    first_line = second_line = dashes_line = results_line = ''
    for problem in problems_input:
        problem_parts = problem.split()
        first_number, operator, second_number = problem_parts[0], problem_parts[1], problem_parts[2]
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        problem_parts = problem.split(f' {operator} ')
        for problem_part in problem_parts:
            number = ''
            for char in problem_part:
                if char.isalpha():
                    return "Error: Numbers must only contain digits."
                number += char
            if len(number) > 4:
                return "Error: Numbers cannot be more than four digits."

        result_value = ''
        if '+' in operator:
            result_value = str(int(first_number) + int(second_number)).strip()
        elif '-' in operator:
            result_value = str(int(first_number) - int(second_number)).strip()

        length = max(len(first_number), len(second_number))
        if problem == first_problem:
            first_line += str(first_number).rjust(length + 2)
            second_line += operator + ' ' + str(second_number).rjust(length)
            dashes_line += '-' * (length + 2)
            results_line += str(result_value).rjust(length + 2)
        else:
            first_line += str(first_number).rjust(length + 6)
            second_line += operator.rjust(5) + ' ' + str(second_number.rjust(length))
            dashes_line += '    ' + '-' * (length + 2)
            results_line += '    ' + str(result_value).rjust(length + 2)

    if show_results is True:
        string = first_line + "\n" + second_line + "\n" + dashes_line + "\n" + results_line
    else:
        string = first_line + "\n" + second_line + "\n" + dashes_line
    return string
