#setting variabel
a=10
b=20
c=50

def 1A(a , b, c) :
  result=((a+b)*(b*c))/(a+b+c) 
  return result

def 2B(a, b, c) :
  p=a
  l=b
  t=c
  result=p*l*t
  return result


def 3C(a, c):
  t=c
  result=0.5*a*c
  return result


def 4D(a, b, c, d) :
  result=(((a+b) *2) +((b*c) *2))/(a*b) 
  return result

print(f"Hasil A={menghitung A(a, b, c) }") 
print(f"Hasil B={menghitung B(a, b, c) }") 
print(f"Hasil C={menghitung C(a, c) }") 
print(f"Hasil D={menghitung D(a, b, c)}") 
