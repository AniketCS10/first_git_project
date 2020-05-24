# d={'a':10, 'b':20}
# print(dir(d))
##old way
# d={}
# d={'a':10, 'b':20}
# print(d)
###new way get data from dict
# d=dict()
# d=dict(a=10,b=20)
# print(d['a'])
# # print(d['c'])##gives error so we should use get ()
# print(d.get('c',0))

##clear()
# d=dict(a=10,b=20)
# d.clear()
# print(d)

##copy()
# d1=dict(c=['praj','undo'])
# d1['a']=['aniket','surve']
# d2=d1.copy()
# print(d2)

##fromkeys
# x = ('key1', 'key2', 'key3')
# # z=dict({('a',1),('b',2),('c',3)})
# y = (1,2,3)
# thisdict = dict.fromkeys(x, y)
#
# print(thisdict)

##get
# d=dict(a=10,b=20)
# print(d['a'])
# # print(d['c'])##gives error so we should use get ()
# print(d.get('c',0))

## pop
# d={'a':10, 'b':20 , 'c':30}
# d.pop('a')
# print(d)
# # print(d.pop('x'))##gives error so we should use default value as any 0 to 100
# print(d.pop('x',100))


## del or remove
# d={'a':10, 'b':20 , 'c':30}
# del(d['c'])
# print(d)

## popitem
# d={'a':10, 'b':20 , 'c':30,'d':40}
# val=d.popitem()
# print(val)

## setdefault
# d={'a':10,'b':20,'c':30}
# d.setdefault('d',100)
# print(d)

## update
# d={'a':10, 'b':20 , 'c':30}
# d1={'d':40,'e':50}
# d.update(d1)
# print(d)

## items
# sales = {'apple': 2, 'orange': 3, 'grapes': 4}
# print(sales.items())
# random sales dictionary
# sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
#
# items = sales.items()
# print('Original items:', items)
#
# # delete an item from dictionary
# del[sales['apple']]
# print('Updated items:', items)

## keys
# x={'a':10, 'b':20 , 'c':30}
# for item in x.keys():
#  print (item)
 # for key in d:
 # # print(d[key])
# print("%s=%s" %(key,d[key]))

## values
# d={'a':10, 'b':20 , 'c':30}
# for item in d.values():
#  print (item)
#  print(d.keys())
#  print(d.values())
# for values in d:
#   print(d[values])

#items()
# d={'a':10, 'b':20 , 'c':30}
# for k,v in d.items():
#     print("key={},value={}" .format(k,v))