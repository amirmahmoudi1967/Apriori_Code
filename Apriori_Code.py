# -*- coding: utf-8 -*-
"""
@author: Amir Mahmoudi
"""

import itertools
def Appriori(ensemble,occurence):
    L = []
    #We create the first singleton's list
    countL = {}
    for individu in ensemble:
        for singleton in individu:
            if singleton in countL.keys():
                countL[singleton]+=1
            else:
                countL[singleton]=1
    L.append([l for l in countL.keys() if countL[l]>=occurence])
    
    k = 1
    #Program's main loop
    while L[k-1] and len(L[k-1])!=1:
        #L_temp is used to save what L[k-1] is containing (an integer list)
        if k == 1:
            L_temp = list(dict.fromkeys([item for item in L[k-1]]))#We use the formula my_list = list(dict.fromkeys(my_list))  to delete the copies, [1,2,3,4,5,5,5,2,3] becomes [1,2,3,4,5]
        else:
            L_temp = list(dict.fromkeys([item for sublist in L[k-1] for item in sublist])) 
        C = [list(c) for c in itertools.combinations(L_temp,k+1)]#It's the C in the Apriori Algorithm
        L.append([])
        for c in C:
            countC = 0#This variable avoids the creation of set D since if C it is not in set countC will be equal to 0 and will not be added to L[k].
            for sEnsemble in ensemble:
                if all(item in sEnsemble for item in c):
                    countC+=1
            if countC>=3:
                L[k].append(c)
        k+=1
    return L

t1 = [[1,2,5],[1,3,5],[1,2],[1,2,3,4,5],[1,2,4,5],[2,3,5],[1,5]]
print(Appriori(t1,3))