
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
    print("ITEM\t\tCOUNT")
    print ("{:<50} {:<10} {:<10}".format('ITEM', 'CONFIDENCE','SUPPORT'))
# print each data item.
    for key, value in itemDict.items():
        conf,supp = value
        print ("{:<50} {:<10} {:<10}".format(key, conf,supp))
    #for i in itemDict:
        #print("{}\t\t{}".format(i,itemDict[i]))

def print_itemSupport_table(itemDict):
    print("ITEM\t\tSUPPORT")
    #for i in itemDict:
        #print("{}\t\t{}".format(i,itemDict[i]))
    

def item_support(itemSupport):
    itemSupport1={}
    for i in itemSupport:
        itemSupport1[i]=round(itemSupport[i]/20,2)
    return itemSupport1

def list_of_keys(comb_size, newItemSupport_Dict):
    newList=[]
    if comb_size <= 2: 
        for key in newItemSupport_Dict:
            newList.append(key)
    else:
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
            #print('comb',item2)
                if item2 in itemDict2.keys():
                    itemDict2[item2]=itemDict2[item2] + 1
                else:
                    itemDict2[item2] = 1
    return itemDict2

def remove_items(item_data):
    minSupport=0.3
    itemDict3={}
    for i in item_data:
        if(item_data[i]>=minSupport):
            itemDict3[i]=item_data[i]
    return itemDict3 

db1=open('Transaction1.txt')
lines=[]
transaction=[]
itemDict = {}
comb=2

i = 0
for f in db1:
    f = f.rstrip('\n')
    transaction.append(f.split(","))
    line = f.split(",")
    for item in line: 
        if (item in itemDict.keys()):
            itemDict[item] = itemDict[item] + 1
        else: 
            itemDict[item] = 1
print_itemCount_table(itemDict)
newItemSupport_Dict=item_support(itemDict)
itemDict=remove_items(newItemSupport_Dict)

comb=2
i=1
while len(itemDict) > 1:
    midlist=[]
    midlist=list_of_keys(comb, newItemSupport_Dict)
    #print('midlist',i)
    #for j in midlist:
        #print(j)
    combined_data=get_comb_data(comb,midlist)
    #print('comb_ans',i)
    #for j in combined_data:
        #print (j)
    itemDict=item_count(combined_data,transaction)
    print('Count_Table: ',i)
    print_itemCount_table(itemDict)
    newItemSupport_Dict=item_support(itemDict)
    print('Suppoer_Table: ',i)
    print_itemSupport_table(newItemSupport_Dict)
    itemDict=remove_items(newItemSupport_Dict)
    print('itemDict after removing')
    print_itemSupport_table(itemDict)
    comb=comb+1
    i=i+1
print(itemDict)

db1.close()



"""

 #if len(retArr) > 0 and all(x in retArr[rt][0] for x in left) and all(y in retArr[rt][1] for y in right):

for k, v in itemDict.items():
        lang, perc, change = v
        print ("{:<8} {:<15} {:<10} {:<10}".format(k, lang, perc, change))


from typing import final
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
    print("ITEM\t\tCOUNT")
    for i in itemDict:
        print("{}\t\t{}".format(i,itemDict[i]))

def print_itemSupport_table(itemDict):
    print("ITEM\t\tSUPPORT")
    for i in itemDict:
        print("{}\t\t{}".format(i,itemDict[i]))

def item_support(itemSupport):
    itemSupport1={}
    for i in itemSupport:
        itemSupport1[i]=round(itemSupport[i]/20,2)
    return itemSupport1

Giving you each item (single) in a dictionary 
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
            #print('comb',item2)
                if item2 in itemDict2.keys():
                    itemDict2[item2]=itemDict2[item2] + 1
                else:
                    itemDict2[item2] = 1
    return itemDict2

def remove_items(item_data):
    minSupport=0.24
    itemDict3={}
    for i in item_data:
        if(item_data[i]>=minSupport):
            itemDict3[i]=item_data[i]
        else: 
            all_removed_items.append(i)
    return itemDict3 

db1=open('Transaction1.txt')
lines=[]
transaction=[]
itemDict = {}
comb=2
final_answer = {}
all_removed_items = []

i = 0
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
print(itemDict)
comb=2
i=1
while len(itemDict) > 1:
    midlist=[]
    midlist=list_of_keys(comb, newItemSupport_Dict)
    #print('midlist',i)
    #for j in midlist:
        #print(j)
    combined_data=get_comb_data(comb,midlist)
    #print('comb_ans',i)
    #for j in combined_data:
        #print (j)
    itemDict=item_count(combined_data,transaction)
    print('Count_Table: ',i)
    print_itemCount_table(itemDict)
    newItemSupport_Dict=item_support(itemDict)
    print('Suppoer_Table: ',i)
    print_itemSupport_table(newItemSupport_Dict)
    itemDict=remove_items(newItemSupport_Dict)
    print('itemDict after removing')
    print_itemSupport_table(itemDict)
    final_answer.update(itemDict)
    comb=comb+1
    i=i+1
print('Printing final answer')
print(final_answer)
# print('Printing all removed items')
# print(all_removed_items)

Input: List of single items, Output: list permutation

def perm(data):
    if len(data)==0:
        yield []
    elif len(data)==1:
        yield data
    else:
        for i in range(len(data)):
            x=data[i]
            xs=data[:i] + data[i+1:]
            for p in perm(xs):
                yield [x]+p
    
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
                print('they both are already in ret list')
            else: 
                retArr.append([ left , right])
            pointer = pointer +1

    return retArr
            
final_list=list_of_keys(3,final_answer)
print('Fianl_list')
print(final_list)
print("Permutations")
eachPermList = []
association_list=[]
for each in final_list: 
    for eachPerm in perm(each):
        eachPermList.append(eachPerm)
print(eachPermList)
print('association_list')
association_list=association(eachPermList)
print(association_list)
db1.close()









"""