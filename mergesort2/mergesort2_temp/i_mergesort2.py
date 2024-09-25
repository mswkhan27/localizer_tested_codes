def mergeSort(nlist):
    c[15] += 1
    if len(nlist) > 1:
        c[1] += 1
        if len(nlist) % 2 == 0:
            c[2] += 1
            mid = len(nlist) // 2
            lefthalf = nlist[:mid]
            righthalf = nlist[mid:]

            mergeSort(lefthalf)
            mergeSort(righthalf)
            i = j = k = 0

            while i < len(lefthalf) and j < len(righthalf):
                c[3] += 1
                if lefthalf[i] < righthalf[j]:
                    c[4] += 1
                    nlist[k] = lefthalf[i]
                    i += 1
                else:
                    c[5] += 1
                    nlist[k] = righthalf[j]
                    j += 1
                k += 1

            while i < len(lefthalf):
                c[6] += 1
                nlist[k] = lefthalf[i]
                i += 1
                k += 1

            while j < len(righthalf):
                c[7] += 1
                nlist[k] = righthalf[j]
                j += 1
                k += 1
       
        else:
            c[8] += 1
            mid = len(nlist) // 2
            lefthalf = nlist[:mid]
            righthalf = nlist[mid:]

            mergeSort(lefthalf)
            mergeSort(righthalf)
            i = j = k = 0

            while i < len(lefthalf) and j < len(righthalf):
                c[9] += 1
                if lefthalf[i] < righthalf[j]: # error
                    c[10] += 1
                    nlist[k] = lefthalf[i]
                    i += 1
                else:
                    c[11] += 1
                    nlist[k] = righthalf[j]
                    j += 1
                k += 1 

            while i < len(lefthalf):
                c[12] += 1
                nlist[k] = lefthalf[i]
                i += 1
                k += 1

            while j < len(righthalf):
                c[13] += 1
                nlist[k] = righthalf[j]
                j += 1
                k += 1
    else:
        c[14] += 1
        pass
