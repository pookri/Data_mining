import math
def truncate(number, digits) -> float:
    step = 10.0 ** digits
    return math.trunc(step * number) / step

db1=open('Transaction1.txt')
lines=[]
transaction=[]
itemDict = {}
itemDict1={}
midlist=[]
comb=2
comb_data=[]
comb_data1=[]
comb_ans=[]
itemDict2={}
itemDict3={} 
itemDict4={} 
itemDict5={} 
itemDict6={}
itemDict7={}        
comb_ans1=[]
midlist1=[] 
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

print("ITEM\t\tCOUNT")
for i in itemDict:
    print("{}\t\t{}".format(i,itemDict[i]))

for i in itemDict:
   itemDict1[i]=round(itemDict[i]/20,2)

print("\nITEM\t\tSUPPORT")
#for i in itemDict1:
   # print("{}\t\t{}".format(i,itemDict1[i]))
for key in itemDict1:
    midlist.append(key)
print('midlist')
for i in midlist:
    print(i)
#combination function
def combination(comb_size,item_data,comb_data):
    if len(comb_data) == comb_size:
        yield comb_data
    elif len(item_data) == 0 : 
        pass
    else:
        item = item_data.pop(0)
        comb_data.append(item)
        for j in combination(comb_size,item_data[:],comb_data[:]):
            yield j
        comb_data.pop()
        for j in combination(comb_size,item_data[:],comb_data[:]):
            yield j


for i in combination(comb,midlist,comb_data):
    comb_ans.append(i)
    
print('comb_ans')
for i in comb_ans:
    print (i)
print('transaction')
for j in transaction:
    print(j)

for j in range(len(comb_ans)):
    for k in range(len(transaction)):
        trans_set=set(transaction[k])
        comb_set=set(comb_ans[j])
        if(comb_set.issubset(trans_set)):
            item2=str(comb_set)
            #print('comb',item2)
            if item2 in itemDict2.keys():
                itemDict2[item2]=itemDict2[item2] + 1
            else:
                itemDict2[item2] = 1
 
for i in itemDict2:
   itemDict3[i]=round(itemDict2[i]/20,2)

for i in itemDict3:
    if(itemDict3[i]>=0.3):
        itemDict4[i]=itemDict3[i]

for key in itemDict4:
    midlist1.append(key)
print('midlist1')
for i in midlist1:
    print(i)
for i in combination(3,midlist1,comb_data1):
    comb_ans1.append(i)

print('comb_ans')
for i in comb_ans1:
    print(i)


for j in range(len(comb_ans1)):
    for k in range(len(transaction)):
        trans_set=set(transaction[k])
        comb_set1=set(comb_ans1[j])
        if(comb_set1.issubset(trans_set)):
            item2=str(comb_set1)
            #print('comb',item2)
            if item2 in itemDict5.keys():
                itemDict5[item2]=itemDict5[item2] + 1
            else:
                itemDict5[item2] = 1
    
for i in itemDict5:
   itemDict6[i]=round(itemDict5[i]/20,2)

for i in itemDict6:
    if(itemDict6[i]>=0.3):
        itemDict7[i]=itemDict6[i]

for it in itemDict7:
    print("{}\t\t{}".format(it,itemDict7[it]))

db1.close()








"""
comb_set1=set(i)
    print(i)
    if(comb_set1.issubset(trans_set)):
        item2=str(comb_set1)
        #print('comb',item2)
        if item2 in itemDict5.keys():
            itemDict5[item2]=itemDict5[item2] + 1
        else:
            itemDict5[item2] = 1



for j in range(len(comb_ans)):
    for k in range(len(transaction)):
        if(transaction[k]==comb_ans[j]):
            item2=comb_ans[j]
            itemDict2[item2]=itemDict2[item2] + 1
            #print('match')



from tabulate import tabulate
def remove_newlines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]


print ("{:<10} {:<10}".format('ITEM', 'SUPPORT'))
 
# print each item_data item.
for key, value in itemDict.items():
    item, support = value
    print ("{:<10} {:<10} {:<10}".format(item, support))


for each_row in zip(*([i] + (j)
                      for i, j in itemDict.items())):
     
      print(*each_row, " ")

#print(tabulate(itemDict,headers=["items","support"]))
#test=db1.split(",")
res=dict()

for i in range(1,6):
    lines.append( {i:itemDict} )
    i = i + 1

#for idx, ele in lines:
#    res[idx] = ele
#    print(res)

"""