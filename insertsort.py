def inserter(arr,x):
  arr2=[]
  inserted=False
  for i in arr:
    if(x<i and inserted==False):
      arr2.append(x)  
      inserted=True
    arr2.append(i)
  if inserted==False:
    arr2.append(x)
  return arr2
def insertsort(arr):
  arr2=[]
  for i in arr:
    arr2=inserter(arr2,i)
  return arr2
insertsort([1,2,66,44,99,1])
