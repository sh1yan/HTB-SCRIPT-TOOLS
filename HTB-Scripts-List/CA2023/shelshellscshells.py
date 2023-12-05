#!/usr/bin/python3

t = "2c4ab799a3e57078936e97d9476d38bdffbb85996fe14aab74c37ba8b29fd7ecebcd63b23923e184929609c699f258facb6f6f5e1fbe2b138ea5a99993ab8f701cc0c43ea6fe933590c3c910e9"
m1 = "6e3fc3b9d78d1558e50ffbac224d57dbdfcfedfc1c846ad81ca617c4c1bfa08587a143d4584f8da8b2f27ca3b98637dabf070a7e73df5c60aecacfb9e0deff0070b9e45fc89ab351f5aea87e8d"
m2 = "641ef5e2c097441bf85ff9be185d488e91e4f6f15c8d269e2ba102f7c6f7e4b398fe57ed4a4bd1f6a1eb09c699f258facb6f6f5e1fbe2b138ea5a99993ab8f701cc0c43ea6fe933590c3c910e9"  

t = bytes.fromhex(t)
m1 = bytes.fromhex(m1)
m2 = bytes.fromhex(m2) 

result1 = bytes([t[i] ^ m1[i] for i in range(len(t))])
result2 = bytes([t[i] ^ m2[i] for i in range(len(t))])  

print(result1.decode())
print(result2.decode())
