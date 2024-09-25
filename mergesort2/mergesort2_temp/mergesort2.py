def mergeSort(nlist):
    if len(nlist) > 1:
        if len(nlist) % 2 == 0:
            mid = len(nlist) // 2
            lefthalf = nlist[:mid]
            righthalf = nlist[mid:]

            mergeSort(lefthalf)
            mergeSort(righthalf)
            i = j = k = 0

            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    nlist[k] = lefthalf[i]
                    i += 1
                else:
                    nlist[k] = righthalf[j]
                    j += 1
                k += 1

            while i < len(lefthalf):
                nlist[k] = lefthalf[i]
                i += 1
                k += 1

            while j < len(righthalf):
                nlist[k] = righthalf[j]
                j += 1
                k += 1
       
        else:
            mid = len(nlist) // 2
            lefthalf = nlist[:mid]
            righthalf = nlist[mid:]

            mergeSort(lefthalf)
            mergeSort(righthalf)
            i = j = k = 0

            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]: # error
                    nlist[k] = lefthalf[i]
                    i += 1
                else:
                    nlist[k] = righthalf[j]
                    j += 1
                k += 1 

            while i < len(lefthalf):
                nlist[k] = lefthalf[i]
                i += 1
                k += 1

            while j < len(righthalf):
                nlist[k] = righthalf[j]
                j += 1
                k += 1
    else:
        pass
