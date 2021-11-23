def quicksort(tab):

    left = []
    equal = []
    right = []

    if len(tab) > 1:
        pivot = tab[0]
        for x in tab:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                right.append(x)

        return quicksort(left) + equal + quicksort(right)
    
    else:
        return tab

tab = [12,154,3,485,22,354,6,312,125,5452,12,212,5,36]
print(quicksort(tab))