def encode(string):
    if not string:
        return ""

    result = []
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            if count > 1:
                result.append(str(count))
            result.append(string[i - 1])
            count = 1

    # handle last run
    if count > 1:
        result.append(str(count))
    result.append(string[-1])

    return "".join(result)


def decode(string):
    result = []
    count = ""

    for ch in string:
        if ch.isdigit():
            count += ch
        else:
            if count:
                result.append(ch * int(count))
                count = ""
            else:
                result.append(ch)
    return "".join(result)
