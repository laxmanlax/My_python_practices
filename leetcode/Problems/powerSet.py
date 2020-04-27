"""
l = [1, 2, 3]
powerset(l) = [[], [1], [2], [3], [1,2], [1,3], [2,3],[1,2,3]]
"""
l = [1, 2, 3]


def powerset(xs):
    result = [[]]
    for x in xs:
        newsubsets = [subset + [x] for subset in result]
        result.extend(newsubsets)
    return result


for i in powerset(l):
    if sum(i) == 3:
        print i


def powerset2(orig, newset):
    if orig == []:
        return [newset]
    else:
        res = []
        for s in powerset2(orig[1:], newset+[orig[0]]):
            res.append(s)
        for s in powerset2(orig[1:], newset):
            res.append(s)
    return res


def powerset3(orig, newset):
    if orig == []:
        yield newset
    else:
        for s in powerset3(orig[1:], newset+[orig[0]]):
            yield s
        for s in powerset3(orig[1:], newset):
            yield s


def powerset4(lst):
    if len(lst) <= 1:
        yield lst
        yield []
    else:
        for x in powerset4(lst[1:]):
            yield [lst[0]] + x
            yield x


print powerset(l), "\n"
print powerset2(l, []), "\n"
print list(powerset3(l, [])), "\n"
print list(powerset4(l)), "\n"
