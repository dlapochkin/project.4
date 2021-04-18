def main():
    """
    Main function
    :return: None
    """
    code = list(map(int, input('Введите код Прюфера: ').split()))
    empty = [[] for _ in range(len(code) + 1)]
    mess = prufer(code, [x for x in range(1, len(code)+2)])
    branches = tree(empty, mess)
    matrix(branches, len(branches), len(branches))


def prufer(code, numbers):
    """
    Prüfer code decryption
    :param code: input Prüfer code
    :param numbers: list of numbers in range from 1 to the number of vertices
    :return: decoded tree (in a mess)
    """
    if len(code) == 0:
        return numbers
    v = code.pop(0)
    nums = []
    for number in numbers:
        if number != v and number not in code:
            nums.append(number)
    m = min(nums)
    numbers.remove(m)
    return [(v, m), prufer(code, numbers)]


def tree(branches, mess):
    """
    Creating sorted tree branches
    :param branches: updatable tree branches
    :param mess: decoded tree (in a mess)
    :return: branches of a tree
    """
    if len(mess) == 1:
        return branches
    a, b = mess[0]
    branches[a-1].append(b)
    branches[b-1].append(a)
    return tree(branches, mess[1])


def matrix(branches, n, i):
    """
    Prints adjacency matrix
    :param branches: branches of a tree
    :param n: number of vertices
    :param i: vertex number (depth of a recursion)
    :return: None
    """
    if i == -1:
        return
    if n == i:
        inprint = '   '
        for num in range(1, n+1):
            inprint += '{:<3}'.format(str(num))
        print('\n', inprint, sep='')
        return matrix(branches, n, i-1)
    inprint = '{:<3}'.format(str(n-i))
    for v in range(1, n+1):
        if v in branches[n-i-1]:
            inprint += '{:<3}'.format('1')
        else:
            inprint += '{:<3}'.format('0')
    print(inprint)
    return matrix(branches, n, i-1)


if __name__ == '__main__':
    main()