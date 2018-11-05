class sublist:
    EQUAL=0
    SUPERLIST =1
    UNEQUAL =0
    SUBLIST =2

    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
        self.is_sub = self.is_sub(l1, l2)

    def is_sub(self, l1, l2):
        if l1 == l2:
            return self.EQUAL
        elif l1 in list_process(l2, len(l1)):
            return self.SUBLIST
        elif l2 in list_process(l1, len(l2)):
            return self.SUPERLIST
        else:
            return UNEQUAL

    def list_process(lst, len):
        return [lst[i: i + size] for i in range(len(lst) - size + 1)]


def check_lists(l1, l2):
    test = sublist(l1, l2)
    return test.is_sub
