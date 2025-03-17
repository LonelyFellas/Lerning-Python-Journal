import typing as t

T = t.TypeVar('T')

def chunk(array: t.Sequence[T], size=1) -> t.List[t.Sequence[T]]:
    if not isinstance(array, list):
        raise TypeError('array must be a list')
    n = len(array)
    if n <= size:
        return [array]

    res = []
    temp = []
    count = 0

    for (i, it) in enumerate(array):
        temp.append(it)
        count += 1
        if count >= size or i == n-1:
            res.append(temp)
            temp = []
            count = 0

    return res