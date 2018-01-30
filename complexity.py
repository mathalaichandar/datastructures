import random
import timeit

def uniqueCheckFast(aList):
    """
    Return True if aList contains any duplicates. Its Contents are
    altered and completes in O(n) time with O(n) Space requirement.
    """
    check = set()
    for v in aList:
        if v in check:
            return True
        check.add(v)
    return False

def uniqueCheckSlow(aList):
    """
    Return True if aList contains any duplicates. Its contents are
    altered and comples in O(n^2) time with no space requiement.
    """
    for i in range(len(aList)-1):
        for j in range(i+1,len(aList)):
            if aList[i] == aList[j]:
                return True
    return False

if __name__ == '__main__':
    print("N\tSlow      \tFast")
    for trial in(2**_ for _ in range(1,12)):
        numbers = [random.random() for _ in range(trial)]
        mSlow = timeit.timeit(stmt="uniqueCheckSlow(numbers)",
                        setup="import random\nfrom __main__ import uniqueCheckSlow, numbers",
                        number=1000)
        mfast = timeit.timeit(stmt="uniqueCheckFast(numbers)",
                        setup="import random\nfrom __main__ import uniqueCheckFast, numbers",
                        number=1000)
        print("{0:d}\t{1:f}\t{2:f}".format(trial,mSlow,mfast))
