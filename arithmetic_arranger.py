def arithmetic_arranger(problems, solve = False) :
    split_problems = []
    for problem in problems :
        split_problems.append(problem.split())

    arranged_problems = None
    arranged_problems = check_inputs(split_problems)
    if arranged_problems is not None : return arranged_problems

    formatted_problems = format_problems(split_problems)

    if solve :
        formatted_problems = add_solutions(formatted_problems, split_problems)

    arranged_problems = arrange_problems(formatted_problems)

    return arranged_problems


def add_solutions(formatted_list, split_list) :
    for index in range(len(split_list)) :
        problem = split_list[index]
        if problem[1] == '+' :
            solution = solve_plus(problem)
        else :
            solution = solve_minus(problem)
        solution = solution.rjust(len(formatted_list[index][2]))
        formatted_list[index].append(solution)
    return formatted_list


def solve_plus(problem) :
    return str(
        int(problem[0]) + int(problem[2])
        )


def solve_minus(problem) :
    return str(
        int(problem[0]) - int(problem[2])
        )


def format_problems(two_d_arr) :
    formatted_problems = []
    for equation in two_d_arr :
        width = find_equation_width(equation[0], equation[2])
        spacer = "-" * width
        first_line = equation[0].rjust(width)
        second_line = equation[1] + equation[2].rjust(width - 1)
        formatted_problems.append([first_line, second_line, spacer])
    return formatted_problems


def arrange_problems (formatted_arr) :
    arranged_problems = ""

    for num_ind in range(len(formatted_arr[0])) :
        for eq_ind in range(len(formatted_arr)) :
            if eq_ind == len(formatted_arr) - 1 :
                arranged_problems += formatted_arr[eq_ind][num_ind] + "\n"
            else :
                arranged_problems += formatted_arr[eq_ind][num_ind] + (" " * 4)

    arranged_problems = arranged_problems.rstrip()
    return arranged_problems


def find_equation_width(first_number, second_number) :
  first_length = len(first_number)
  second_length = len(second_number)
  if first_length > second_length :
    return first_length + 2
  else :
    return second_length + 2


def check_inputs(two_d_arr) :
    err_msg = None
    err_msg = only_five_problems(two_d_arr)
    if err_msg is not None : return err_msg

    for problem in two_d_arr :
        err_msg = correct_operator(problem)
        if err_msg is not None : return err_msg
        err_msg = check_both_digits(problem)
        if err_msg is not None : return err_msg

    return err_msg


def only_five_problems(two_d_arr) :
    if len(two_d_arr) > 5 :
        return "Error: Too many problems."
    else :
        return None


def correct_operator(problem) :
    if problem[1] != '+' and problem[1] != '-' :
        return "Error: Operator must be '+' or '-'."
    else :
        return None


def check_both_digits(problem):
    error_msg = None
    for digits_string in [problem[0], problem[2]] :
        error_msg = max_four_digits(digits_string)
        if error_msg is None :
          error_msg = integers_only(digits_string)
    return error_msg


def max_four_digits(digits_string) :
    if len(digits_string) > 4 :
        return "Error: Numbers cannot be more than four digits."
    else :
        return None


def integers_only(digits_string) :
    try :
        digits_string = int(digits_string)
    except :
        return "Error: Numbers must only contain digits."
    else :
        return None
