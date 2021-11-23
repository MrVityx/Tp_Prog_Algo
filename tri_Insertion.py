def insertion(tab): 
    for i in range(1, len(tab)): 
        k = tab[i] 
        j = i-1
        while j >= 0 and k <tab[j] : 
                tab[j+1] = tab[j] 
                j -= 1
        tab[j + 1] = k
    return tab

tab = [98,22,15,32,2,74,63,70]
print(insertion(tab))