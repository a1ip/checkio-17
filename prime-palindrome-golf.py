def golf(n):
 while 1:
  n+=1
  if not any(n%i==0 for i in range(2,n))and str(n)==str(n)[::-1]:return n