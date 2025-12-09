from functools import reduce


def valid(answer, formula):
    result = []
    for part in formula:
        if len(part) > 1 and part[0] in answer and answer[part[0]] == 0:
            return False
        if part[-1] in answer:
            result.append(answer[part[-1]])
    if len(result) < len(formula):
        return True
    return sum(result[:-1]) % 10 == result[-1]


def check(answer, formula):
    result = [''.join(str(answer[x]) for x in part) for part in formula]
    result = [int(x) for x in result]
    return sum(result[:-1]) == result[-1]


def dfs(dep, used, answer, letters, formula):
    if not valid(answer, formula):
        return False
    if dep == len(letters):
        return check(answer, formula)
    for number in range(10):
        if used[number]:
            continue
        used[number] = True
        answer[letters[dep]] = number
        if dfs(dep + 1, used, answer, letters, formula):
            return True
        used[number] = False
        answer.pop(letters[dep])
    return False


def solve(puzzle):
    formula = []
    last_digit = set()
    for part in puzzle.split():
        if part == '+' or part == '==':
            continue
        formula.append(part)
        last_digit.add(part[-1])
    letters = reduce(lambda x, y: x | set(y), formula, set())
    if len(letters) > 10:
        return None
    used = [False] * 10
    other_digit = letters - last_digit
    letters = list(last_digit) + list(other_digit)
    answer = {}
    if dfs(0, used, answer, letters, formula):
        return answer
    return None
