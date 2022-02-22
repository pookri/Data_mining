

import time
from typing import final
#import tabulate
import collections

def create_combination(comb_size, item_data): 
    original_list= set()
    comb_data = []

    def combination(comb_size,item_data,comb_data):
        if len(comb_data) == comb_size:
            yield comb_data
        elif len(item_data) == 0 : 
            pass
        else:
            item = item_data.pop()
            comb_data.append(item)
            for j in combination(comb_size,item_data[:],comb_data[:]):
                yield j
            comb_data.pop()
            for j in combination(comb_size,item_data[:],comb_data[:]):
                yield j

    for items in item_data: 
        if comb_size == 2: 
            return combination(comb_size, item_data, comb_data)
        else: 
            for inner in items: 
                original_list.add(inner)
    return combination(comb_size, list(original_list), comb_data )
    
def print_itemCount_table(itemDict):
    print("ITEM\t\t\tCOUNT")
    for i in itemDict:
        print("{}\t\t{}".format(i,itemDict[i]))

def print_itemSupport_table(itemDict):
    print("ITEM\t\t\tSUPPORT")
    for i in itemDict:
        print("{}\t\t{}".format(i,itemDict[i]))

def item_support(itemSupport):
    itemSupport1={}
    for i in itemSupport:
        itemSupport1[i]=round(itemSupport[i]/20,2)
    return itemSupport1

""" Giving you each item (single) in a dictionary """
def list_of_keys(comb_size, newItemSupport_Dict):
    newList=[]
    if comb_size <= 2: 
        for key in newItemSupport_Dict:
            newList.append(key)
    else: # Generating single items to add to a list 
        for key in newItemSupport_Dict:
            key = key.replace("'", "")
            keyarr_tmp = key[1:len(key)-1].split(",")
            keyArr = []
            for key_inner in keyarr_tmp:
                key_inner = key_inner.strip()
                keyArr.append(key_inner)
            newList.append(keyArr)
    return newList

def get_comb_data(comb,midlist):
    comb_ans=[]
    for i in create_combination(comb,midlist):
        comb_ans.append(i)
    return comb_ans  

def item_count(c_data,t_data):   
    itemDict2={}
    for j in range(len(c_data)):
        for k in range(len(t_data)):
            trans_set=set(t_data[k])
            comb_set=set(c_data[j])
            if(comb_set.issubset(trans_set)):
                item2=str(comb_set)
                if item2 in itemDict2.keys():
                    itemDict2[item2]=itemDict2[item2] + 1
                else:
                    itemDict2[item2] = 1
    return itemDict2

def remove_items(item_data):
    itemDict3={}
    for i in item_data:
        if(item_data[i]>=minSupport):
            itemDict3[i]=item_data[i]
        else: 
            all_removed_items.append(i)
    return itemDict3 

"""Input: List of single items, Output: list permutation """
def perm(data):
    if len(data)==0:
        yield []
    elif len(data)==1:
        yield data
    else:
        for i in range(len(data)):
            i_data=data[i]
            p_data=data[:i] + data[i+1:]
            for p in perm(p_data):
                yield [i_data]+p
    
def association(data):
    retArr = []
    def isDuplicate(left, right): 
        for ra in retArr:
            if collections.Counter(ra[0]) == collections.Counter(left) and collections.Counter(ra[1]) == collections.Counter(right):
                return True
        return False

    for lt in range(len(data)):
        listOfString = data[lt]
        pointer = 1
        for rt in range(len(listOfString)-1):
            left = listOfString[:pointer]
            right = listOfString[rt+1:]
            #if len(retArr) > 0 and all(x in retArr[rt][0] for x in left) and all(y in retArr[rt][1] for y in right):
            if len(retArr) > 0 and isDuplicate(left, right):
                pass
                #print('they both are already in ret list')
            else: 
                retArr.append([ left , right])
            pointer = pointer +1
    return retArr

def generate_rules(associ_list):
    final_ruleDict={}
    for product in associ_list:
        supp_dict={}
        supp_dict=item_support(item_count([product[0]+product[1]],transaction))
        for i in supp_dict:            
            suppValue1=supp_dict[i]
        #print(suppValue1)
        leftSide=','.join(product[0])
        rightSide=','.join(product[1])
        finalKey=leftSide+' -> '+rightSide
        final_ruleDict[finalKey]=[Calculate_confidence(product[0],product[1]),suppValue1]
    #print_itemCount_table(final_ruleDict)
    return final_ruleDict

def Calculate_confidence(left,right):
    temp1=item_count([left],transaction) 
    temp2=item_count([left+right],transaction)
    for i in temp1:
        temp1Value=temp1[i]
    for j in temp2:
        temp2Value=temp2[j]
    confidence=temp2Value/temp1Value
    return confidence 

def association_rules(finalDict):
    rule_dict={}
    for rule in finalDict:
        confiList=finalDict[rule]
        if confiList[0] >= minConfidence:
            rule_dict[rule]=finalDict[rule] 
    return rule_dict

db1=open('Transaction3.txt')
lines=[]
transaction=[]
itemDict = {}
comb=2
final_answer = {}
all_removed_items = []
minConfidence=float(input('Enter minimum Confidence:'))
minSupport=float(input('Enter minimum Support:'))
starttime=time.time()
for f in db1:
    f = f.rstrip('\n')
    transaction.append(f.split(","))
    line = f.split(",")
    for item in line: 
        if (item in itemDict.keys()):
            itemDict[item] = itemDict[item] + 1
        else: 
            itemDict[item] = 1

newItemSupport_Dict=item_support(itemDict)
itemDict=remove_items(newItemSupport_Dict)
print('transaction',transaction)
print('itemDict')
print(itemDict)
comb=2
cnt=1
while len(itemDict) > 1:
    midlist=[]
    midlist=list_of_keys(comb, itemDict)
    combined_data=get_comb_data(comb,midlist)
    itemDict=item_count(combined_data,transaction)
    newItemSupport_Dict=item_support(itemDict)
    itemDict=remove_items(newItemSupport_Dict)
    final_answer.update(itemDict)
    comb=comb+1
    cnt=cnt+1
print('Printing final answer')
print(final_answer)
# print('Printing all removed items')
# print(all_removed_items)

final_list=list_of_keys(3,final_answer)
print('Frequent item set')
print(final_list)
eachPermList = []
association_list=[]
for each in final_list: 
    for eachPerm in perm(each):
        eachPermList.append(eachPerm)
print('association_list')
association_list=association(eachPermList)
print(association_list)
ruleDict=generate_rules(association_list)
final_ruleDict=association_rules(ruleDict)
print_itemCount_table(final_ruleDict)
db1.close()
endtime=time.time()
print("Time taken by Apriori Algorithm:",endtime-starttime)




"""


def left_right_count(p_list,ass_list):
    temp={}
    temp1={}
    for key in ass_list:
        print(key[0])
        j=key[0]
        temp1.update(item_count([j],transaction))
    print_itemCount_table(temp1)
    temp=item_count(p_list,transaction)
    print_itemCount_table(temp)
    return temp,temp1

"""