def way(arr,j):
  if (not isinstance(arr[j],bool)):
   print(str(j)+' ⇒ ',end='')
   way(arr,arr[j])
  else:
    print(j)