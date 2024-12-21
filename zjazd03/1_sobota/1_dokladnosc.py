a = 0.1
b = 0.2
c = 0.3
print(a+b==c)  #false, niedokładność programowania

#Rozwiązanie

a = 0.1
b = 0.2
ab = a + b
c = 0.3
e = 1e-9  #0.0000000001

print(abs(ab - c) < e)