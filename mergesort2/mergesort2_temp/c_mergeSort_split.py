from src.utils import Count 

def mergeSort(nlist):
    Count.incC(15)
    if len(nlist) > 1:
        Count.incC(1)
        if len(nlist) % 2 == 0:
            Count.incC(2)
            mid = len(nlist) // 2
            lefthalf = nlist[:mid]
            righthalf = nlist[mid:]
            mergeSort(lefthalf)
            mergeSort(righthalf)
            i = j = k = 0
            while i < len(lefthalf) and j < len(righthalf):
                Count.incC(3)
                if lefthalf[i] < righthalf[j]:
                    Count.incC(4)
                    nlist[k] = lefthalf[i]
                    i += 1
                else:
                    Count.incC(5)
                    nlist[k] = righthalf[j]
                    j += 1
                k += 1
            while i < len(lefthalf):
                Count.incC(6)
                nlist[k] = lefthalf[i]
                i += 1
                k += 1
            while j < len(righthalf):
                Count.incC(7)
                nlist[k] = righthalf[j]
                j += 1
                k += 1
        else:
            Count.incC(8)
            mid = len(nlist) // 2
            lefthalf = nlist[:mid]
            righthalf = nlist[mid:]
            mergeSort(lefthalf)
            mergeSort(righthalf)
            i = j = k = 0
            while i < len(lefthalf) and j < len(righthalf):
                Count.incC(9)
                if lefthalf[i] < righthalf[j]: # error
                    Count.incC(10)
                    nlist[k] = lefthalf[i]
                    i += 1
                else:
                    Count.incC(11)
                    nlist[k] = righthalf[j]
                    j += 1
                k += 1 
            while i < len(lefthalf):
                Count.incC(12)
                nlist[k] = lefthalf[i]
                i += 1
                k += 1
            while j < len(righthalf):
                Count.incC(13)
                nlist[k] = righthalf[j]
                j += 1
                k += 1
    else:
        Count.incC(14)
        pass
