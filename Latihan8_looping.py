# for loops
#for i in range(1,10):
  #print(i)
list_dosen=("wawan","salim","dedi","lukman")
list_jadwal=("senin","selasa","rabu","kamis","jumat")

for i in (list_dosen):
  for k in (list_jadwal):
    print(1,"-",k)


...
#fibonanci
n=10
fib= [0,1]

for i in range(n-2):
  fib_lanjut= fib[i+1] + fib[i]
  print(fib[i+1]," + ", fib[i]," = ",fib_lanjut)
  fib.append(fib_lanjut)
