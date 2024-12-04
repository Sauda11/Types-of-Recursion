def tail(n):
  if n != 0 :
    print(n)
    tail(n-1)

n = 4
tail(n)