

def covert(s: str, num_rows: int) -> str:
    res = [""] * num_rows

    index = -1
    flag = True
    for i in range(len(s)):
        if flag:
            index += 1
            res[index] += s[i]
            if index == num_rows - 1:
                flag = False
        else:
            index -= 1
            res[index] += s[i]
            if index == 0:
                flag = True

    return "".join(res)


print(covert("PAYPALISHIRING", 3))



