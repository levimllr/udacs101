print ((1234 - 10**4)*(1234/10**4))
print ('|00000*****|'[:11-int(234/(10**3))])
print (len(str(1200)))
print (int(1234 - 10**3))

def print_abacus(value):
    i = len(str(value))
    num = int(value)
    while i >= 0:
      print ('|00000*****|'[:11-int(num/(10**i))] + '   ' + '|00000*****|'[11-int(num/(10**i)):])
      num = num - int(num/10**i)*10**i
      i = i - 1

print_abacus(374869041)
